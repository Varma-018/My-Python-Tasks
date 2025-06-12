#1.How do you create an empty list in Python?
'''
L=[]
print(L)
'''
#2. What is the difference between append() and extend()?
'''
L=[1,2,3,4,5]
print(L)
L.append(6)
print(L)
L.extend([7,8,9,0])
print(L)
'''
#3. How can you access the third element in a list?
'''
L=[10,15,20,25,30,35]
l=L[3]
print(l)
'''
#4. How do you update the second element of a list?
'''
L=[10,15,20,25,30,35]
L[2]=18
print(L)
L.insert(3,20)
print(L)
'''
#5. What does the len() function do when used on a list?
'''
L=[10, 15, 18, 20, 25, 30, 35]
print(len(L))
'''
#6. How do you remove an item from a list by value?
'''
L=[10, 15, 18, 20, 25, 30, 35]
L.remove(15)
print(L)
'''
#7. How do you remove an item from a list by index?
'''
L=[10, 15, 18, 20, 25, 30, 35]
L.pop(2)
print(L)
'''