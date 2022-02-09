phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

"""
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))

phone = phonebook['Chris']

print(phone)

print(len(phonebook))

mydictionary= dict(m=8,n=9)
print(mydictionary)


print()
print('*****  end section 1 ********')
print()

"""




"""

print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'
if name in phonebook:
    print (phonebook[name])
else: 
    print(name, "is not in the phonebook")


print()
print('*****  end section 2 ********')
print()


"""





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

phonebook['chris'] = "555-0123" #edit

phonebook["Chris"] = "555-4444" #append

print(phonebook)

print()
print('*****  end section 3 ********')
print()





"""
print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook["Chris"]

print(phonebook)



print()
print('*****  end section 4 ********')
print()

"""



"""
print()
print('*****  start section 5 - iterate through keys ********')
print()

for key in phonebook:
    print(key)
    print(phonebook[key])



print()
print('*****  end section 5 ********')
print()

"""


"""

print()
print('*****  start section 6 - iterate through values  ********')
print()


for value in phonebook.values():
    print(value)


print()
print('*****  end section 6 ********')
print()


"""




"""
print()
print('*****  start section 7 - iterate through both key and value pair********')
print()


for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)

for key,value in phonebook.items():
    print(key)
    print(value)



print()
print('*****  end section 7 ********')
print()


"""

"""
print()
print('*****  start section 8 - using get and clear ********')
print()

phone = phonebook.get('Chris', 'key not found')
print(phone)

phonebook.clear()
print(phonebook)

print()
print('*****  end section 8 ********')
print()

"""
"""
print()
print('*****  start section 9 - using pop method ********')
print()

remove= phonebook.pop('Chris', 'not found')
print(remove)

print (phonebook)


print()
print('*****  end section 9 ********')
print()

"""
"""
print()
print('*****  start section 10 - using poptime ********') it doesnot pop up the random number, it only show the last one.
print()

a = phonebook.popitem()
print (a)
print (phonebook)


print()
print('*****  end section 10 ********')
print()

"""
"""
import random
print()
print('*****  start section 11 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)
phone = phonebook[random_key]

##other way to do it
##phone = phonebook[random.choice(list(phonebook))]

print(phone)


print()
print('*****  end section 11 ********')
print()
"""







