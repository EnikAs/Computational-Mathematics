import functions
import dif_formulas
import deriv_funcs
import matplotlib.pyplot as plt
import inspect
import math
import numpy as np
import array

X_0 = 10
ctoto = 0

def add_line_in_graph(x_array, y_array, label,  color, marker='^', linestyle='-'):
    plt.plot(x_array, y_array, label=label, color=color, marker=marker, linestyle=linestyle)

def show_graph(func_name):
    plt.yscale('log')
    plt.xscale('log')

    plt.grid()

    plt.legend()

    plt.xlabel('$h_n$')
    plt.ylabel('$delta_f$\'')

    title = 'График для функции' + ' ' + func_name
    print(title)
    plt.title(title)
    
    plt.savefig(title)

if __name__ == "__main__":

    func_arr = []
    for name, obj in inspect.getmembers(functions):
        if inspect.isfunction(obj):
            func_arr.append(obj)

    dif_arr = []
    for name, obj in inspect.getmembers(dif_formulas):
        if inspect.isfunction(obj):
            dif_arr.append(obj)

    deriv_arr = []
    for name, obj in inspect.getmembers(deriv_funcs):
        if inspect.isfunction(obj):
            deriv_arr.append(obj)

    real_derivative = 0

    colors = ['r', 'b', 'black', 'g', 'magenta']

    for i in range(0, functions.NUMBER_OF_FUNCS):
        real_derivative = deriv_arr[i](X_0)

        for j in range(0, dif_formulas.NUMBER_OF_DIFS):
            h = 2
            y_array = array.array('f')
            x_array = array.array('f')

            for n in range(1, 22):
                h /= 2
                x_array.append(h)
                y_array.append(math.fabs(real_derivative - dif_arr[j](func_arr[i], X_0, h)))

            add_line_in_graph(x_array, y_array, dif_formulas.LABELS[j], colors[j%len(colors)])

        show_graph(functions.FUNCS_NAMES[i])
        plt.clf()
