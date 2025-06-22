# Write a Python program to print the word with the maximum length from the list m = ['python', 'java', 'c++', 'developer']
'''
m=['python','java','c++','developer']
def max_len(m):
    a=m[0]
    for i in m:
        if len(i)>len(a):
            a=i
    return a
print(max_len(m))
'''
# Given a list and a target number, return all pairs that sum to the target.
'''
li=[1, 2, 3, 4, 5, 6, 7, 8, 9]
tar=10
def pairs(li,tar):
    for i in range(len(li)):
        for j in range(len(li)):
            if (i+j)==tar:
                print(i,'+',j,'='i+j)
pairs(li, tar)
'''
# Write a program to remove duplicate elements from a list.
'''
l1=[1,2,3,5,4,6,3,1,3,8,7,6,4,1,1,1,1,2]
def dup(l1):
    res=[]
    for i in l1:
        if i not in res:
            res.append(i)
    return res
print(dup(l1))
'''
# Write a Python program to print the common elements between two given lists.
'''
l1=[3,4,5,7,8,6,46,84]
l2=[7,6,8,4,53,5,3,46,84,4,37]
def common(l1,l2):
    res=[]
    for i in l1:
            if i in l2:
                res.append(i)
    return res
print(common(l1, l2))
'''
# Write a Python program to move all 0's in the list k = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0] to the end of the list?
'''
k = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]
def move(k):
    res=[]
    c=[]
    for i in k:
        if i==0:
            c.append(i)
        else:
            res.append(i)
    return res + c
print(move(k))
'''