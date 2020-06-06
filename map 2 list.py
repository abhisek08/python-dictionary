'''
Write a Python program to map two lists into a dictionary.
'''
a=[1,2,3]
b=[10,20,30]
d={}
for i in range(3):
    d[a[i]]=b[i]
print(d)
