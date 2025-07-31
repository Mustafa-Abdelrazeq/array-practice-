import numpy as np

array = np.random.randint(1,99 , (3,3))
def  SumRow(array):
    print('Your Array is : \n', array)
    
    for row in range(array.shape[0]) :
        
        Sum = 0
        # chosen this place to empty Sum for each row loop
        for col in range(array.shape[1] ) :
            Sum += array[row][col]
        print(f'sum of row [{row+1}] is : ',Sum)
    print()
SumRow(array)
print('_'*90)



array = np.random.randint(1,99 , (3,3))
def  SumRowAppendList(array):
    l = []
    print('Your Array is : \n', array)
    
    for row in range(array.shape[0]) :
        
        Sum = 0
        # chosen this place to empty Sum for each row loop
        for col in range(array.shape[1] ) :
            Sum += array[row][col]
        print(f'sum of row [{row+1}] is : ',Sum)
        l.append(int(Sum))

    print()
    return l
print(SumRowAppendList(array))
print('_'*90)

