NUMBER_OF_DIFS = 5

LABELS = ["1", "2", "3", "4", "5"]

def dif1(f, x, h):
    return (f(x + h) - f(x))/h

def dif2(f, x, h):
    return (f(x) - f(x - h))/h

def dif3(f, x, h):
    return (f(x + h) - f(x - h))/(2 * h)

def dif4(f, x, h):
    return 4/3 * (f(x + h) - f(x - h))/(2 * h) - 1/3 * (f(x + 2 * h) - f(x - 2 * h))/(4 * h)

def dif5(f, x, h):
    return 3/2 * (f(x + h) - f(x - h))/(2 * h) - 3/5 * (f(x + 2 * h) - f(x - 2 * h))/(4 * h) + 1/10 * (f(x + 3 * h) - f(x - 3 * h))/(6 * h)