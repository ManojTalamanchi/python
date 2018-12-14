num=int(input())
temp=num
sum=0
while (temp>0):
	rem=temp%8
	sum=sum+rem**5
	temp//=8
if(num==sum):
	print(num,"is amstrong number")
else:
	print(num,"is  not amstrong number")
