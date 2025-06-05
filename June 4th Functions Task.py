# Write a program to print the sum of all even numbers between 1 and 100 using function.
'''
def sum_range(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
        print(sum)
b= sum_range(1,100)
print(sum)
'''

# Calculate the factorial of a number entered by the user.
'''
n = int(input("Enter a number to calculate its factorial: "))
def f(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(f(n))
'''

# Print the reverse of a given number (e.g., input 1234 → output 4321).
'''
def rev(num):
    x=0
    rev=0
    while (num>0):
        x=num%10
        num=num//10
        rev=rev*10+x
    return rev
print(rev(1234))
'''

# Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
'''
def add(a):
    sum=0
    while(a>0):
        digit=a%10
        sum+=digit
        a=a//10
    return sum
print(add(123))
'''

# Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
# def rev(n):
'''
def palindrome(k):
    n=k
    j = n
    rev=0
    while n>0:
        digit=n%10
        n=n//10
        rev=rev*10+digit
    if rev==j:
        print("Palindrome")
    else:
        print("Not a Palindrome")
    return rev
print(palindrome(121))
'''
