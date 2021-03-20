list1=[("nirajan","dhakal",18),("praahsant","rana magar",19),("ram","karki",None)]

for i in range(len(list1)):
    if list1[i][2] ==None:
        list1.pop(i)

average_age=0

for i in range(len(list1)):
    average_age+=int(list1[i][2])

average_age=average_age/len(list1)
print("The average age is ",average_age)

for i in range(len(list1)):
    age=list1[i][2]
    if age>average_age:
        print(age,"is older")
    else:
        print(age,"is younger")