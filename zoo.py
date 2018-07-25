print("Python Tuples Exercise")

# Create a tuple named zoo that contains your favorite animals.
zoo = ("fox", "dog", "cat", "tiger", "panda")

# Find one of your animals using the .index(value) method on the tuple.
zoo.index("fox")

# Determine if an animal is in your tuple by using for value in tuple.
for animal in zoo:
    if(animal == "tiger"):
        print(animal)

# Create a variable for each of the animals in your tuple with this cool feature of Python.
(fox, dog, cat, tiger, panda) = zoo
print(fox)

# Convert your tuple into a list.
animal_list = list(zoo)

# Use extend() to add three more animals to your zoo.
add_animals = ["lion", "bear", "penguin"]
animal_list.extend(add_animals)
print(animal_list)

# Convert the list back into a tuple.
new_zoo = tuple(animal_list)
print(new_zoo)