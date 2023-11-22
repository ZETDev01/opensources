#1-	Thiết kế phần mềm ứng dụng giải hệ phương trình tuyến tính n phương trình n ẩn
import numpy as np
n=int(input('Nhập số phương trình: '))
while (n<=0):
  n = int(input('Nhập số phương trình: '))
m=int(input('Nhập số ẩn: '))
while (m<=0):
  m = int(input('Nhập số ẩn: '))

X=np.zeros((n,m))
x=np.zeros(n)
print("Nhập ma trận hệ số X: ")
for i in range(n):
  for j in range(m):
    X[i][j]=float(input(f"A[{i+1},{j+1}]: "))
print("Nhập vector x: ")
for i in range(n):
  x[i]=float(input(f"b[{j+1}]: "))
kq=np.linalg.solve(X,x)
print("Nghiệm phương trình là: ",kq)

