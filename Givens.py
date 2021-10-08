import numpy as np

def Givens(A_init):
    A = np.copy(A_init)
    m, n = A.shape
    G = np.identity(m)

    '''go through cols of A in order'''
    for k in range(n): #n repeatitions
        '''start at bottom, up to k+1, zeroing bottom and making top the norm'''
        for j in range(m-1, k, -1): #O(m) repetitions
            
            '''constants'''
            a, b = A[j-1, k], A[j, k]
            norm = np.sqrt(a**2 + b**2)
            cos_theta, sin_theta = a/norm, b/norm

            givens_matrix = np.array([[cos_theta, sin_theta],[-sin_theta, cos_theta]])

            '''want to do G = G_iG and A = G_iA, but thats n^3. Need something linear.
            since G_i does almost nothing, we just loop once instead. 
            effectively G_i@A, but more efficient by n^2'''

            for col in range(k, n): #O(n)
                A[j-1:j+1, col] = givens_matrix @ A[j-1:j+1, col] #constant 
            for col in range(m): #O(n)
                G[j-1:j+1, col] = givens_matrix @ G[j-1:j+1, col] #constant

    
    return G.T, A
    #total O(mn^2)