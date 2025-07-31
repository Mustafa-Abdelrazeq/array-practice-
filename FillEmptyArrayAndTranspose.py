import numpy as np

EmpArray = np.empty((4,4))

print(EmpArray)

def FillArray (Array):
    # This Counter has the value will start with
    Counter = 0
    for row in range(Array.shape[0]):
        
        for col in range(Array.shape[1]):
            
            Array[row][col] = Counter+1
            Counter+=1
    return Array

print(FillArray (EmpArray))

SequentialArray = FillArray (EmpArray)


print('--------------------')

# This Function Only working with squared Matrix Like (2,2 or 4,4 )
# The Two Matrix should have same Shape
def TransposeArray (SequentialArray):
    # Create NEw Zeros Array
    ZerosArray = np.zeros((EmpArray.shape))
    
    for row in range(SequentialArray.shape[0]):      # mean for i in range(number of rows)
        for col in range(SequentialArray.shape[1]):  # mean for i in range(number of cols)
            ZerosArray[col][row] = SequentialArray[row][col]
    return ZerosArray
print(TransposeArray (SequentialArray))