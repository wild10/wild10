#///////////////////////////////////////
#   509. Fibonacci Numbers
#   author: wild10
#///////////////////////////////////////

## writing the fuction fib recursive
def Fib(n):
    # base 
    if n <= 1: 
        return n 
    else:
        # recursive
        return Fib(n - 1) + Fib(n - 2)

# main call for functions: good practice

if __name__ =='__main__':
    # defin input
    N = int( input() )
    result = Fib( N )
    # print the result
    print(result)