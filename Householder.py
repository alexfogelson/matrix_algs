import numpy as np

def Householder(A_init):
    A = np.copy(A_init)
    m,n = A.shape
    rank = min(m,n)
    Vs = np.zeros((m, n))
    for k in range(rank):
        #get the part of A that you want
        A_slice = A[k:m, k:n]
        #want to map the first column of A_slice to unit vector times magnitude
        #that direction is v = ||x||e_1 - x
        e_k = np.zeros(m-k)
        e_k[0] = np.linalg.norm(A_slice[:,0])

        v = e_k - A_slice[:, 0]
        v_norm = np.linalg.norm(v)

        if (v_norm != 0):
            v = v/v_norm
            vp = np.reshape(v, (m-k,1))
            #A_slice = (I - 2vv^T/v_norm^2) A_slice
            A[k:m, k:n] = A_slice - 2*((vp @ vp.T) @ A_slice)
        
            Vs[k:m, k] = v

    Q = np.identity(m)

    indices = [rank-i-1 for i in range(rank)]
    for k in indices:
        vp = np.reshape(Vs[k:m, k], (m-k, 1))
        Q[k:m, k:m] = Q[k:m, k:m] - 2*(vp @ (vp.T) @ Q[k:m, k:m])

    return Q, A