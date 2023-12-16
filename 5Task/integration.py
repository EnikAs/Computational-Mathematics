import matplotlib
import math
import numpy as np

# VII.9.5(б)
step_size = 0.125
function_values = np.array([0.000000, 0.021470, 0.293050, 0.494105, 0.541341, 0.516855, 0.468617, 0.416531, 0.367879])

def TrapezoidMethod(step, values):
    values_sum = sum(values)
    first_and_last_avg = (values[0] + values[-1]) / 2
    result = (values_sum - first_and_last_avg) * step
    return result

def SimpsonMethod(step, values):
    odd_sum = 0
    even_sum = 0
    for i in range(1, len(values) - 1):
        if i % 2 == 0:
            even_sum += values[i]
        else:
            odd_sum += values[i]
    first_term = values[0]
    last_term = values[-1]
    odd_sum = 4 * odd_sum
    even_sum = 2 * even_sum
    result = (first_term + odd_sum + even_sum + last_term) * step / 3
    return result

def richardson_extrapolation(raw_integration, st):
    return raw_integration(step_size, function_values) + (raw_integration(step_size, function_values) - raw_integration(step_size * 2, function_values[::2])) / (2 ** st - 1)

print('\n****************************************************')
print('******* Результаты численного интегрирования *******')
print('****************************************************')
print('* Метод трапеций:             ', TrapezoidMethod(step_size, function_values), '*')
print('* Ричардсон (метод трапеций): ', richardson_extrapolation(TrapezoidMethod, 2), ' *')
print('* Метод Симпсона:             ', SimpsonMethod(step_size, function_values), '*')
print('* Ричардсон (метод Симпсона): ', richardson_extrapolation(SimpsonMethod, 4), ' *')
print('* Реальное значение (wolfram): 0.3678794411714423  *')
print('****************************************************\n')
