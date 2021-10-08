##### THIS IS STRASSEN FROM SCRATCH #####

#Numpy only included for comparison. It's never used.

def slice_matrix(M, row_s, row_e, col_s, col_e):
    slice = []
    for i in range(row_s, row_e):
        row = []
        for j in range(col_s, col_e):
            row.append(M[i][j])
        slice.append(row)
    return slice

def add(M1, M2):
    if (len(M1) == 0 and len(M2) == 0):
        return []
    if (len(M1) == 0 or len(M2) == 0):
        raise Exception("Invalid dimensions")
    
    m1, n1 = len(M1), len(M1[0])
    m2, n2 = len(M2), len(M2[0])
    
    new_M = []

    if (m1 != m2 or n1 != n2):
        raise Exception("Invalid dimensions")

    for i in range(len(M1)):
        row = []
        for j in range(len(M1[0])):
            row.append(M1[i][j] + M2[i][j])
        new_M.append(row)

    return new_M

def subtract(M1, M2):
    if (len(M1) == 0 and len(M2) == 0):
        return []
    if (len(M1) == 0 or len(M2) == 0):
        raise Exception("Invalid dimensions")
    
    m1, n1 = len(M1), len(M1[0])
    m2, n2 = len(M2), len(M2[0])
    
    new_M = []

    if (m1 != m2 or n1 != n2):
        raise Exception("Invalid dimensions")

    for i in range(len(M1)):
        row = []
        for j in range(len(M1[0])):
            row.append(M1[i][j] - M2[i][j])
        new_M.append(row)

    return new_M

def get_dims(M):
    if (len(M) == 0):
        return 0,0
    return len(M), len(M[0])

def conjoin_matrices(W,X,Y,Z):
    w1, w2 = get_dims(W)
    x1, x2 = get_dims(X)
    y1, y2 = get_dims(Y)
    z1, z2 = get_dims(Z)

    if (w2 != y2 or x2 != z2 or w1 != x1 or y1 != x1):
        raise Exception("Invalid dimensions for conjoin matrices!")
    
    M = []
    for i in range(w1):
        row = []
        for j in range(w2):
            row.append(W[i][j])
        for j in range(x2):
            row.append(X[i][j])
        M.append(row)
    
    for i in range(y1):
        row = []
        for j in range(y2):
            row.append(X[i][j])
        for j in range(z2):
            row.append(Z[i][j])
        M.append(row)
    
    return M

#matrices are given in row major form, list of lists
def StrassenMultiply(M1, M2):
    if (len(M1) == 0 and len(M2) == 0):
        return []
    if (len(M1) == 0 or len(M2) == 0):
        raise Exception("Invalid dimensions")
    
    m1, n1 = len(M1), len(M1[0])
    m2, n2 = len(M2), len(M2[0])

    if (n1 != m2):
        raise Exception("Invalid dimensions")

    if (m1 == 1 and n1 == 1 and m2 == 1 and n2 == 1):
        return [[M1[0][0] * M2[0][0]]]
    


    A = slice_matrix(M1, 0, m1//2, 0, n1//2)
    B = slice_matrix(M1, 0, m1//2, n1//2, n1)
    C = slice_matrix(M1, m1//2, m1, 0, n1//2)
    D = slice_matrix(M1, m1//2, m1, n1//2, n1)

    E = slice_matrix(M2, 0, m2//2, 0, n2//2)
    F = slice_matrix(M2, 0, m2//2, n2//2, n2)
    G = slice_matrix(M2, m2//2, m2, 0, n2//2)
    H = slice_matrix(M2, m2//2, m2, n2//2, n2)

    P1 = StrassenMultiply(add(A, D), add(E,H))
    P2 = StrassenMultiply(add(C, D), E)
    P3 = StrassenMultiply(A, subtract(F,H))
    P4 = StrassenMultiply(D, subtract(G, E))
    P5 = StrassenMultiply(add(A, B), H)
    P6 = StrassenMultiply(subtract(C,A), add(E,F))
    P7 = StrassenMultiply(subtract(B,D), add(G,H))


    W = add(subtract(add(P1, P4), P5), P7)
    X = add(P3 ,P5)
    Y = add(P2, P4)
    Z = add(subtract(add(P1, P3), P2) ,P6)

    return conjoin_matrices(W,X,Y,Z)


import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

runtimes = []

MAX = 7
for n in range(1, MAX):
    start = datetime.now()
    for i in range(10):
        A = np.random.rand(2**n,2**n)
        B = np.random.rand(2**n,2**n)
        
        #numpy_result = (A@B).tolist()
        my_result = StrassenMultiply(A.tolist(), B.tolist())
        #np.isclose(numpy_result, my_result)
    end = datetime.now()

    delta = (end-start).total_seconds()/10
    runtimes.append(np.log(delta))
    print(n)

log_ms = [np.log(2**i) for i in range(1, MAX)]
slope, intercept = np.polyfit(log_ms, runtimes, 1)
print(slope, np.log(7)/np.log(2))
plt.plot(log_ms, runtimes)
plt.show()
