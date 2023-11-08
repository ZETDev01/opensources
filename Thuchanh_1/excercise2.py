import tkinter as tk
from tkinter import messagebox
import numpy as np
from sympy import symbols, diff, integrate, Eq, solve


def create_equations():
  num_equations = int(num_equations_entry.get())

  for widget in equations_frame.winfo_children():
    widget.destroy()

  equation_entries.clear()

  for i in range(num_equations):
    equation_frame = tk.Frame(equations_frame)
    equation_frame.pack()
    equation_entries_row = []

    for j in range(num_equations + 1):
      equation_entry = tk.Entry(equation_frame)
      equation_entry.grid(row=i, column=j)
      equation_entries_row.append(equation_entry)

    equation_entries.append(equation_entries_row)


def solve_equations():
  try:
    coefficients = []
    results = []

    for entry_row in equation_entries:
      equation_coefficients = []
      for entry in entry_row[:-1]:
        value = float(entry.get())
        equation_coefficients.append(value)
      coefficients.append(equation_coefficients)
      result_value = float(entry_row[-1].get())
      results.append(result_value)

    A = np.array(coefficients)
    b = np.array(results)

    solution = np.linalg.solve(A, b)
    result_text.config(text="Nghiệm phương trình là: " + str(solution))
  except np.linalg.LinAlgError:
    messagebox.showerror("Lỗi", "Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")
  except ValueError:
    messagebox.showerror("Lỗi", "Giá trị nhập không hợp lệ trong ma trận.")


def differentiate_expression():
  try:
    x = symbols('x')
    expression = input("Nhập biểu thức cần tính đạo hàm theo x: ")
    expr = diff(expression, x)
    result_text.config(text=f"Đạo hàm của {expression} theo x là: {expr}")
  except ValueError:
    messagebox.showerror("Lỗi", "Biểu thức không hợp lệ.")


def integrate_expression():
  try:
    x = symbols('x')
    expression = input("Nhập biểu thức cần tính tích phân theo x: ")
    expr = integrate(expression, x)
    result_text.config(text=f"Tích phân của {expression} theo x là: {expr}")
  except ValueError:
    messagebox.showerror("Lỗi", "Biểu thức không hợp lệ.")


# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Phần mềm hỗ trợ học tập môn giải tích")

equation_entries = []

equations_frame = tk.Frame(window)
equations_frame.pack(padx=20, pady=20)

num_equations_label = tk.Label(equations_frame, text="Nhập số phương trình:")
num_equations_label.grid(row=0, column=0)
num_equations_entry = tk.Entry(equations_frame)
num_equations_entry.grid(row=0, column=1)

create_button = tk.Button(equations_frame, text="Tạo Hệ Phương Trình", command=create_equations)
create_button.grid(row=0, column=2)

solve_button = tk.Button(equations_frame, text="Giải Hệ Phương Trình", command=solve_equations)
solve_button.grid(row=0, column=3)

differentiate_button = tk.Button(equations_frame, text="Tính Đạo Hàm", command=differentiate_expression)
differentiate_button.grid(row=1, column=0)

integrate_button = tk.Button(equations_frame, text="Tính Tích Phân", command=integrate_expression)
integrate_button.grid(row=1, column=1)

result_text = tk.Label(equations_frame, text="")
result_text.grid(row=2, column=0, columnspan=4)

window.mainloop()
