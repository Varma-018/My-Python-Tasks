# 1.	Access the value 200 from this nested tuple?
#                       t = (10, 20, (30, 40, (100, 200)), 50)
'''
t=(10, 20, (30, 40, (100, 200)), 50)
print(t [2][2][1])
'''
# 2.	Access the value 70 from the nested structure?
#                    data = (10, (20, 30, (40, 50, (60, 70))), 80)
'''
data=(10,(20,30,(40,50,(60,70))),80)
print(data[1][2][2][1])
'''
# 3.	Convert   j=(10,20,30,40,50)  tuple data type to list data type?
'''
j=(10,20,30,40,50)
x=list(j)
print(type(x))
'''
# 4.	Find Common Elements Between Two Tuples
#          t1 = (1, 2, 3, 4)
#          t2 = (3, 4, 5, 6)
'''
t1= (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
c=()
for i in t1:
    if i in t2:
        c+=(i,)
print(c)   
'''