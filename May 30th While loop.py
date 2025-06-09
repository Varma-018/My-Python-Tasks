#Display count down timer from 10 to 0 using while loop?
'''
import time
count = 10
while count >= 0:
    print(count)
    time.sleep(1)  # Wait for 1 second
    count -= 1
print("Countdown finished!")
'''

#Find max digit in number s=2569 using while loop?
'''
s=2569
max_digit=0
while s>0:
    digit=s % 10
    if digit > max_digit:
        max_digit=digit
    s=s//10
print("Maximum digit is:",max_digit)
'''

#simulate a basic login system (max attempts 3)
#Input=['kumar','202','84558906' ]
'''
correct_username= 'kumar'
correct_password= '202'
correct_mobile= '84558906'

attempts=3

while attempts>0:
    username=input("Enter username:")
    password=input("Enter Password:")
    mobile=input("Enter Mobile:")
    
    if username==correct_username and password==correct_password and mobile==correct_mobile:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print(f"Incorrect Details. Attempts Left{attempts}")
        
        if attempts ==0:
            print("Accounts locked. Maximum login attempts Exceeded")
'''