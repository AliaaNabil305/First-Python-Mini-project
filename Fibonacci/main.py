count=int(input("Enter the number of Fibonacci numbers: "))
if count<0:
    print("Enter postive number")
else:
    a,b=0,1    

for _ in range(count):
    print(a, end=" ")
    a, b = b, a + b 