# 1. Write a Python program to rotate a list to the right by k steps.
'''
l=[1,2,3,4,5,6]
k=2
print(l[-k:]+l[:-k])
'''
# 2. Write a Python program to find the sum of prime digits in the number L = 123456.
'''
l=123456
total=0
prime=[2,3,5]
while l>0:
    digit=l%10
    if digit in prime:
        total+=digit
    l//=10
print(total)
'''
# 3. Write a Python program to find the sum of even digits in the number M = 65897.
'''
m=65897
total =0
while m>0:
    digit=m%10
    if digit%2==0:
        total+=digit
    m//=10
print(total)
'''
# 4. Write a Python program to calculate the sum of the largest elements from each row of a 2D list. EX: M=[[1,2,3],[4,5,6],[7,8,9]] output: 24
'''
m=[[1,2,3],[4,5,6],[7,8,9]]
s=0
for i in m:
    s+=max(i)
print(s)
'''
# 5. Write a Python program to find the product of all elements in a list.
'''
l = [1,2,3,4,5,6]
p = 1
for i in l:
    p=p*i
print(p)
'''
# 6. Write a Python program to check whether a given number is an Armstrong number or not. EX: K=153
'''
k=153
h=k
res=len(str(k))
total=0
while k>0:
    digit=k%10
    total+=digit**res
    k//=10
print("Armstrong Number" if total==h else "Not an Armstrong Number")
'''
# 7. Write a Python program to check whether a given number is a Perfect number or not. Perfect number: sum of all factors of a given number
'''
n=int(input("Enter"))
x=0
for i in range(1,n):
    if n%i==0:
        x+=i
if x==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
'''