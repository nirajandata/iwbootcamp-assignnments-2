def calculate(x1,x2,cal):
	
	if (cal=="+"):
	 return x1+x2

	elif (cal=="-"):
	 return x1-x2
	
	elif (cal=="*"):
	 return x1-x2
	
	elif (cal=="/"):
	 try:
		 return x1/x2

	 except ZeroDivisionError:
		 return "you can't divide by zero"

	else:
		print("Enter the correct operation")

	
x1=int(input("enter the first number "))
x2=int(input("enter the second number "))
cal=input("enter the operation ")
print(calculate(x1,x2,cal))