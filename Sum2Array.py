import numpy as np
from PerfectNumber import UserInput
num = UserInput('Enter How Many Numbers is 2 Random Arrays : ')
RandomList1 = np.random.randint(1,99 , num)
RandomList2 = np.random.randint(1,99 , num)
print(RandomList1)
print(RandomList2)
print('-------------------------')
def SumTwoArrays (arr1,arr2):
    NewArray = np.zeros((num))
    for i in range(len(arr1)):
        NewArray[i] = ( arr1[i] + arr2[i])
    return NewArray

# print(SumTwoArrays (RandomList1,RandomList2))