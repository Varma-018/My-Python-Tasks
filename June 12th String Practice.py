#1.	Reverse a string.
#Input: "hello" → Output: "olleh"
'''
S="hello"
print(S[4::-1])
'''
#2.	Check if a string is a palindrome.
#Input: "madam" → Output: True
'''
s="madam"
k=s[::-1]
print(k)
if k==s:
    print(True)
else:
    print(False)
'''
#3.	Count the number of vowels in a string.
#Input: "OpenAI" → Output: 3
'''
s="OpenAI"
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1
print (count)
'''
#4.	Find the most frequent character in a string.
#Input: "hello" → Output: 'l'
'''
s="hello"
for x in s:
    c=0
    for y in s:
        if x==y:
            c+=1
    if c==2:
        print(x)
'''
'''
a=input()
result="" #to store the character with the highest frequency
count=0 #to store how many times that character appears
for i in a:
    if a.count(i)>count: #"a.count(i)" how many times 'i' appears in string & compare with "count"
        result=i 
        count=a.count(i) 
print(result,count)
'''
#5.	Remove all duplicates from a string.
#Input: "aabbcc" → Output: "abc"
'''
s="aabbcc"
for x in s:
    c=2
    for y in s:
        if x==y:
            c-=2
    if c==0:
        print(x)
'''