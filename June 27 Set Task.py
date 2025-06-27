# 1.	Create a set with elements from 1 to 5. Add elements 6 and 7 to the set in one line.
'''
s={1,2,3,4,5}
s.update([6,7])
print(s)
'''
# 2.	Given two sets:
#            A = {1, 2, 3, 4, 5}
#            B = {4, 5, 6, 7, 8}
# Find elements that are present in A or B but not both (symmetric difference).
'''
a= {1, 2, 3, 4, 5}
b= {4, 5, 6, 7, 8}
res= a.symmetric_difference(b)
print(res)
'''
# 3.	Remove an element from a set, but avoid error if element doesn't exist.
#  Find maximum and minimum element from a set {5, 8, 12, 3, 15, 7}.
'''
s={5, 8, 12, 3, 15, 7}
x=min(s)
y=max(s)
print(x,y)
'''
# 4.	Create a set with the values: 10, 20, 30, 40. Then add the value 50 to the set.
'''
set= {10, 20, 30, 40}
set.add(50)
print(set)
'''
# 5.	Remove an element 30 from a set {10, 20, 30, 40, 50} using a set method.
'''
s={10, 20, 30, 40, 50}
s.discard(30)
print(s)
'''
# 6.	Check whether the number 25 exists in the set {15, 20, 25, 30, 35}.
'''
x= {15, 20, 25, 30, 35}
s= 25 in x
print(s)
'''
# 7.	Find the union of two sets:
#            A = {1, 2, 3, 4}
#            B = {3, 4, 5, 6}
'''
a= {1, 2, 3, 4}
b= {3, 4, 5, 6}
x= a.union(b)
print(x)
'''
# 8.	Find the intersection of two sets:
#            A = {10, 20, 30, 40}
#             B = {30, 40, 50, 60}
''''
a= {10, 20, 30, 40}
b= {30, 40, 50, 60}
s= a.intersection(b)
print(s)
'''