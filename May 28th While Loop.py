#Print numbers from 1 to 10 using a while loop.
'''
n=1
while n<=10:
    print(n)
    n+=1
'''

#Print even numbers between 1 and 50 using a while loop.
'''
n=0
while n<=50:
    print(n)
    n+=2
'''

#Print the multiplication table of a given number (e.g., 5) using a while loop.
'''
n=5
i=1
while i <=10:
    print(n,'*',i,'=',n*i)
    i += 1
'''

#Calculate the sum of digits of a number using a while loop.
#e.g., 123 → 6
'''
n=123
sum=0
while n>0:
    digit=n%10
    n=n//10
    sum=sum//1+digit
print(sum)
'''

#Reverse a number using a while loop.
#e.g., 123 → 321
'''
n=123
rev=0
while n>0:
    digit=n%10
    n=n//10
    rev=rev*10+digit
print(rev)
'''

#Check if a number is a palindrome using a while loop.
#e.g., 121 → Palindrome
'''
n=int(input("Enter a number: "))
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
'''

#Print the Fibonacci series up to N terms using a while loop.
'''
a=0
b=1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c
'''

#Count the number of digits in a given number using a while loop.
'''
n=123456
count = 0
while n>0:
    n=n//10
    count +=1
print(count)
'''

#Keep asking the user for input until they enter "exit".
#Hint: Use while True: and break.
'''
while True:
    x=input("Enter  ")
    if x=="exit":
        print("Input Matched")
        break
'''

#Create a number guessing game using a while loop
#Keep looping until the user guesses the correct number.
#Provide hints like "Too High" or "Too Low".
'''
while :
    x=int(input("Enter a Value"))
    if x==50:
        print("Input Matched")
    elif x<50:
        print("Too Low")
    else:
        print("Too High")
'''
