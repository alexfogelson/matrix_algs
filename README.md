# Matrices are cool
Matrices are really, really cool. Cool enough that most silicon manufacturers have put hundreds of millions into designing chips just for matrix multiplications (normally with fancy names like **Neural Engines**). Cool enough that many supercomputers are judged on how quickly they can run matrix operations. Matrices are really, really cool.

## Matrix algorithms are deceiving

Hey, you want an orthonormal basis for a vector space? Use Graham-Schmidt, right? Wrong. Every linear algebra classes flaunts this algorithm likes it's the end-all-be-all orthogonalization algorithm. But alas, finite precision makes this a useless algorithm.

Turns out, this is true for many algorithms. *Canonical algorithms are either really inefficient or unstable in finite precision.*

The algorithms in this library are implementations of stable, efficient algorithms that are vital for matrix algebra.

## Strassen

Matrix multiplication will some day be O(n^2), I hope. But for now, O(n^2.81) will have to do. At least it's better than O(n^3).

## MGS
This is simply modified Graham-Schmidt. Typical Graham Schmidt grabs a vector v, normalizes, and projects onto the space orrthogonal to the span created thus far. Modified Graham-Schmidt projects all the vectors on to this space as we go along, which improves stability and maintains the same efficiency.

## Householders
We aim to factor A = QR, where Q is orthogonal and R is upper triangular. Pick a column v, and find an orthogonal matrix which projects v onto an axis while norm preserving. Applying this to the first column of a matrix makes A' upper triangular in the first column. Doing this iteratively to submatrices gives us upper-triangularity after n iterations (where n is the number of columns). In the end, the product of each such orthogonal matrix is simply Q^T, and R is the final result. O(mn^2).

## Givens Rotations
We aim to factor A = QR, where Q is orthogonal and R is upper triangular. This works identically to Householders, but instead of one projection matrix, we use a series of smaller 2x2 orthogonal rotation matrices known as givens matrices. The asymptotic efficiency is the same. 

