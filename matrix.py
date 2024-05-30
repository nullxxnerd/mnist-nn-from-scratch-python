import random
from math import sqrt
class Matrix:
    def __init__(self,rows,cols) -> None:
        self.entries = [[0.0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
    def matrixFill(self,n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.entries[i][j] = n
                
    def __str__(self):
        result = []
        for row in self.entries:
            result.append(' '.join(map(str, row)))
        return '\n'.join(result)
    
    def save(self, file_string):
        try:
            with open(file_string, 'w') as file:
                file.write(f"{self.rows}\n")
                file.write(f"{self.cols}\n")
                for row in self.entries:
                    for value in row:
                        file.write(f"{value:.6f}\n")
            print(f"Successfully saved matrix to {file_string}")
        except IOError as e:
            print(f"An error occurred while saving the matrix to {file_string}: {e}")
    def __getitem__(self, idx):
        return self.entries[idx]

    def __setitem__(self, idx, value):
        self.entries[idx] = value

    @classmethod
    def load(cls, file_string):
        try:
            with open(file_string, 'r') as file:
                rows = int(file.readline().strip())
                cols = int(file.readline().strip())
                matrix = cls(rows, cols)
                for i in range(rows):
                    for j in range(cols):
                        matrix.entries[i][j] = float(file.readline().strip())
            print(f"Successfully loaded matrix from {file_string}")
            return matrix
        except IOError as e:
            print(f"An error occurred while loading the matrix from {file_string}: {e}")
            return None
    def Randomize(self, n):
        if n <= 0:
            raise ValueError("Parameter n must be greater than 0")
        min_val = -1.0 / sqrt(n)
        max_val = 1.0 / sqrt(n)
        for i in range(self.rows):
            for j in range(self.cols):
                self.entries[i][j] = uniformDistribution(min_val, max_val)
    def Argmax(self):
        max_score = 0;
        max_idx =0
        for i in range(self.rows):
            if(self.entries[i][0]> max_score):
                max_score = self.entries[i][0]
                max_idx = i
        return max_idx            
    def flatten(self, axis):
        if axis not in (0, 1):
            raise ValueError("Argument to flatten must be 0 or 1")
        
        if axis == 0:
            # Flatten to a column vector
            flattened_matrix = Matrix(self.rows * self.cols, 1)
            for i in range(self.rows):
                for j in range(self.cols):
                    flattened_matrix.entries[i * self.cols + j][0] = self.entries[i][j]
        elif axis == 1:
            # Flatten to a row vector
            flattened_matrix = Matrix(1, self.rows * self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    flattened_matrix.entries[0][i * self.cols + j] = self.entries[i][j]
        
        return flattened_matrix    
def uniformDistribution(low, high):
    if low >= high:
        raise ValueError("Low must be less than high")
    
    difference = high - low
    
    scale = 10000
    scaled_difference = int(difference * scale)
   
    if scaled_difference <= 0:
        raise ValueError("Scaled difference must be greater than 0")
    return low + (random.randint(0, scaled_difference - 1) / scale)


