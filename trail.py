def print_matrix(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            print(mat[i][j],end=" ")
        print()

def matrix_product(p):
    length = len(p)
    # len(p) = number of matrices + 1
 
    # m[i][j] is the minimum number of multiplications needed to compute the
    # product of matrices A(i), A(i+1), ..., A(j)
    # s[i][j] is the matrix after which the product is split in the minimum
    # number of multiplications needed
    # m = [[-1]*length for _ in range(length)]
    # s = [[-1]*length for _ in range(length)]
    m = [([-1]*length) for _ in range(length)]
    s = [([-1]*length) for _ in range(length)]
 
    matrix_product_helper(p, 1, length - 1, m, s)
 
    return m, s
 
 
def matrix_product_helper(p, start, end, m, s):
    if m[start][end] >= 0:
        return m[start][end]
 
    if start == end:
        q = 0
    else:
        q = float('inf')
        for k in range(start, end):
            temp = matrix_product_helper(p, start, k, m, s) + matrix_product_helper(p, k + 1, end, m, s) + p[start - 1]*p[k]*p[end]
            if q > temp:
                q = temp
                s[start][end] = k
 
    m[start][end] = q
    # Return minimum number of scalar multiplications needed to compute from start to end
    return q

def print_parenthesis(s,start,end):
    if(start == end):
        print(chr(65+end-1),end="")
        return

    k = s[start][end]

    print('(',end="")
    print_parenthesis(s,start,k)
    print_parenthesis(s,k+1,end)
    print(')',end="")

if __name__ == "__main__":
    # n = int(input('Enter number of matrices: '))
    p = list(map(int, input("Enter the dimensions of the matrices : ").split()))
    n = len(p) - 1
    m, s = matrix_product(p)
    print_matrix(m)
    print()
    print('The minimum number of scalar multiplications needed : ', m[1][n])
    print('Optimal parenthesize is : ', end='')
    print_parenthesis(s,1,n)

