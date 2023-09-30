import math

NUMBER_OF_FUNCS = 5

FUNCS_NAMES = ["sin(x^2)", "cos(sin(x))", "exp(sin(cos(x)))",
               "ln(x+3)", "(x+3)^0,5"]

def f1(x):
    return math.sin(x*x)

def f2(x):
    return math.cos(math.sin(x))

def f3(x):
    return math.exp(math.sin(math.cos(x)))

def f4(x):
    return math.log(x + 3)

def f5(x):
    return math.sqrt(x + 3)