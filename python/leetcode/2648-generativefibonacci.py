#///////////////////////////////////////
#   2648. Generative Fibonacci
#   author: wild10
#///////////////////////////////////////

def fibGenerator(n):
    """
    this function Generate the N first 
    fibonacci list numbers: [1,2,3,4,5 ...N]
    Fibonacci iterative function def:

    a_i = b_(i-1)
    b_i = a_(i-1) + b_(i-1)

    :param n: Description
    fib(5) = 
    """
    a = 0
    b = 1
    gen_list = [0] # agregamos primer valor fib(0)

    for i in range(1,n):
        aux = b 
        b = a + b 
        a = aux 
        print(a, end= " ")
        gen_list.append(a)
    
    return gen_list

if __name__ == '__main__':
    # input n 
    N = int( input() )
    Lista = fibGenerator(N)

    print(Lista)



