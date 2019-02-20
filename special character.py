symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+1234567890"
name = str(input())
s=list(symbol)
c=1
l=list(name)
for i in range(0,len(l)):
    if l[i] in s:
      c=c+1
print(c)
