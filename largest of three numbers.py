num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
largest=0
if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
elif num3>num1 and num3>num2:
    largest=num3
else:
    print("All numbers are equal")
print("Largest number is:",largest) 