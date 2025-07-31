# Sum All Element Of Array 

import numpy as np

Array = np.random.randint(1,5 , (3,2))
print(Array)
def SumAllElementOfArray(Matrix):
    Sum = 0
    for row in range(Matrix.shape[0]):
        for col in range(Matrix.shape[1]):
            Sum += Matrix[row][col]
    return Sum

print(SumAllElementOfArray(Array))
