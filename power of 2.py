def main():
	try:
		g=0
		b=int(input())
		while(b!=0):
			b=b/2
			if b==1:
				g=1
				break
		if g!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
