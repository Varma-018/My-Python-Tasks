# 1.	Create a dictionary from two lists:
'''
keys =['id', 'name', 'age']
values =[101, 'John', 25]
print(dict(zip(keys,values)))
'''
# 2.	Create a dictionary to store student name and age.
'''
k={}
k['name']=input('Enter name')
k['Age']=input('Enter Age')
print(k)
'''
# 3.	Create an empty dictionary and add key-value pairs one by one.
'''
k={}
k ['Name']='Varma'
print(k)
k.update({'Age':22})
k.update({'Mobile':768041350})
print(k)
'''
# 4.	Get the value of key "salary" from this dictionary:
'''
Employee = {'name': 'John', 'age': 30, 'salary': 50000}
print(Employee['salary'])
'''
# 5.	 Remove the last inserted key-value pair from the dictionary using an appropriate method
'''
k={}
k ['Name']='Varma'
print(k)
k.update({'Age':22})
k.update({'Mobile':768041350})
print(k)
#Method-1
k.pop('Mobile')
print(k)
#Method-2
k.popitem()
print(k)
'''
# 6.	Define packing and unpacking in Python. Also, provide one example for both packing and unpacking
'''
Packing:- This packing is nothing but grouping n no.of elements into a single variable is called packing.
Example:- [100,150,200,'Python',True]
Unpacking:- This is nothing but gettting the elemnts from the single variable and assiging diffrent variables to the elemnts is called unpacking.
Example:-
x=[100,150,200,'Python',True]
a,b,*c=x
print(a)
print(b)
print(c)
'''