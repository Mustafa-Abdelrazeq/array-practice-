import numpy as np

# Shape Must be unification to complet Multiply 
Shape = (3,3)

F_Matrix = np.random.randint(1,5, Shape)
print(f'First Matrix is :\n{F_Matrix}')
# print('-'*20)
S_Matrix = np.random.randint(1,10, Shape)
print(f'Second Matrix is :\n{S_Matrix}')

print('-'*20)
def Multiply2Arrays ():
    # Create Empty Array has same Shape To Save Result in
    EmpArray = np.empty(Shape)
    # Because Of All Arrays Have Same Shape We Can Choose any One of Them to using The Shape Range 
    # We Can Choose Any Array [F_Matrix , S_Matrix , EmpArray] All Will Working 
    for row in range(F_Matrix.shape[0]):
        for col in range (F_Matrix.shape[1]):
            EmpArray[row][col] = (F_Matrix[row][col] * S_Matrix[row][col])
    return EmpArray
print(Multiply2Arrays ())
