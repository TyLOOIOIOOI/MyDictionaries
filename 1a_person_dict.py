person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(type(person["children"]))

print (type(person["pets"]))

# print child - "Betty"
childname=person['children'][1]
print(childname)

# print the pet name of the cat
cat = person['pets']['cat']
print (cat)

# use a for loop to print out all the children
for child in person['children']:
    print(child)



# use a for loop to print out the type of pet and name of pet
for pet in person['pets']:
    print(pet)
    print(person['pets'][pet])
    