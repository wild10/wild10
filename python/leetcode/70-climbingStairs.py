#///////////////////////////////////////
#   70. Climbing Stairs
#   Author: wild10
#///////////////////////////////////////

memo = {}
# simple function recursive: O(n^2)
def climb (n):
    if n==1 or n==2:
        return n 
    else :
        return climb (n-1) + climb (n-2)


# function using memoization O(n)
def climb2 (n):
    if n <= 2:
        return n 
    # check memo
    if n in memo:
        return memo[n]
    
    memo[n] = climb2 (n - 1) + climb2 (n - 2)
    return memo[n]

# main
if __name__=='__main__':
    N = int(input())

    print(climb2 (N))