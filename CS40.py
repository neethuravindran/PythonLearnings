def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = input("Enter the number: ")
print("number : ", num)
print("Factorial : ", factorial(int(num)))
