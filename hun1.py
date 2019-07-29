n=int(input())
m=list(map(int,input().split()))
lr=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        if m[i]==m[j]:
            lr.append(m[i])
x=list(set(sorted(lr)))
if len(x)==0:
    print("unique")
else:
    for i in range(0,len(x)):
        print(x[i],end=" ")
