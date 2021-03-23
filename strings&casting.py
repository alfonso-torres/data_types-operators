# Strings and Casting

# Let's have a look at some industry practices
# single and double quotes examples

# greetings = 'hello world'
# single_quotes = 'single quotes \'WoW\''
# double_quotes = "double quotes 'WoW'" # It is more easier to use
# print(greetings)
# print(single_quotes)
# print(double_quotes)

# String slicing

# greetings = "Hello world!" # String
# indexing in Python starts from 0
# H e l l o   w o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
# how can we find out the length of this statement/string

# print(len(greetings))
# We have a method called len() to find out the total length of the statement

#print(greetings[0:5]) # out puts Hello starting from 0 to 4
# print(greetings[6:11]) # out puts world starting from 6 to 10
# print(greetings[-1])

# reverse indexing starts with -1

# Let's have a look at some strings methods
# white_space = "Lot's of space at the end                        "
# strip() helps us delete all white spaces
# print(len(white_space))
# print(len((white_space.strip())))

Example_text = "here's Some texts with lot's of text"
# print(Example_text.count("text"))
# counts the number of times the word is mentioned in the statement
print(Example_text)
print(Example_text.upper())
print(Example_text.lower())
print(Example_text.capitalize()) # capitalises first letter of the string
print(Example_text.replace("with", ","))
# will replace the world "with" , in this case