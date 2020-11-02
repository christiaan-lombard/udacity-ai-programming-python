# Linear Algebra


## Symbols

 - Vector: $\vec{x}$
 - Magnitude: $\begin{Vmatrix} \end{Vmatrix}$

## Vectors

A vector is an ordered list of numbers.

$\vec{a} = \begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ \ldots \\ a_n \end{bmatrix}$

$\vec{a} \in \mathbb{R}^n$

- Each element in the vector, also called component or coordinate, is a number, denoted here by $a_i$.
- This specific vector has $n$ elements and can be in the field of Real Numbers $\mathbb{R}$.
- A vector of $n$ real elements defines an $n$ dimensional vector and belongs to $\mathbb{R}^n$

### Vector addition:

$\begin{bmatrix} x_1 \\ y_1 \end{bmatrix} + \begin{bmatrix} x_2 \\ y_2 \end{bmatrix} = \begin{bmatrix} x_1 + x_2 \\ y_1 + y_2 \end{bmatrix}$

### Vector magnitude:

$\vec{a} = \begin{bmatrix} x_1 \\ y_1 \end{bmatrix}$

$\begin{Vmatrix}\vec{a}\end{Vmatrix} = \sqrt{x_1^2 + y_1^2}$


### Linear Combinations

The **basis** of a vector space is a set of **linearly independent** vectors that **span** the full space.

Definition of a linear combination is a multiplication of a scalar to a variable and addition of those terms:

If $x$, $y$ and $z$ are vectors, and $a_1$, $a_2$ and $a_3$ are scalars, the following equations will be a linear combination:

$\vec{v} = a_1 \vec{x} + a_2 \vec{y} + a_3 \vec{z}$

If $\vec{v_1}, \vec{v_2}, ..., \vec{v_n} \in \mathbb{R}$ then the **Span** of those vectors (also referred to as the Linear Span) is the set of all possible linear combinations of those vectors: $Sp(\vec{v_1}, \vec{v_2}, \vec{v_n})$



## Matrix

- A Matrix is a two dimensional array that contains the same elements as the vector.
- A Matrix can have $m$ rows and $n$ columns.
- If a Matrix has $m$ rows and $n$ columns is it called an $m \times n$ matrix.


$A = \begin{bmatrix} a_11 & a_12 & a_13 & ... & a_1n \\ a_21 & a_22 & a_23 & ... & a_2n \\ a_31 & a_32 & a_33 & ... & a_3n \\ ... & ... & ... & ... & ... \\ a_m1 & a_m2 & a_m3 & ... & a_mn \end{bmatrix}$

### Matrix Addition

To add one matrix to the other we need to:

- Verify that the matrices are of the **same dimensions**
- Make sure we add elements in the correct corresponding index.

$$
A + B =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & ... & a_{1n} \\
a_{21} & a_{22} & a_{23} & ... & a_{2n} \\
a_{31} & a_{32} & a_{33} & ... & a_{3n} \\
... & ... & ... & ... & ... \\
a_{m1} & a_{m2} & a_{m3} & ... & a_{mn}
\end{bmatrix} +
\begin{bmatrix}
b_{11} & b_{12} & b_{13} & ... & b_{1n} \\
b_{21} & b_{22} & b_{23} & ... & b_{2n} \\
b_{31} & b_{32} & b_{33} & ... & b_{3n} \\
... & ... & ... & ... & ... \\
b_{m1} & b_{m2} & b_{m3} & ... & b_{mn}
\end{bmatrix}

$$

$$
A + B =
\begin{bmatrix}
a_{11} + b_{11} & a_{12} + b_{12} & a_{13} + b_{13} & ... & a_{1n} + b_{1n} \\
a_{21} + b_{21} & a_{22} + b_{22} & a_{23} + b_{23} & ... & a_{2n} + b_{2n} \\
a_{31} + b_{31} & a_{32} + b_{32} & a_{33} + b_{33} & ... & a_{3n} + b_{3n} \\
... & ... & ... & ... & ... \\
a_{m1} + b_{m1} & a_{m2} + b_{m2} & a_{m3} + b_{m3} & ... & a_{mn} + b_{mn}
\end{bmatrix}
$$

### Matrix Scalar Multiplication

$$
\alpha A =
\begin{bmatrix}
\alpha a_{11} & \alpha a_{12} & \alpha a_{13} & ... & \alpha a_{1n} \\
\alpha a_{21} & \alpha a_{22} & \alpha a_{23} & ... & \alpha a_{2n} \\
\alpha a_{31} & \alpha a_{32} & \alpha a_{33} & ... & \alpha a_{3n} \\
... & ... & ... & ... & ... \\
\alpha a_{m1} & \alpha a_{m2} & \alpha a_{m3} & ... & \alpha a_{mn}
\end{bmatrix}
$$

### Square Matrix Multiplication

- When multiplying 2 matrices we need to consider the dimensions of each, as multiplication is not possible if the dimensions are not aligned appropriately.
- The easiest multiplication to consider is that of two **square matrices** of the same dimensions $n \times n$.
- A square matrix is a matrix that has the same number of rows and columns.

$$
P =
\begin{bmatrix}
p_{11} & p_{12} & p_{13} \\
p_{21} & p_{22} & p_{23} \\
p_{31} & p_{32} & p_{33}
\end{bmatrix}

Q =
\begin{bmatrix}
q_{11} & q_{12} & q_{13} \\
q_{21} & q_{22} & q_{23} \\
q_{31} & q_{32} & q_{33}
\end{bmatrix}
$$

$$
P =
\begin{bmatrix}
p_{11}q_{11} + p_{12}q_{21} + p_{13}q_{31} && p_{11}q_{12} + p_{12}q_{22} + p_{13}q_{32} && p_{11}q_{13} + p_{12}q_{23} + p_{13}q_{33} \\
p_{21}q_{11} + p_{22}q_{21} + p_{23}q_{31} && p_{21}q_{12} + p_{22}q_{22} + p_{23}q_{32} && p_{21}q_{13} + p_{22}q_{23} + p_{23}q_{33} \\
p_{31}q_{11} + p_{32}q_{21} + p_{33}q_{31} && p_{31}q_{12} + p_{32}q_{12} + p_{33}q_{32} && p_{31}q_{13} + p_{32}q_{23} + p_{33}q_{33}
\end{bmatrix}
$$

Each element $ij$ in $P \times Q$ is a result of multiplying all elements in row $i$ of matrix $P$ with the corresponding $j$ elements in column $j$ of matrix $Q$.

## Matrix Multiplication

If $P$ is a matrix with dimensions $t \times m$ and $Q$ is a matrix with dimensions $m \times v$ then:

- $P \times Q$ is possible as the dimensions match. ($P$ has $m$ columns and $Q$ has $m$ rows).
- $P \times Q$ will be a matrix of $t \times v$. ($t$ rows and $v$ columns).

$$
P =
\begin{bmatrix}
p_{11} & p_{12} & p_{13} \\
p_{21} & p_{22} & p_{23}
\end{bmatrix}

Q =
\begin{bmatrix}
q_{11} & q_{12} & q_{13} & q_{14} \\
q_{21} & q_{22} & q_{23} & q_{24} \\
q_{31} & q_{32} & q_{33} & q_{34}
\end{bmatrix}
$$

$$
P \times Q=
\begin{bmatrix}
p_{11}q_{11}+p_{12}q_{21}+p_{13}q_{31} & p_{11}q_{12}+p_{12}q_{22} + p_{13}q_{32} & p_{11}q_{13}+p_{12}q_{23}+p_{13}q_{33} &p_{11}q_{14}+p_{12}q_{24}+p_{13}q_{34} \\
p_{21}q_{11}+p_{22}q_{21}+p_{23}q_{31} &p_{21}q_{12}+p_{22}q_{22}+p_{23}q_{32} &p_{21}q_{13}+p_{22}q_{23}+p_{23}q_{33}&p_{21}q_{14}+p_{22}q_{24}+p_{23}q_{34}
\end{bmatrix}

$$
