n = int(input())
# 0,1,2
mainInp = input()
print(mainInp)
k = 0

for i in range(n):
    if(mainInp[i] == mainInp[i+1]):
        k += 1
print(k)

# person = SELECT * FROM person WHERE age <=30;
# ORM = Obejct relational mapper

# Model 


# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age= models.IntegerField()
#     address = models.CharField(max_length=30)
#     description= models.TextField()



