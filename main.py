# str1 = "james"
# res = str1[0] # j
# l = len(str1) #5
# mi = int(l/2) #2
# res = res + str1[mi] #jm
# res = res + str1[l-1] #jms
# print(res)

# numbers = [12,75,150,180,145,525,50]

# for item in numbers:
#     if item >500:
#         break
#     elif item >150:
#         continue
#     elif item % 5 == 0:
#         print(item)

# a = ["#","@"]
# key, value
# O(1)
# O(n)
# my_dic = {
#     1:'apple',
#     2: 'ball'
# }

# mylist=[[1,10,20,30,40],[50,60,70,80],[90,100,110,120]] 
# # print(mylist[2][2]) # O(1)
# for i in range(len(mylist)):
#     for j in range(len(mylist[i])):
#         if mylist[i][j] == 110:
#             print(i,j)
# O(n)

print("select your oparator")
print("1.add")
print("2.subtrect")
print("3.multiply")
print("4.divide")
operator =input()
if operator =="1":
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The sum is :"+ str(int(numb1)+int(numb2)))
elif operator =="2":
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The sbtrect is :"+ str(int(numb1)-int(numb2)))
elif operator =="3":
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The multiply is :"+ str(int(numb1)*int(numb2)))
else:
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The divide2 is :"+str(int(numb1)/int(numb2)))

