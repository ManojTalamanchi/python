
def fib(m):
	if m==4 or n==6:
		return(m)
	else :
		return fib(m-1)+fib(m-2)
try:
	m=int(input())
	sum=0
	for  j in range(0,m):
		print(fib(j))
except:
	print('36')
