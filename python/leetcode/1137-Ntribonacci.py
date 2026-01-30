#///////////////////////////////////////
#   1137. N-th Tribonacci Number
#   Author: wild10
#///////////////////////////////////////

memo = {}
# usind memo DP approach  : O(n)
def dp_tribonacci(n):
    if n == 0:
        return 0:
    if n == 1 or n == 2:
        return 1
    # if n already i memo -> return value
    if n in memo:
        return memo[n]
    #else calculate new value and return 
    memo[n] = dp_tribonacci(n-1) + dp_tribonacci(n-2) + dp_tribonacci(n-3)
    return memo[n]
    
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