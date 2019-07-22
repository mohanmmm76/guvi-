m,k=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
A=0
NUM=0
while k>0:
  NUM+=arr[A]
  k=k-1
  A=A+1
print(NUM)
