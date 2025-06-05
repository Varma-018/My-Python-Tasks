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
# Write a program that prints the first 10 powers of 2 using a loop.
'''
def power():
    for i in range(10+1):
        print(f"2^{i} = {2**i}")
print (power())
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
# Count the number of digits in a given integer using a loop.
'''
def count(num):
    count=0
    while(num>0):
        num=num//10
        count+=1
    return count
print(count(123))    
'''
# Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5.
'''
def divisible_3_and_5(num): 
    for i in range(1,num+1):
        if i%3==0 and i %5==0:
            print(i)
divisible_3_and_5(100)
'''
# Without using multiplication, calculate a * b using addition and a loop.
'''
def addition_for_multiplication(a,b):
    res=0
    for i in range(b):
        res=res+a
    print(res)
    return res
addition_for_multiplication(9,8)
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
# Write a program to find the highest digit in a given number.
'''
def high(n):
    high=0
    for i in range(n):
        digit=n%10
        n//=10
        if high > digit:
            high = high
        else:
            high = digit
    return high
print(high(298))
'''
# 11. Write a program to check if a number is positive, negative, or zero.
'''
def num():
    x=int(input("enter a value"))
    if x<0:
        print("Negative")
    elif x==0:
        print("Zero")
    else:
        print("Positive")
    return num
num()
'''
# 12. Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
'''
def num():
    n=int(input('Enter a Number'))
    if n%2==0 and n%3==0:
        print("It is divisible by both 2 & 3")
    elif n%2==0:
        print("It divisible by 2")
    elif n%3==0:
        print("It is divisible by 3")
    else:
        print("Not divisible by 2 & 3")
    return num
num()
'''
# 13. Check if a number is a three-digit number using conditionals.
'''
def count():
    n=int(input("Enter a value"))
    s=str(n)
    if len(s)==3:
        print("It is a Three Digit")
    else:
        print("It is not a Three Digit")
    return count
count()
'''
# 14. Write a program to check whether a given number is a prime number.
'''
def p():
    x=int(input("enter a number"))
    if x<=1:
        print(f"{x} is not a prime number")
    else:
        for i in range(2,x):
            if x%i==0:
                print(f"{x}is not a prime number")
                break
        else:
            print(f"{x} is a prime number")
    return p
p()
'''
# 15. Write a program to find the largest of three numbers entered by the user using nested if-else.
'''
a=int(input("Enter a Value"))
b=int(input("Enter a Value"))
c=int(input("Enter a Value"))
def largest(a,b,c):
    if a>b:
        if a>c:
            print("A is Larger", a,b,c)
        else:
            print("C is Larger", a,b,c)
    elif b>a:
        if b>c:
            print("B is Larger", a,b,c)
        else:
            print("C is Larger", a,b,c)
    else:    # if 2 or more values are equal
        if a==b:
            print("A & B are Equal", a,b,c)
        elif b==c:
            print("B & C are Equal", a,b,c)
        elif a==c:
            print("A & C are Equal", a,b,c)
        else:
            print("All are equal", a,b,c)    
    return largest
largest(a,b,c)
'''
# 16. Check if a year is a leap year or not.
'''
def leap():
    n=int(input("Enter a Value"))
    if n%4==0 and n%100!=0 or n%400==0:
        print("Leap year")
    else:
        print("Not a Leap year")
    return leap
leap()
'''
# 17. Take an integer input and determine if it is even and greater than 50.
'''
def num():
    n=int(input("Enter a value"))
    if n%2==0 and n>=50:
        print("It is even & Grater than 50")
    elif n%2==0 and n<=50:
        print("It is even & Less than 50")
    elif n%2!=0 and n>=50:
        print("It is Odd & Greater than 50")
    else:
        print("It is Odd & Less than 50")
    return num
num()
'''        
# 18. Write a program to classify a number as:
'''
* Less than 0: "Negative"
* 0 to 9: "Single Digit"
* 10 to 99: "Two Digits"
* 100 and above: "Three or More Digits"
'''
'''
def classify():
    n=int(input("Enter a Value"))
    if n<0:
        print("Negative")
    elif n>=0 and n<=9:
        print("Single Digit")
    elif n>=10 and n<=99:
        print("Two Digits")
    else:
        print("Three or more digits")
    return classify
classify()
'''
# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.
'''
def square():
    n=int(input("Enter a Value"))
    s=n**2
    if s>1000:
        print("Yes",s)
    else:
        print("No",s)
    return square
square()
'''
# 20. Take two integers as input and determine if one is a factor of the other.
'''
a=int(input("Enter a Value"))
b=int(input("Enter a Value"))
def factor(a,b):
    if a%b==0 or b%a==0:
        print("One is factor of other")
    else:
        print("No")
    return factor
factor(a,b)
'''