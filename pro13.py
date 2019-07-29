m,k=map(int,input().split())
h=(input().split())[0:m]
i=0
while i<k:
  m,n=map(int,input().split())
  i+=1
  print(min(h[m-1:n]))
