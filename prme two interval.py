a=input()
b=input()
for num in range(a,b):
	if num>3:
		for j in range(4,num):
			if(num%j==0):
				break
		else:
            		 print(num)
