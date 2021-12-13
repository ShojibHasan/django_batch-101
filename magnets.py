n = int(input())
magnets =[]
count=1
for i in range(n):
    magnets.append(int(input()))
# magnets = list(map(int,input().split()))

for i in range(n-1):
    if magnets[i] != magnets[i+1]:
        count = count+1
print(count)

# 10 10 10 01 10 10