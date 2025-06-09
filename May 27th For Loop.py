#Count how many numbers between 1 and 50 are divisible by 7.
'''
count = 0
for i in range(1,51):
    if i % 7 == 0:
        count+=1
        print(i)
'''
#Print the factorial of a number (e.g., 5!) using a for loop.
'''
x=5
y=1
for i in range(x):
    y*=i
    print(y)
'''
# Print all numbers from 1 to 40nwhich are divisible by both 5 and 7
'''
count = 0
for i in range(1,41):
    if i % 5==0 and i % 7 ==0:
        print(i)
        count += 1
'''