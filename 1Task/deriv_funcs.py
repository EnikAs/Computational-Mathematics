import math

def f1_deriv(x):
    return 2 * x * math.cos(x*x)

def f2_deriv(x):
    return (-1) * math.cos(x) * math.sin(math.sin(x))

def f3_deriv(x):
    return (-1) * math.exp(math.sin(math.cos(x))) * math.sin(x) * math.cos(math.cos(x))

def f4_deriv(x):
    return 1 / (x + 3)

def f5_deriv(x):
    return 1 / (2 * math.sqrt(x + 3))