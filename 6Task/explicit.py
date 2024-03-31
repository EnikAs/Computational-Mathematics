import numpy as np
import matplotlib.pyplot as plt

def solveDiffEq(h, startT, endT, initialX, diffFunc, method):
    assert startT <= endT
    assert h > 0
    nSteps = int((endT - startT) / h) + 1
    tVals = np.linspace(startT, endT, nSteps)
    xVals = np.zeros((nSteps, np.shape(initialX)[0]))
    for i in range(np.shape(initialX)[0]):
        xVals[0][i] = initialX[i]
    return method(h, tVals, xVals, diffFunc)

def adams(stepSize, timeVals, stateVals, diffFunc):
    nSteps = np.shape(stateVals)[0]
    fVals = np.zeros((nSteps, np.shape(stateVals[0])[0]))
    fVals[0] = diffFunc(timeVals[0], stateVals[0])
    stateVals[1] = stateVals[0] + stepSize * fVals[0]
    fVals[1] = diffFunc(timeVals[1], stateVals[1])
    stateVals[2] = stateVals[1] + stepSize * fVals[1]
    fVals[2] = diffFunc(timeVals[2], stateVals[2])
    for j in range(3, np.shape(timeVals)[0]):
        stateVals[j] = stateVals[j - 1] + stepSize * (23 / 12 * fVals[j - 1] - 16 / 12 * fVals[j - 2] + 5 / 12 * fVals[j - 3])
        fVals[j] = diffFunc(timeVals[j], stateVals[j])
    return timeVals, stateVals

def euler(stepSize, timeVals, stateVals, diffFunc):
    for j in range(1, np.shape(timeVals)[0]):
        k1 = diffFunc(timeVals[j - 1], stateVals[j - 1])
        stateVals[j] = stateVals[j - 1] + stepSize * k1
    return timeVals, stateVals

def rk4(stepSize, timeVals, stateVals, diffFunc):
    for j in range(1, np.shape(timeVals)[0]):
        k1 = diffFunc(timeVals[j - 1], stateVals[j - 1])
        k2 = diffFunc(timeVals[j - 1] + 0.5 * stepSize, stateVals[j - 1] + 0.5 * stepSize * k1)
        k3 = diffFunc(timeVals[j - 1] + 0.5 * stepSize, stateVals[j - 1] + 0.5 * stepSize * k2)
        k4 = diffFunc(timeVals[j - 1] + stepSize, stateVals[j - 1] + stepSize * k3)
        stateVals[j] = stateVals[j - 1] + stepSize * (1 / 6 * k1 + 2 / 6 * k2 + 2 / 6 * k3 + 1 / 6 * k4)
    return timeVals, stateVals

def getDiffEqFunc(AVal, BVal):
    return lambda t, stateVals: np.array(
        [AVal + stateVals[1] * stateVals[0] ** 2 - (BVal + 1) * stateVals[1], 
         BVal * stateVals[0] - stateVals[1] * stateVals[0] ** 2])

for bVal in range(2, 6):
    diffEq = getDiffEqFunc(1, bVal)
    step = 0.001
    
    for methodName, methodFunc, color in [("Euler (1 Order)", euler, "darkred"),
                                     ("RK4 (4 Order)", rk4, "lawngreen"),
                                     ("Adams Bashforth(3 Order)", adams, "teal")]:
        timeSteps, solutionVector = solveDiffEq(step, 0, 100, np.array([1, 1]), 
                                                diffEq, methodFunc)
        x1Vals = np.array([solutionVector[i][0] for i in range(np.shape(solutionVector)[0])])
        x2Vals = np.array([solutionVector[i][1] for i in range(np.shape(solutionVector)[0])])
        plt.plot(x1Vals, x2Vals, c=color, label=methodName)
    plt.grid(True)
    plt.legend()
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title(f'B = {bVal}\nStep size = {step}')
    plt.savefig("img/" + f'Bval{bVal}')
    plt.close()
    #plt.show()