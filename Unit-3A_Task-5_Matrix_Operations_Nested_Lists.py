a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print("Matrix A:")
for i in a:
    print(i)

print("Matrix B:")
for i in b:
    print(i)

# Matrix Addition
print("Addition:")
for i in range(2):
    for j in range(2):
        print(a[i][j] + b[i][j], end=" ")
    print()

# Matrix Subtraction
print("Subtraction:")
for i in range(2):
    for j in range(2):
        print(a[i][j] - b[i][j], end=" ")
    print()

# Matrix Transpose
print("Transpose of Matrix A:")
for i in range(2):
    for j in range(2):
        print(a[j][i], end=" ")
    print()