'''
Write a Python program to multiply all the items in a dictionary.
'''
d={1: 10, 2: 20, 3: 30, 4: 40}
m=1
for i in d.values():
    m=m*i
print(m)