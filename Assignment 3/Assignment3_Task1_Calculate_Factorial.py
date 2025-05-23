#Calculate factorial of given number.
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
num=int(input("Enter number: "))
result=factorial(num)
print("Factorial of ",num," is ", result)
