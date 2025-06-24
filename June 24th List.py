# 1.	Flatten the nested list [[1, 2], [3, 4], [5, 6]] into a single list.
'''
L=[[1, 2], [3, 4], [5, 6]]
res=[]
for i in L:
    for j in i:
        res.append(j)
print(res)
# Method 2
res = [j for i in L for j in i]
print(res)
'''
# 2.	From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.
'''
l=[[2, 5], [7,9], [12, 15]]
res=[]
for i in l:
    for j in i:
        if j%2==0:
            res.append(j)
print(res)
# Method 2
res=[ j for i in l  for j in i if j%2==0]
print(res)
'''
# 3.	Create a list of squares for numbers from 1 to 20.
'''
sq=[]
for i in range (1,21):
    sq.append(i**2)
print(sq)
# Method 2
sq=[i**2 for i in range(1,21)]
print(sq)
'''
# 4.	Print prime numbers between 10 to 20 using list comprehension?
'''
p=[i for i in range(10,20)  for j in (2,i) if (i%j)!=0]
print(p)
# Method 2
p=[]
for i in range (10,20):
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            p.append(i)
print(p)
'''
# 5.	Convert a=10 int data type to 10 string data type  with out using str()?
'''
a=10
k=''
d="0123456789"
while a>0:
    m=a%10
    a//=10
    for i in range(len(d)):
        if i==m:
            k=d[i]+k
print(k,type(k))
'''         
# 6.	Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method.
'''
x="PYTHON programming"
for i in x:
    if ord(i) >= 65 and ord(i) <= 91:
        print(chr(ord(i)+32),end="")
    else:
        print(chr(ord(i)-32),end="")

# Method 2
x="PYTHON programming"
res=""
for i in x:
    if i.isupper():
        res+=i.lower()
    else:
        res+=i.upper()
print(res)
'''
# 7.	Write a list comprehension to print only the word 'python' from the list.
#                      S=[ ‘python’ ,’java’ , ‘c++’ , ‘developer’ ]
'''
s=['python', 'java', 'c++', 'developer']
res=[i for i in s if i[0]=='p']
print(res)
'''