import random

class Matrix:

    def __init__(self, row, collumn) -> None:
        self.row = row
        self.collumn = collumn
    
    def createMatrix(self):
        return [[random.randint(0, 1000) for i in range(self.collumn)] for j in range(self.row)]
    
    @classmethod
    def addMatrix(cls, matrixA, matrixB):
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
    
    @staticmethod
    def substactMatrix(matrixA, matrixB):
        if len(matrix1) != len(matrixB):
            return "matrix should have equal row and collumn"
        
        new = []

        for i in range(len(matrixA)):
            new_row = []
            for j in range(len(matrixA[i])):
                sum = matrixA[i][j] - matrixB[i][j]
                new_row.append(sum)
            new.append(new_row)

        return new
    
    @property
    def transpose(self, matrix):
        new = []
        for i in range(len(matrix)):
            new_mat = []
            for j in range(len(matrix[i])):
                new_mat.append(matrix[j][i])
            new.append(new_mat)
        return new
    # def status(self):
    #     return f"this matrix has row {self.row} and column {self.column}"

m = Matrix(2,3)
print("matrix:")
matrix1 = m.createMatrix()
matrix2 = m.createMatrix()

print(matrix1)
print(matrix2)
print()

print("ADDING")
sum = Matrix.addMatrix(matrix1,matrix2)
print(sum)
print()

print("SUBSTRACT")
sub = Matrix.substactMatrix(matrix1, matrix2)
print(sub)

print()
print("TANSPOSE")
print(f"transpose of matrix1 is {m.transpose(Matrix, ma)}")