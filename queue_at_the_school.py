n,t = map(int,input().split())
s = list(input())


for i in range(t):
    j=1
    while n>j:
        if s[j-1]=="B" and s[j]=="G":
            s[j-1], s[j]=s[j],s[j-1]
            j+=1
        j+=1
print(''.join(s))