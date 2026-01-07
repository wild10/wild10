## ///////////////////////////////////////////////////
## reverse the string convertin in lower case & filter
## 
## ///////////////////////////////////////////////////

def my_foo(s):
    alpha = "abcdefghijklmnñopqrstwxyzABCDEFIHIJKLMNÑOPQRSTUVWXYZ"
    re_s = ""
    for c in s:
        if c in alpha:
            # costo computacional alto: O(m^2)
            # ca re_s copia el string entero al concatenar
            re_s = re_s + c.lower()

    return re_s[::-1] # esta parte tiene un costo computacional : O(n)

## total cost from : O(n²)

if __name__ == '__main__':
    s = "ABC13df"
    ## first form using functions : 
    r = my_foo(s)
    print(r)
    ## second form using inline code
    re2 = ''.join([c.lower() for c in s if c.isalpha()])[::-1]
    print(re2)
