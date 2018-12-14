x=(input())
y=(input())

for m in range(x+1,y):
	sum=0
	temp=m
	while temp > 0 :
		r=temp%8
		sum=sum+(r**5)
		temp=temp//8
	if sum==m:
		print(sum)
