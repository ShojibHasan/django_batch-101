#Python List

# students = ["Rakib","Sakib","Rahim","Kabir"]
# teacher= ["Sisir","Shojib"]
# a = "20"
# print(students)
# print(students[0])
# print(len(students))
# print(type(students))
# print(type(a))
# students.insert(2,"Ashraful")
# print(students)
# students.extend(teacher)
# print(students)
# students.remove("Rakib")
# print(students)
# students.pop(3)
# print(students)

# a,b,c = input().split()
# list1 = list(map(int,input()))

students = ["Rakib","Sakib","Rahim","Kabir",10,20,30] # 7
# for i in range(len(students)):
#     print(students[i])

# starting, ending, distance,skip

# for i in range(0,10,3):
#     print(i)

# i = 0
# while i< len(students):
#     if students[i] == 10:
#         break
#     print(students[i])
#     i +=1
#     print("In the While Loop")

# print("Out of the while loop")

# students1 = ["Rakib","Sakib","Rahim","Kabir","lol","Pretty"]
# print(students1.sort())
# students2 = []

# for i in students1:
#     if "a" in i:
#         students2.append(i)
# print(students2)

# take an empty list. insert 10 data in the list. sort the data 
# data1 = [2,4,56,45,34,3,5,7,6,8,5,8]
# data2 = []


# data1.sort()
# for i in data1:
#     # i <= len(data1)
#     data2.append(i)
# print(data2)


aList=[]

for i in range(5):
    a=input()
    aList.append(a)
    aList.sort()

  
print(aList)
# print(sorted(aList))


# k=aList.sort()

# print(k)


w = int(input())
if w >2:
    if w%2==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
