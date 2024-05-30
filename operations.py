from matrix import *

def checkDimensions(m1,m2):
    if(m1.rows == m2.rows and m1.cols == m2.cols):
        return True
    return False

def matrixMultiply(m1 :Matrix,m2: Matrix):
    if(checkDimensions(m1,m2)):
        m = Matrix(m1.rows,m1.cols)
        for i in range(m1.rows):
            for j in range(m2.cols):
                m.entries[i][j] = m1.entries[i][j] * m2.entries[i][j]
        return m
    else:
        print(f"Dimensions mistmatch multiply: {m1.rows}x{m1.cols}\t{m2.rows}x{m2.cols}")
        print("ERRORR")

def matrixAdd(m1,m2):
    if(checkDimensions(m1,m2)):
        m = Matrix(m1.rows,m1.cols)
        for i in range(m1.rows):
            for j in range(m2.cols):
                m.entries[i][j] = m1.entries[i][j] + m2.entries[i][j]
        return m
    else:
        print(f"Dimensions mistmatch multiply: {m1.rows}x{m1.cols}\t{m2.rows}x{m2.cols}")
        print("ERRORR")
        
def matrixSubtract(m1,m2):
    if(checkDimensions(m1,m2)):
        m = Matrix(m1.rows,m1.cols)
        for i in range(m1.rows):
            for j in range(m2.cols):
                m.entries[i][j] = m1.entries[i][j] - m2.entries[i][j]
        return m
    else:
        print(f"Dimensions mistmatch multiply: {m1.rows}x{m1.cols}\t{m2.rows}x{m2.cols}")
        print("ERRORR")
    
def matrixApply( func,m:Matrix,):
    applied_matrix = Matrix(m.rows, m.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            applied_matrix.entries[i][j] = func(m.entries[i][j])
    return applied_matrix

def matrixDot(m1, m2):
    if m1.cols != m2.rows:
        raise ValueError(f"Dimension mismatch for dot product: {m1.rows}x{m1.cols} and {m2.rows}x{m2.cols}")
    
    result = Matrix(m1.rows, m2.cols)
    for i in range(m1.rows):
        for j in range(m2.cols):
            result.entries[i][j] = sum(m1.entries[i][k] * m2.entries[k][j] for k in range(m1.cols))
    return result

def matrixScale(n, m):
    scaled_matrix = Matrix(m.rows, m.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            scaled_matrix.entries[i][j] = m.entries[i][j] * n
    return scaled_matrix

def matrixAddScalar(n, m):
    added_matrix = Matrix(m.rows, m.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            added_matrix.entries[i][j] = m.entries[i][j] + n
    return added_matrix

def matrixTranspose(m):
    transposed_matrix = Matrix(m.cols, m.rows)
    for i in range(m.rows):
        for j in range(m.cols):
            transposed_matrix.entries[j][i] = m.entries[i][j]
    return transposed_matrix
