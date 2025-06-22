# Reverse a String
'''
n="Siva"
def reverse(n):
    res=""
    for var in n:
        res=var+res
    return res
print("Reversed String: ", reverse(n))
'''

#count how many times a is repeated
'''
def count_c():
    n=("Chaitanya")
    count=0
    for variable in n:
        if variable == "a":
            count+=1
    return count
print(count_c())
'''

# Take 2 strings and concat ovels in string
'''
a="siva varma"
b="chekuri"
def con(a,b):
    v="aeiouAEIOU"
    res=''
    for var in a+b:
        if var in v:
            res+=var
    return res
print("Concatinated Vovels:",con(a,b))
'''

#Take a string replace "a" with "i"
'''
n="Chaitanya"
def a_with_i(n):
    res=""
    for obj in n:
        if obj == "a":
            res+="i"
        else:
            res+=obj
    return res
print("New str: ",a_with_i(n))
'''
