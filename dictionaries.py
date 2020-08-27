'''
# List - key value pairs (objects)
employee = {"Mary": 24, "Shaelyn": 33, "Charis": 31}
print(employee)

# pulling the value from a key in the dictionary
employee["Shaelyn"]
print(employee["Shaelyn"])

# adding a to the dictionary
employee["Andrea"] = 39
print(employee)

# updating a value
employee["Andrea"] = 40
print(employee)

# deleting a key from the dictionary
del employee["Andrea"]
print(employee)

# to get the keys from the dictionary
print(employee.keys())

# to iterate keys to a list - set the list to a value
a = list(employee.keys())
print(a)
# below, you get the index from that list because lists are index valued. Keys aren't
print(a[0])

tuples example - using the item function - Tuples are used to group
together related data, such as a persons name, their age, and their gender
print(employee.items())

'''

# dictionary example

dic = {}
s = input()
for s in s:
    dic[s] = dict.get(s, 0) + 1

print(" ".join(['%s,%s' %(k, v) for k,v in dic.items()]))


