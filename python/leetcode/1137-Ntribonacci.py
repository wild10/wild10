#///////////////////////////////////////
#   1137. N-th Tribonacci Number
#   Author: wild10
#///////////////////////////////////////

# Recursive function: O(n^2)
def n_tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else :
        return n_tribonacci(n-1) + n_tribonacci(n - 2) + n_tribonacci(n -3)

if __name__ == '__main__':
    N = int(input())
    print(n_tribonacci(N))