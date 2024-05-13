import numpy as np
import matplotlib.pyplot as plt

# Shooting method for assignment XI.9.3(a)
eps = 1e-7
h = 4e-5

def diff2Y(x, Y):
    return x * np.sqrt(Y)

def getY(X, y0, alpha, h):
    Y = []
    y = y0
    dy = alpha

    for x in X:
        Y.append(y)
        y += dy * h
        dy = calculateY(x, dy, diff2Y)

    plt.plot(X, Y)
    return Y

def calculateY(x, y0, dY):
    h = 4e-5
    Yn = y0 + dY(x, y0) * h

    for i in range(1000):
        if abs(Yn - y0) <= 1e-4:
            return Yn
        y0 = Yn
        Yn = y0 + dY(x, y0) * h

    return Yn

def shooting(X, y0, y1, alpha, ha, h, eps):
    Y = getY(X, y0, alpha, h)
    F = Y[-1] - y1

    while abs(F) > eps:
        Y = getY(X, y0, alpha + ha, h)
        alpha = alpha - F / ((Y[-1] - y1 - F) / ha)
        Y = getY(X, y0, alpha, h)
        F = Y[-1] - y1

    return Y, alpha

def plotSolution(X, Y, alpha):
    plt.grid(color='gray', linestyle='--')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(X, Y, label="solution", color='blue')
    plt.title(f"Alpha = {alpha:.6f}")
    plt.savefig("img/Solution")
    plt.show()

# Initial values
y0 = 0
y1 = 2
alpha = 0
X = np.arange(0.0, 1.0, h)

# Solve and plot
Y, alpha = shooting(X, y0, y1, alpha, 1e-2, h, eps)
plotSolution(X, Y, alpha)