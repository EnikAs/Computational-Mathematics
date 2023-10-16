import matplotlib.pyplot as plt
import scipy
import scipy.linalg
import math
import numpy as np

def make_equations(n):
    matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        if i < 5:
            matrix[i, :i+5] = 1
        elif i < 95:
            matrix[i, i-4:i+5] = 1
        else:
            matrix[i, i-4:] = 1
    np.fill_diagonal(matrix, 10)

    f = np.array([n - i for i in range(0, n)])

    return matrix, f

def Gauss_method(A, b):
    n = len(A)

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[max_row, i]):
                max_row = j

        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x
        
def minors_are_degenerated(matrix):
    assert matrix.shape[0] == matrix.shape[1]
    n = matrix.shape[0]
    for i in range(1, n + 1):
        submatrix = matrix[:i, :i]
        if np.linalg.det(submatrix) == 0:
            return True
    return False

def LU_decomposition(A, b, n):
    P, L, U = scipy.linalg.lu(A)
    y = np.zeros(n)
    
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= y[j] * L[i][j]
    
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

def Jacobi_method(A, b, it, x):
    if x is None:
        x = np.zeros(len(A[0]))

    D = np.diag(A)
    R = A - np.diagflat(D)
    errs = np.zeros(it)

    for i in range(it):
        x_new = np.zeros_like(x)
        for j in range(len(A)):
            x_new[j] = (b[j] - np.dot(R[j], x)) / D[j]

        diff = b - np.matmul(A, x_new)
        errs[i] = np.linalg.norm(diff)
        x = x_new

    return x, errs

def Seidel_method(A, b, it, x):
    if x is None:
        x = np.zeros(len(A[0]))
        
    D = np.diagflat(np.diag(A))
    U = np.triu(A) - D
    L = np.tril(A) - D
    inv = np.linalg.inv(L + D)
    R = -np.dot(inv, U)
    F = np.dot(inv, b)
    errs = np.zeros(it)

    for i in range(it):
        x_new = F + np.dot(R, x)
        diff = b - np.matmul(A, x_new)
        errs[i] = np.linalg.norm(diff)
        x = x_new

    return x, errs

def upper_relaxation_method(A, b, w, N):
    x = np.zeros(len(A[0]))
    data = np.zeros(N)
    L = np.tril(A, -1)
    D = np.diag(np.diag(A))
    U = np.triu(A, 1)
    B = -np.linalg.inv(D + w * L).dot((w - 1) * D + w * U)
    F = np.linalg.inv(D + w * L).dot(b) * w

    for i in range(N):
        x = B.dot(x) + F
        diff = b - A.dot(x)
        data[i] = np.linalg.norm(diff)
        
    return x, data

def add_line_in_graph(y_array, label = '', color ='b', marker='^', linestyle='-'):
    it = [i for i in range(len(y_array))]
    plt.plot(it, y_array, label=label, color=color, marker=marker, linestyle=linestyle)

def show_graph(method_name):
    plt.yscale('log')

    plt.grid()

    plt.legend()

    plt.xlabel('Iteration number')
    plt.ylabel('$\lg(Accuracy)$')

    title = 'Graph for' + ' ' + method_name + ' method'
    print(title)
    plt.title(title)
    
    plt.savefig(title)

N = 100 # Number of linear equations
ITERATIONS = 30 # Number of iterations in iterations methods
EPSILON = 1e-6 # Precision

colors = ["red", "green", "blue", "yellow", "orange", "purple",
           "pink", "blue", "brown", "black", "violet", "gray",
           "turquoise", "lime", "raspberry", "lavender"]

# Gauss method
print("1) Gaussian elimination method")
A, b = make_equations(N)
sol = Gauss_method(A, b)
if np.linalg.norm(np.matmul(A,sol) - b) > EPSILON:
    print("Error: wrong solution")
else:
    print("OK")

# LU
print("2) LU-decomposition method")
A, b = make_equations(N)
if minors_are_degenerated(A) == False:
    sol = LU_decomposition(A, b, N)
    if np.linalg.norm(np.matmul(A, sol) - b) > EPSILON:
        print("Error: wrong solution")
    else:
        print("OK")

else:
    print("\nCan't decompose A to LU!")

# 3) Seidel method
A, b = make_equations(N)
x0 = np.zeros(N)
sol, errs = Seidel_method(A, b, ITERATIONS, x0)
plt.figure(figsize=(13, 7))
add_line_in_graph(errs, colors[0])
show_graph("Seidel")
plt.clf()

# 4) Jacoby method
A, b = make_equations(N)
x0 = np.zeros(N)
sol, errs = Jacobi_method(A, b, ITERATIONS, x0)
plt.figure(figsize=(13, 7))
add_line_in_graph(errs, colors[0])
show_graph("Jacoby")
plt.clf()

# 5) Upper relaxation method
plt.figure(figsize=(11, 9))
for i, w in enumerate(np.arange(1.0, 2.5, 0.1)):
    w = math.ceil(w * 10) / 10
    x, dt = upper_relaxation_method(A, b, w, ITERATIONS)
    add_line_in_graph(dt, "w = " + str(w), colors[i-1])

show_graph("Upper relaxation")
