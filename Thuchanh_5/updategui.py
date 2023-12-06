import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Initialize the OpenCV window
cv2.namedWindow("Image Smoothing", cv2.WINDOW_NORMAL)

# Initialize the image and filter variables
img = None
original_img = None
filter_strength = 1

# Define the kernels for filtering
kernels = [
    np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    np.ones((3, 3), np.float32) / 9.0,
    np.ones((5, 5), np.float32) / 25.0
]

# Function to update the filtered image
def update_filtered_image():
    global img, original_img, filter_strength
    if original_img is not None:
        img = original_img.copy()
        for _ in range(filter_strength):
            img = cv2.filter2D(img, -1, kernels[filter_strength - 1])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        label.config(image=img)
        label.image = img

# Function to open a file dialog and load an image
def open_image():
    global original_img, img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        img = original_img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        label.config(image=img)
        label.image = img
        update_filtered_image()

# Function to increase the filter strength
def increase_strength():
    global filter_strength
    if filter_strength < 2:
        filter_strength += 1
    update_filtered_image()

# Create the main window
window = tk.Tk()
window.title("Image Smoothing")

# Create a button to open an image
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

# Create a label to display the image
label = tk.Label(window)
label.pack()

# Create a button to apply the 3x3 filter
filter_3x3_button = tk.Button(window, text="Apply 3x3 Filter", command=increase_strength)
filter_3x3_button.pack()

# Create a button to apply the 5x5 filter
filter_5x5_button = tk.Button(window, text="Apply 5x5 Filter", command=increase_strength)
filter_5x5_button.pack()

# Start the GUI main loop
window.mainloop()
