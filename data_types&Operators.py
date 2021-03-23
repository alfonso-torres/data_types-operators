# Let's see the data types in action

a = 24 # Int
b = 16 # Int
c = 5.5 # float

# Let's check the boolean values
print(a > b)
print(a < b)

# Let's look at some built in methods for boolean
greetings = "Hello World!"
# isalpha() helps us find if the variable holding letters without spaces and special characters
print(greetings.isalpha())

# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
print(isinstance(5, int))

# islower() checks if the statement in lower case
print(greetings.islower())

print(greetings.endswith("!"))
print(greetings.startswith("H"))
print(isinstance(5,int))
# in SQL we have seen Null but in Python we have None which is a key word in Python
x = None
print(x)
print(type(x))
print(x is None)

# Arithmetic Operators
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a + c)

