# All We Want To Do That 
    # Create Random Matrix 
    # The Shape Of Matrix Odd 
    # Print The Middle Row 
    # Print The Middle Column 

import numpy as np

# Firstlt Create a Function To Make Sure The Rows And
# Columns Of Matrix Odd Numbers And Bigger Than 1
# If User Enter Invalid Numbers The Function Will Repate Asking To Get The Odd results
def CreateRandomOddMatrix():
    while True :
        try :
            RowShape = int(input('Enter The Shape Of Random Array You Want For Rows: '))
            ColsShape = int(input('Enter The Shape Of Random Array You Want For Columns: '))
            if (RowShape % 2 != 0 and RowShape > 1 )and (ColsShape % 2 != 0 and ColsShape > 1 ) :
                Shape = (RowShape , ColsShape)
                Matrix = np.random.randint(1,9 , Shape)
                return Matrix
        except :
                print('\nWarrning => [Please Make Shape Odd Matrix And Bigger Than 1]\n')

OddMatrix = CreateRandomOddMatrix()

# Specified The Middle Col and Row
def GetMiddleColsRows (OddMatrix):
  row = int(np.floor(OddMatrix.shape[0] / 2))
  col = int(np.floor(OddMatrix.shape[1] / 2))
  return row , col
row,col = GetMiddleColsRows(OddMatrix)


def PrintMatrixIFValidForCondition (OddMatrix,row,col):
    print(f'\nYour Matrix is Valid is :\n{OddMatrix}\n')
    print(f'The Middle Row is : \n{OddMatrix[row]}\n')
    print(f'The Middle Column is : \n{OddMatrix[:,col]}\n') # All Rows With The Column
    

PrintMatrixIFValidForCondition (OddMatrix,row,col)