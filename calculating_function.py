n = int(input())

if n%2==0:
    ans = n//2
if n%2==1:
    ans = ((n-1)//2)-n
    
print(ans)