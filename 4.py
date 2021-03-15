l1=[]
i1=id(l1)
print(l1)
l1.append("nirajan")
l1.append("shyam")
i2=id(l1)
print(l1)
if(i1==i2):
    print("id didn't changed ")
else:
    print("id changed")
print("the first item is "+l1[0]+" and the second item is "+l1[1])