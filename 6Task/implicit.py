import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def solve_eq(get_jacobian, get_sys_equation, initial_vector, stop_iter_epsilon):
    n_iters = 0
    vector_k_next = np.copy(initial_vector)
    vector_k = np.copy(initial_vector) + np.ones(len(initial_vector)) * 2 * stop_iter_epsilon
    while np.abs(np.linalg.norm(vector_k, ord=np.inf) - np.linalg.norm(vector_k_next, ord=np.inf)) > stop_iter_epsilon and n_iters <= 30000:
        vector_k = np.copy(vector_k_next)
        vector_k_next = vector_k - np.dot(np.linalg.inv(get_jacobian(vector_k)), get_sys_equation(vector_k))
        n_iters += 1
    return vector_k_next, n_iters

def solve_diff_eq(h_step, t_start, t_end, x0_vec, diff_function, method):
    assert(t_start <= t_end)
    assert(h_step > 0)
    n_steps = int((t_end - t_start) / h_step) + 1
    t = np.linspace(t_start, t_end, n_steps)
    x_vec = np.zeros((n_steps, np.shape(x0_vec)[0]))
    for i in range(np.shape(x0_vec)[0]):
        x_vec[0][i] = x0_vec[i]
    return method(h_step, t, x_vec, diff_function)

def function_lab2(t, x_vec):
    return np.array([77.27 * (x_vec[1] + x_vec[0] * (1 - 8.375 * 10 ** (-6) * x_vec[0] - x_vec[1])),
                     1.0 / 77.27 * (x_vec[2]  - (1 + x_vec[0]) * x_vec[1]),
                     0.161 * (x_vec[0] - x_vec[2])])

def get_jacobian_lab2(x_vec):
    return np.array([[77.27 * (1 - x_vec[0] * 2 * 8.375 * 10 ** (-6) - x_vec[1]),
                      77.27 * (1 - x_vec[0]), 0],
                     [-1/77.27 * x_vec[1], 1 / 77.27 * (-1 - x_vec[0]), 1 / 77.27],
                     [0.161, 0, -0.161]])

def get_gear_jacobian_func(h_step, get_jacobian_func, x_vec):
    return lambda x: np.eye(np.shape(x_vec)[0]) - 6 * h_step / 11 * get_jacobian_func(x)

def get_euler_jacobian_func(h_step, get_jacobian_func, x_vec):
    return lambda x: np.eye(np.shape(x_vec)[0]) - h_step * get_jacobian_func(x)

def get_gear_sys_equation_func(h_step, function, x_vec, t, x_free_vec):
    return lambda x: x - 6 * h_step / 11 * function_lab2(t, x) + x_free_vec

def get_euler_sys_equation_func(h_step, function, x_vec, t, x_free_vec):
    return lambda x: x - h_step * function_lab2(t, x) + x_free_vec

def method_gear_3d_order(h_step, t, x_vec, diff_function):
    n_steps = np.shape(x_vec)[0]
    f_vec = np.zeros((n_steps, np.shape(x_vec[0])[0]))
    f_vec[0] = diff_function(t[0], x_vec[0])
    x_vec[1] = x_vec[0] + h_step * f_vec[0]
    f_vec[1] = diff_function(t[1], x_vec[1])
    x_vec[2] = x_vec[1] + h_step * f_vec[1]
    f_vec[2] = diff_function(t[2], x_vec[2])
    for j in range(3, np.shape(t)[0]):
        x_free_vec = -18 / 11 * x_vec[j - 1] + 9 / 11 * x_vec[j - 2] - 2 / 11 * x_vec[j - 3]
        x_start_vec = x_vec[j - 1] + h_step * (23 / 12 * f_vec[j - 1] - 16 / 12 * f_vec[j - 2] + 5 / 12 * f_vec[j - 2])
        x_vec[j], n_iters = solve_eq(get_gear_jacobian_func(h_step, get_jacobian_lab2, x_vec[j]), \
                                     get_gear_sys_equation_func(h_step, diff_function, x_vec[j], t[j], x_free_vec), \
                                     x_start_vec, 1e-6)
        f_vec[j] = diff_function(t[j], x_vec[j])
    return t, x_vec

t_step, solution_vec = solve_diff_eq(0.01, 0, 800, np.array([4, 1.1, 4]), function_lab2, method_gear_3d_order)

figure = plt.figure()
gs = GridSpec(ncols=1, nrows=1, figure=figure)
axes = figure.add_subplot(gs[0, 0])
axes.minorticks_on()
axes.grid(which='major', linewidth=2, color='#919191')
axes.grid(which='minor', linestyle=':')

x1 = np.array([solution_vec[i][0] for i in range(np.shape(solution_vec)[0])])
x2 = np.array([solution_vec[i][1] for i in range(np.shape(solution_vec)[0])])
x3 = np.array([solution_vec[i][2] for i in range(np.shape(solution_vec)[0])])

axes.plot(t_step, x1, c='lawngreen', label='x1')
axes.plot(t_step, x2, c='darkred', label='x2')
axes.plot(t_step, x3, c='teal', label='x3')

axes.legend()
axes.set_xlabel('t')
axes.set_ylabel('value')
plt.savefig("img/" + 'lab2')