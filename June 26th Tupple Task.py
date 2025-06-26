# 1.    nums = [5, 12, 17, 24, 35, 40, 55]
#               Create a tuple containing only numbers that are divisible by 5 using comprehension.
'''
num=[5,12,17,24,35,40,55]
x=tuple(i for i in num if i%5==0)
print(x)
'''

# 2.	Given a string: "HelloWorld" Create a tuple of all uppercase letters present in the string using comprehension.?
'''
s="HelloWorld"
print(tuple(i for i in s if i.isupper()))
'''
# 3.	marks = [55, 72, 48, 90, 67]
#             Create a tuple where each element is "Pass" if marks are >= 50 else "Fail" using comprehension.?
'''
m=[55, 72, 48, 90, 67]
print(tuple("Pass" if i>=50 else "fail" for i in m))
'''
# 4.	Given a sentence: "Python is powerful and easy to learn"
#             Create a tuple of words that have more than 4 characters using comprehension.
'''
x="Python is powerful and easy to learn"
print(tuple(i for i in x.split() if len(i)>4))
'''
# 5.	students = [("Alice", 85), ("Bob", 45), ("Charlie", 60), ("David", 30)]
#                Create a tuple containing names of students who scored 50 or more using comprehension
'''
s=[("Alice", 85), ("Bob", 45), ("Charlie", 60), ("David", 30)]
print(tuple(name for name, i in s if i >= 50))
'''