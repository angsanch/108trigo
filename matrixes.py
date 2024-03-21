##
## EPITECH PROJECT, 2023
## matrixes.py
## File description:
## manage matrixes
##

class Matrix:
    matrix:list
    width:int
    height:int
    def __init__(self, width, height, numbers):
        if type(width) != int or type(height) != int or type(numbers) != list:
            raise TypeError("Error, invalid type for dimensions")
        if width * height != len(numbers):
            raise ValueError("Invalid amount of numbers")
        try:
            numbers = [float(i) for i in numbers]
        except ValueError:
            raise TypeError("Invalid numbers inputted")
        self.width = width
        self.height = height
        self.matrix = []
        for i in range(height):
            self.matrix.append(numbers[width * i:width * (i + 1)])

    def _check_matrix(matrix):
        if not isinstance(matrix, Matrix):
            raise TypeError("A matrix is needed")

    def _check_square(matrix):
        Matrix._check_matrix(matrix)
        if matrix.width != matrix.height:
            raise ValueError("Matrixes must be square")

    def _check_same_size(self, matrix):
       if self.width != matrix.width or self.height != matrix.height:
            raise ValueError("Matrixes must be the same size")

    def _check_mul_compatible(self, matrix):
        if self.width != matrix.height:
            raise ValueError("Incompatible matrix sizes")

    def _det(matrix):
        Matrix._check_square(matrix)
        if matrix.width == 1:
            return matrix.matrix[0][0]
        elif matrix.width == 2:
            return (matrix.matrix[0][0] * matrix.matrix[1][1]) - \
                (matrix.matrix[0][1] * matrix.matrix[1][0])
        det = 0
        for x in range(matrix.width):
                det += Matrix(matrix.width - 1, matrix.height - 1,
                    row_col_delete(matrix.matrix, x, 0)).det() * \
                    ((-1) ** x) * matrix.matrix[0][x]
        return det

    def det(self):
        return (Matrix._det(self))

    def adj(self):
        if self.width == 1 and self.height == 1:
            return self
        numbers = []
        for y in range(self.height):
            for x in range(self.width):
                numbers.append(Matrix(self.width - 1, self.height - 1,
                    row_col_delete(self.matrix, x, y)).det() * \
                        ((-1) ** (x + y)))
        return Matrix(self.width, self.height, numbers).trans()

    def trans(self):
        numbers = []
        for i in range(self.height):
            for j in range(self.width):
                numbers.append(self.matrix[j][i])
        return Matrix(self.height, self.width, numbers)

    def inverse(self):
        if self.width == 1 and self.height == 1:
            return (Matrix(1, 1, [1 / self.matrix[0][0]]))
        return self.adj().trans() / self.det()

    def to_list(self):
        result = []
        for i in self.matrix:
            result += [round(j, 0) for j in i]
        return result

    def __add__(self, this):
        Matrix._check_matrix(this)
        self._check_same_size(this)
        result = []
        for i in range(self.height):
            result += [self.matrix[i][j] + this.matrix[i][j]
                for j in range(self.width)]
        return Matrix(self.width, self.height, result)

    def __sub__(self, this):
        Matrix._check_matrix(this)
        self._check_same_size(this)
        result = []
        for i in range(self.height):
            result += [self.matrix[i][j] - this.matrix[i][j]
                for j in range(self.width)]
        return Matrix(self.width, self.height, result)

    def __mul__(self, this):
        Matrix._check_matrix(this)
        self._check_mul_compatible(this)
        result = []
        for i in range(self.height):
            for j in range(this.width):
                result.append(combine_lists(self.matrix[i],
                    [k[j] for k in this.matrix]))
        return Matrix(self.height, this.width, result)

    def __truediv__(self, this):
        if isinstance(this, Matrix):
            return self * this.inverse()
        elif not (isinstance(this, int) or isinstance(this, float)):
            raise TypeError("A matrix, a float or an int is needed")
        result = []
        for i in range(self.height):
            for j in range(self.width):
                result.append(self.matrix[j][i] / this)
        return Matrix(self.width, self.height, result)

    def __str__(self):
        lines = ["\t".join([f"{int(j):d}" for j in i])
            for i in self.matrix]
        return "\n".join(lines)


def matrix_print_asf(m):
    lines = ["\t".join([f"{j}" for j in i])
        for i in m.matrix]
    return "\n".join(lines)

def combine_lists(l1, l2):
    if len(l1) != len(l2):
        raise IndexError("Lists need to be the same size")
    result = 0
    for i in range(len(l1)):
        result += l1[i] * l2[i]
    return result

def row_col_delete(matrix, x, y):
    result = []
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if x != i and y != j:
                result.append(matrix[j][i])
    return result

if __name__ == "__main__":
    print(Matrix(2, 2, [1, 2, 3, 4]).adj())
