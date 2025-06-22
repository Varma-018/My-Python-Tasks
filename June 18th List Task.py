# Rotate a list by k positions.
'''
def rotate(a):
    b=[]
    c=[]
    k=2
    for i in range(len(a)-k, len(a)):
        b.append(a[i])
    for i in range(len(a)-k):
        c.append(a[i])
    print(b+c)
a=[1, 2, 3, 4, 5, 6, 7]
rotate(a)
'''
# Find the second largest element in a list without sorting.
'''
li=[1,2,3,55,0,98,67]
li.remove(max(li))  # Remove the largest element
print(max(li))  # The new maximum is the second largest element
'''
# Move all zeroes to the end of the list while maintaining the order.
'''
li=[1,3,4,6,0,2,0,4,8,0,5,6,0,0]
def zero(l):
    res=[]
    value=[]
    for i in l:
        if i==0:
            value.append(i)
        else:
            res.append(i)
    return res+value
print(zero(li))
'''
# Remove duplicates from a list without using set().
'''
l=[1,2,3,6,3,2,5,7,9,2,2,0,0,5,2,4,7,1,0,4,6,2]
def dup(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
print(dup(l))
'''
# Count the frequency of each element in a list.
'''
l=[1,2,3,6,3,2,5,7,9,2,2,0,0,5,2,4,7,1,0,4,6,2]
def frequency(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    for i in l1:
        print(i,":",l.count(i),end="   ")
frequency(l)
'''
# Find the maximum product of two elements in a list.
'''
l=[1,2,3,6,3,2,5,7,9,2,2,0,0,5,2,4,7,1,0,4,6,2]
def max_product(l):
    max=0
    for i in range (len(l)-1):
        a=l[i]*l[i+1]
        if a>max:
            max=a
        else: 
            max=max
    return max
print(max_product(l))
'''
# Reverse a list without using built-in reverse functions.
'''
l=[1,2,3,6,3,2,5,7,9,2,2,0,0,5,2,4,7,1,0,4,6,2]
def reverse(l):
    li=[]
    for i in range (len(l)-1,-1,-1):
        li.append(l[i])
    return li
print(reverse(l))
'''
# Check if a list is a palindrome.
'''
l=[2,0,5,0,2]
def palindrome(l):
    res=[]
    for i in range(len(l)-1,-1,-1):
        res.append(l[i])
    if l==res:
        print (res,'palindrome')
    else:
        print (res,'not palindrome')
palindrome(l)
'''
# Find the common elements between two lists.
'''
l1=[1, 2, 3, 4, 5]
l2=[4, 5, 6, 7, 8]
def common(l1,l2):
    res=[]
    for i in l1:
        if i in l2:
            res.append(i)
    return res
print(common(l1, l2))
'''
# Replace every element with the greatest element on its right.


