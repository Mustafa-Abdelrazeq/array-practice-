# 1- Sum All Element Of Array 

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
print('----------------------------------')
# ------------------------------------------------------------------------
# 2- Check To Two Matrices If Sum Equals Each Others 
    # Count How Many times Taked To Get The Same Sum of Two Matrices

def HowManyTimesToSeeSameResults():
    Times = 0
    while True:
        Array_1 = np.random.randint(1,5 , (3,5))
        Array_2 = np.random.randint(1,5 , (3,2))
        
        if SumAllElementOfArray(Array_1) == SumAllElementOfArray(Array_2):
            print(Array_1)
            print()
            print(Array_2)
            print()
            print(f'The Sum Of Each Matrix is : [{SumAllElementOfArray(Array_1)}]')
            return f'[{Times}] Times.'

        Times+=1
print(HowManyTimesToSeeSameResults())