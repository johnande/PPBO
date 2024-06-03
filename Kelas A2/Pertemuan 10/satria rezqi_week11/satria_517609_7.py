from collections import namedtuple
import random

class Matrix(namedtuple('matrix', ['row', 'collumn'])):
    
    def createMatrix(self):
        return [[random.randint(0, 1000) for i in range(self.collumn)] for j in range(self.row)]
    
    def addMatrix(self, matrixA, matrixB):
        if len(matrix1) != len(matrixB):
            return "matrix should have equal row and collumn"
        
        new = []

        for i in range(len(matrixA)):
            new_row = []
            for j in range(len(matrixA[i])):
                sum = matrixA[i][j] + matrixB[i][j]
                new_row.append(sum)
            new.append(new_row)

        return new
    
m1 = Matrix(2,3)
matrix1 = m1.createMatrix()
matrix2 = m1.createMatrix()
sum = m1.addMatrix(matrix1, matrix2)

print(matrix1)
print(matrix2)
print()

print("ADDING")
print(sum)


