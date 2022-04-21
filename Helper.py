import numpy as np
import math
from time import time


def cpuFactorial(n, iterations):
    arr = np.ones(iterations).astype(np.int32)
    t1 = time()
    for k in range(iterations):  # run "iterations" (# total processes) # of times sequentially to compare against gpu time
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        arr[k] = math.sqrt(fact)
    print('total time to compute on CPU: %fs' % (time() - t1))
    return arr

def checkNumberOfTargetValues(resultingArray, factorialInput):
    numChanged = 0
    correctFactorialValue = np.float32(math.sqrt(math.factorial(factorialInput))) # put through
    for i in resultingArray:
        if (i == correctFactorialValue):
            numChanged += 1
        percentCorrect = int(numChanged/resultingArray.size * 100)
    print("%d percent of the values are correct (equal to %d)" % (percentCorrect, correctFactorialValue))
    # print("The value of outvec_gpu, after computation is:   \n", resultingArray)

# def dictGPCRCreation(angleIncrementValue, numHelices):
    # for i in numHelices:
        # i * angleIncrementValue
