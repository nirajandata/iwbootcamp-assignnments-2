list1=[("ravi","lamichanne",30),("nirajan","dhakal",18),("hari","kumar",None)]
av_age=[]
list2=[]

#for filtering the none values
for i in range(len(list1)):
    test=str(list1[i][2])
    if (test != "None"):
        list2.append(list1[i])
#for appending age
for i in range(len(list2)):
    av_age.append(list2[i][2])

avg = sum(av_age)/len(av_age)
print("the average age are",avg)

for i in range(len(list2)):
    if list2[i][2] > avg:
        print(list2[i][0] + " is old")
    else:
        print(list2[i][0] + " is young")

 