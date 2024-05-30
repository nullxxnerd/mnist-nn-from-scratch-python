import numpy as np

def sigmoid(input):
    return 1.0 / (1 + np.exp(-input))

def sigmoidPrime(m):
    ones = np.ones_like(m)
    subtracted = ones - m
    multiplied = m * subtracted
    return multiplied

def softmax(m):
    exp_values = np.exp(m - np.max(m))  # Subtract max for numerical stability
    total = np.sum(exp_values)
    return exp_values / total

# Assuming matrix_create and matrix_fill functionalities are replaced by numpy array manipulations:
def matrixCreate(rows, cols):
    return np.zeros((rows, cols))

def matrixFill(matrix, value):
    matrix.fill(value)
    return matrix

# Sample usage with numpy arrays
if __name__ == "__main__":
    m = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
    print("Original Matrix:")
    print(m)

    print("\nSigmoid:")
    print(sigmoid(m))

    print("\nSigmoid Prime:")
    print(sigmoid_prime(sigmoid(m)))

    print("\nSoftmax:")
    print(softmax(m))
