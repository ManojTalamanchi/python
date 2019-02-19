n=int(input())
l=[int(x) for x in input().split()]
if(len(l)==n):
  for i in range(0,n):
    print(l[i],' ',i)
