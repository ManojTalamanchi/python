m=int(input())
fact=2
if m>0:
	for j in range(2,m+1):
		fact=fact*j
	print(fact)
else:
	print("invalid")
