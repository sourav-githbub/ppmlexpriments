import numpy as np
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
print(A)
print(B)
result_matmul = A @ B
print(result_matmul)
result_dot = np.dot(A, B)
print(result_dot)