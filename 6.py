# Design and implement a dynamic programming algorithm for chain matrix multiplication. #

# Function to print the matrix
def print_matrix(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            print(mat[i][j],end=" ")
        print()


# Function to calculate and return m and s matrices
def matrix_product(p):
    # m[i][j] is the minimum number of scalar multiplications needed to compute the
    # product of matrices A(i), A(i + 1), ..., A(j).
 
    # s[i][j] is the index of the matrix after which the product is split in an
    # optimal parenthesization of the matrix product.
 
    # p[0... n] is a list such that matrix A(i) has dimensions p[i - 1] x p[i].
    # len(p) = number of matrices + 1
    length = len(p) 
 
    # m[i][j] is the minimum number of multiplications needed to compute the product of matrices A(i), A(i+1), ..., A(j)

    # s[i][j] is the matrix after which the product is split in the minimum number of multiplications needed

    
    m = [(['-']*length) for _ in range(length)]
    s = [(['-']*length) for _ in range(length)]

    # cost is zero when multiplying one matrix.
    for i in range(1, length):
        m[i][i] = 0
 
    for chain_length in range(2, length):
        for start in range(1, length - chain_length + 1):
            end = start + chain_length - 1
            q = float('inf')
            for k in range(start, end):
                # temp = cost/scalar multiplications
                temp = m[start][k] + m[k + 1][end] + p[start - 1]*p[k]*p[end]
                if temp < q:
                    q = temp
                    s[start][end] = k
            m[start][end] = q
    return m, s
 
# Function to Recursively print the arrangement for minimum cost of multiplication
def print_parenthesization(s, start, end):
    # s[i][j] is the index of the matrix after which the product is split in an
    # optimal parenthesization of the matrix product.

    # If only one matrix left in current segment
    if start == end:
        print(chr(65 + end-1), end = "")
        return
 
    k = s[start][end]
 
    print('(', end='')
    # Recursively put brackets around subexpression from i to k.
    print_parenthesization(s, start, k)
    # Recursively put brackets around subexpression from k + 1 to end.
    print_parenthesization(s, k + 1, end)
    print(')', end='')
 
 
if __name__ == "__main__":
    # Taking input the number of matrices and their orders
    n = int(input('Enter total number of matrices: '))
    p = [] # list to store the dimesnsions of matrix sequentially
    temp_row = int(input('Enter number of rows in matrix {}: '.format(chr(65))))
    temp_col = int(input('Enter number of cols in matrix {}: '.format(chr(65))))
    print()
    p.append(temp_row)
    x = temp_col
    for i in range(1,n):
        temp_row = int(input('Enter number of rows in matrix {}: '.format(chr(65 + i))))
        if(x != temp_row):
            print("(row no of prev matrix != col no of next matrix).... hence, Matrix multiplication not possible")
            exit(0)
        temp_col = int(input('Enter number of cols in matrix {}: '.format(chr(65 + i))))
        print()
        x = temp_col
        # appending the dimesnions sequentially into the list
        if i < n-1:
            p.append(temp_row)
        else:
            p.append(temp_row)
            p.append(temp_col)

    m, s = matrix_product(p)
    # printing matrices m and s
    print_matrix(m)
    print()
    print_matrix(s)
    print()
    print('The number of scalar multiplications needed:', m[1][n])
    print('Optimal parenthesization: ', end='')
    print_parenthesization(s, 1, n)