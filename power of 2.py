g=0
b=int(input())
while(b>0):
  if b==1:
	  g=1
	  break
  else:
    b=b/2

if g!=1:
	print('no')
else :
	print('yes')
