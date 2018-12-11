x=int(input())
for j in range(4,x):
	if (x%j==0):
		print(x," is not a prime number")
		break
	else:
		print(x," is prime number")
		break
