m,u=map(int,input().split())  
for n in range(m,u):
   s= 0
   t=n
   while t> 0:
       d= t% 10
       s+=d** 3
       t//= 10
 
   if n==s:
       print(n,"",end="")
