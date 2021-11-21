# a =[1,2,3,4,54]
# # a = 1
# # a = "a"

# # array / list

# a =[1,2,3,4,54]
# # print(a[3])
# sum =0 #3
# for i in range(len(a)): # 0,1,2,3,4
#     sum += a[i]
# 0,1,2,3
a = [[2,4,5,7],
    [1,5,8,0],
    [8,1,2,0],
    [8,6,4,1]]
result =0
for i in range(len(a)): 
    for j in range(len(a[i])):
        result += a[i][j]
print(result)


# a = [[1,2,3,4,5],[5,6,7,8,9],[1,2,3,4,5,6]]
# print(a[a>2] )

# data = [True for i in range(6)]
# print(str(data))