##1.Multiplication of two integers using recursion
def multiply(a,b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b-1)
    else:
        return -multiply(a, -b)

a = int(input("Enter a:"))
b = int(input("Enter b:"))

result = multiply(a,b)
print(f"The product of {a} and {b} is: {result}")

# ##2.Using powers without(**)
def power(base,exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base,exponent - 1)
    else:
        return 1/power(base,-exponent)

base = int(input("Enter the base:"))
exponent = int(input("Enter the exponent:"))

result = power(base,exponent)
print(f" {base} power {exponent} is : {result}")

##3.Print numbers from n down to 0
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)

n = int(input("Enter a number to countdown from:"))
countdown(n)

# ##4.Print from 0 to n using modified countdown
def countup(n , current=0):
    if current > n:
        return
    print(current)
    countup(n,current + 1)

n = int(input("Enter a number to countup from:"))
countup(n,current=0)

##5.Reverse a string recursive
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

s = input("Enter the word:")
result = reverse_string(s)
print("Reverse string:", result)

##6.Check if a number is prime
def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

n = int(input("Enter a number to check if its a prime number:"))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is NOT a prime number.")

##7.Convert a number from decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)
n = int(input("Enter a number:"))
binary = decimal_to_binary(n)
print("Binary:" , binary if binary else "0")






