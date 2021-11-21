numbers_of_problems = int(input()) # 3
k =0
for i in range(numbers_of_problems): #0,1,2
    solution = list(map(int,input().split()))
    if sum(solution) >= 2:
        k+=1
print(k)

# solution = list(map(int,input().split())) #1,2,3,1,5
# k = 0
# for i in range(len(solution)): # 4
#     k += solution[i]
# print(k)