### //////////////////////////////////////
##  piramid numbers using double loop
### //////////////////////////////////////

def make_piramid(N):
	a, b = N, N 
	aux = 0
	for i in range(a):
		for j in range(i):
			print(aux, end=' ')
			aux = aux + 1 
		print()

if __name__ =='__main__':
	## integer value:
	N = 5
	make_piramid( N )
