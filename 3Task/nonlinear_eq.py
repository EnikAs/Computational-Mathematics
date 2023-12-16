import math
import matplotlib.pyplot as plt
import numpy as np
import os

def calculate_x_next(x: float) -> float:
    return 4.0 * math.log10(x) + 2.0

def calculate_deriv(func, x: float, h: float) -> float:
    return (func(x + h) - func(x)) / h

def calculate_F(x: float) -> float:
    return 2.0 * math.log10(x) - x / 2.0 + 1

def plot_graph(xs, title, xlabel, ylabel, save_path):
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(xs, '.-', color='blue', linewidth=1.5, markersize=5.0)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.clf()

def mpi_method():
    eps: float = 1e-4
    prev_x = 10.0
    xs = [prev_x]
    new_x = calculate_x_next(prev_x)
    while abs(new_x - prev_x) > eps:
        prev_x = new_x
        xs.append(prev_x)
        new_x = calculate_x_next(prev_x)
    plot_graph(xs, "MPI eq", "Step", "X", "img/x_n_mpi.png")
    print(f"MPI eq = {new_x}")

def newton_method():
    eps: float = 1e-4
    prev_x = 10.0
    h = 1e-3
    dFdx = calculate_deriv(calculate_F, prev_x, h)
    new_x = prev_x - calculate_F(prev_x) / dFdx
    xs = [prev_x]
    while abs(new_x - prev_x) > eps:
        prev_x = new_x
        dFdx = calculate_deriv(calculate_F, prev_x, h)
        new_x = prev_x - calculate_F(prev_x) / dFdx
        xs.append(new_x)
    plot_graph(xs, "Newton eq", "Step", "X", "img/x_n_newton.png")
    print(f"Newton eq = {new_x}")

def x_from_eq(y):
    return 1 - math.cos(y) / 2

def y_from_eq(x):
    return math.sin(x + 1) - 1.2

def mpi_system():
    eps: float = 1e-4
    prev_x = 15.0
    prev_y = 15.0
    xs = [prev_x]
    ys = [prev_y]
    new_x = x_from_eq(prev_y)
    new_y = y_from_eq(prev_x)
    while (abs(new_x - prev_x) > eps) and (abs(new_y - prev_y) > eps):
        prev_x = new_x
        prev_y = new_y
        xs.append(prev_x)
        ys.append(prev_y)
        new_x = x_from_eq(prev_y)
        new_y = y_from_eq(prev_x)
    print('MPI system = (', new_x, ',', new_y, ')')
    plot_graph(xs, "MPI system", "X", "Y", "img/system_mpi.png")

def newton_system():
    eps: float = 1e-4
    prev_x = 13.0
    prev_y = 13.0
    xs = [prev_x]
    ys = [prev_y]
    dF = np.zeros((2, 2))
    dF[0][0] = math.cos(prev_x + 1)
    dF[0][1] = -1
    dF[1][0] = 2
    dF[1][1] = -math.sin(prev_y)
    new_x = prev_x - (np.linalg.inv(dF) @ [math.sin(prev_x + 2) - prev_y - 1.5, prev_x + math.cos(prev_y - 2) - 0.5])[0]
    new_y = prev_y - (np.linalg.inv(dF) @ [math.sin(prev_x + 2) - prev_y - 1.5, prev_x + math.cos(prev_y - 2) - 0.5])[1]
    xs.append(new_x)
    ys.append(new_y)
    while (abs(new_x - prev_x) > eps) and (abs(new_y - prev_y) > eps):
        prev_x = new_x
        prev_y = new_y
        dF[0][0] = math.cos(prev_x + 1)
        dF[0][1] = -1
        dF[1][0] = 2
        dF[1][1] = -math.sin(prev_y)
        new_x = prev_x - (np.linalg.inv(dF) @ [math.sin(prev_x + 2) - prev_y - 1.5, prev_x + math.cos(prev_y - 2) - 0.5])[0]
        new_y = prev_y - (np.linalg.inv(dF) @ [math.sin(prev_x + 2) - prev_y - 1.5, prev_x + math.cos(prev_y - 2) - 0.5])[1]
        xs.append(new_x)
        ys.append(new_y)
    print('Newton system = (', new_x, ',', new_y, ')')
    plot_graph(xs, "Newton system", "X", "Y", "img/system_newton.png")

mpi_method()
newton_method()
mpi_system()
newton_system()