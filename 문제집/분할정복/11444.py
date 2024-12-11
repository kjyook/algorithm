import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

#2x2 행렬 곱할때 쓸 함수
def matrix_mult(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % p, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % p],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % p, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % p]]

def matrix_pow(M, k):
    if k == 1:
        return M
    
    #단위행렬
    result = [[1, 0], [0, 1]]
    base = M

    while k > 0:
        if k % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        k //= 2

    return result

def fibo(a):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    
    basic = [[1, 1], [1, 0]]
    result = matrix_pow(basic, a - 1)

    return result[0][0]

print(fibo(n))