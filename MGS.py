import numpy as np

def MGS(A):
    m, n = A.shape
    R = np.zeros((m,n))
    A = np.copy(A)

    for i in range(n):
        v_i = A[:,i]
        R[i,i] = np.linalg.norm(v_i)
        A[:,i] = A[:,i]/R[i,i]
        for j in range(i+1, n):
            R[i,j] = np.dot(A[:,j], v_i)
            A[:,j] = A[:,j] - (R[i,j]*v_i)
    return A, R