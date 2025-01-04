num=int(input("Enter the number of Factorial: "))
sum=1
for i in range(1, num + 1):
    sum *= i
print("The factorial of", num, "is", sum)  