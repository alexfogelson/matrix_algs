from *

from Householder import *
from Givens import *
from MGS import *

def solve(A, b, mode='MGS'):
    #Rx = Q.Tb
    mode = mode.lower()
    if (mode == 'mgs'):
        Q, R = MGS(A)
    elif ('house' in mode):
        Q, R = Householder(A)
    elif ('given' in mode):
        Q, R = Givens(A)    

    bp = Q.T@b
    m,n = R.shape
    vars = min(m,n)
    solution = np.zeros(vars)
    for i_ in range(vars):
        i = vars-i_-1
        if (R[i,i] == 0):
            solution[i] = 1
        else:
            solution[i] = (bp[i] - np.dot(R[i,:], solution))/(R[i,i])

    return np.reshape(solution, (vars, 1))

def check_upper(A):
    m, n = A.shape
    for i in range(m):
        for j in range(n):
            if (i > j and not(np.isclose(A[i,j], 0))):
                return False

    return True

def test(mode_ = 'mgs'):
    mode = mode_.lower()

    diff_1 = []
    diff_2 = []
    diff_3 = []

    for k in range(1,20):
        loops = 20
        for i in range(0,loops):

            #different sizes
            if (i < loops):
                m, n = k, k
            else:
                m, n = np.random.randint(0, k+1), np.random.randint(k, k+1)


            A = np.random.random((m,n))
            x = np.random.random((n,1))
            b = A@x
            
            if (mode == 'mgs'):
                Q, R = MGS(A)
            elif ('house' in mode):
                Q, R = Householder(A)
            elif ('given' in mode):
                Q, R = Givens(A)

            assert(check_upper(R))

            diff_1.append(np.linalg.norm(Q.T@Q - np.identity(Q.shape[0])))
            diff_2.append(np.linalg.norm(Q@R - A))
            diff_3.append(np.linalg.norm(x - solve(A, b, mode=mode)))

    means = [np.mean(diff_1), np.mean(diff_2), np.mean(diff_3)]
    all_close = np.isclose(means, [0,0,0]).all()

    if (all_close):
        print(f"All tests passed for {mode_}.")
    else:
        print("Tests failed, printing means: ", means)

test('MGS')
test('Household')
test('Givens')