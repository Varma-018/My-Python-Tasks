# 1)  From the list nums = [10, 25, 30, 45, 50, 60], create a set of numbers where the number is divisible by 5 but not divisible by 10 using set                 comprehension.
'''
nums = [10,25,30,45,50,60]
print([i for i in nums if i%5==0 and i%10!=0])
'''
# 2)	Write a program to sum the digits of all numbers in a list.
#     Example: [12, 34, 5] ➞ 1+2 + 3+4 + 5 = 15
'''
x=[12,34,5]
count=0
for num in x:
    while num>0:
        digit=num%10
        count+=digit
        num//=10
print(count)
'''
# 3)	Create a new list by repeating elements of a list n times.
#              Example: [1, 2, 3], n = 2 ➞ [1, 2, 3, 1, 2, 3]
'''
x=[1,2,3]
n=2
print(x*n)
'''
# 4)	Write a function to count frequency of each element in a list (return as dictionary).
'''
n= [10,25,30,45]
l=[]
for i in n:
    if i not in l:
        x=n.count(i)
        y=f"{i}:{x}"
        l.append(y)
print(l)
'''
# 5)	Write a function to count how many prime numbers exist in a given range.
'''
n=23
a=tuple(i for i in range(2,n+1) if all(i%j!=0 for j in range(2,int(i**0.5)+1)))
print({len(a)})
'''
# 6)	Write a function to calculate the sum of digits of a number until a single-digit result is obtained.
#   Example: 9875 ➞ 9+8+7+5=29 ➞ 2+9=11 ➞ 1+1=2
'''
def x(num):
    count=0
    while num>0:
        digit=num%10
        count+=digit
        num//=10
    print(count)
    if count>=10:
        x(count)
x(9875)
'''