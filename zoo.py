# **************************** Challenge: Zoo ****************************
print("************ Zoo *************************")
"""
Author: Trinity Terry
pyrun: python zoo.py
"""

# Create a tuple named zoo that contains 10 of your favorite animals.

zoo = ("monkey", "cat", "dog", "cow", "pig",
       "horse", "whale", "bird", "duck", "chicken")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
print("Index of 'dog': ", zoo.index("dog"))

# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "bird"

if animal_to_find in zoo:
    print(f"{animal_to_find} is in the Zoo")

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
(one, two, three, four, five, six, seven, eight, nine, ten) = zoo
print(one, two, three, four, five, six, seven, eight, nine, ten)


# Convert your tuple into a list.
zoo = list(zoo)

print("tuple as a list: ", zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(["zebra", "panda", "leopard"])

print(zoo)

# Convert the list back into a tuple.

zoo = tuple(zoo)

print("list as a tupple: ", zoo)
