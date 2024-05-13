import numpy as np
import matplotlib.pyplot as plt

# Tridiagonal matrix algorithm for assignment XI.9.5

h = 0.005
N = int(1.0/h)

def f(x):
    return np.cos(2 * np.pi * x)

def p2(x):
    return 10 + np.sin(2 * np.pi * x)

def tridiagonalAlgorithm(A, B, C, r, N):
    alpha = np.zeros(N)
    beta = np.zeros(N)
    gamma = np.zeros(N)
    mu = np.zeros(N)
    nu = np.zeros(N)
    Y = np.zeros(N)

    alpha[1] =  C[0] / B[0]
    beta[1]  = -r[0] / B[0]
    gamma[1] =  A[0] / B[0]

    for i in range(1, N - 1):
        alpha[i + 1] = C[i] / (B[i] - alpha[i] * A[i])
        beta[i + 1]  = (A[i] * beta[i] - r[i]) / (B[i] - alpha[i] * A[i])
        gamma[i + 1] = (A[i] * gamma[i]) / (B[i] - alpha[i] * A[i])

    mu[N-1] = -C[N-1] / (A[N-1] * (alpha[N-1] + gamma[N-1]) - B[N-1])
    nu[N-1] = (r[N-1] - A[N-1] * beta[N - 1]) / (A[N-1] * (alpha[N - 1] + gamma[N - 1]) - B[N-1])

    for i in range(N - 2, -1, -1):
        mu[i] = alpha[i + 1] * mu[i + 1] + gamma[i + 1] * mu[N - 1]
        nu[i] = alpha[i + 1] * nu[i + 1] + gamma[i + 1] * nu[N - 1] + beta[i + 1]

    y0 = nu[0] / (1 - mu[0])
    yN = mu[N-1] * y0 + nu[N-1]

    Y[0] = y0
    Y[N-1] = yN

    for i in range(N - 1, 0, -1):
        Y[i - 1] = alpha[i] * Y[i] + beta[i] + gamma[i] * yN

    return Y

def plotSolutions(X, Y, h):
    plt.grid(color='gray', linestyle='--')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("1 период")
    plt.plot(X, Y, color='orange')
    plt.savefig("img/1Period")
    plt.show()

    plt.grid(color='gray', linestyle='--')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("5 периодов")
    plt.plot(np.arange(0, 5.0, h), np.tile(Y, 5), color='green')
    plt.savefig("img/4Periods")
    plt.show()

# Initial values
A = np.zeros(N)
B = np.zeros(N)
C = np.zeros(N)
r = np.zeros(N)
h2 = h**2

for i in range(0, N):
    A[i] = 1.0
    B[i] = 2.0 + p2(i * h) * h2
    C[i] = 1.0
    r[i] = f(i * h) * h2

# Solve and plot
Y = tridiagonalAlgorithm(A, B, C, r, N)
X = np.arange(0, 1.0, h)
plotSolutions(X, Y, h)