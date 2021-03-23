# Introduction to Python data type and operators

- Strings:
```` python
greetings = "Hello World!"
````  
The None keyword is used to define a null value:
```` python
x = None
````  
- Numbers Integers -> floats, longs:
```` python
a = 24 # Int
b = 16 # Int
c = 5.5 # float
````  
- Boolean (True or False):
```` python
print(a > b) # True is printed
print(a < b) # False is printed
````  


### *Arithmetic Operators*
```` python
+, -, *, /
````
- Modulo operator `%` returns the remainder of dividing two numbers.

### *Comparison Operators*

- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to 
- `==` equals
- `!=` not equal to

### *Strings and Casting*

- Indexing in Python starts from 0.
````python
H e l l o   w o r l d  !
0 1 2 3 4 5 6 7 8 9 10 11
````
- Reverse Indexing.
````python
H e   l   l  o     w  o  r  l  d  !
0 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
````
- We have a method called len() to find out the total length of the statement:
````python
print(len(greetings))
````
- You can return a range of characters by using the slice syntax:
````python
print(greetings[0:5]) # out puts Hello starting from 0 to 4
print(greetings[6:11]) # out puts world starting from 6 to 10
````

### *Let's have a look at some strings methods*

- How to returns a copy of the string by removing white spaces, split():
````python
white_space = "Lot's of space at the end                        "
print(len(white_space))
print(len((white_space.strip())))
````
- The function count() will return the total count of a given element in a string:
````python
Example_text = "here's Some texts with lot's of text"
print(Example_text.count("text"))
````
- The method upper() converts all lowercase characters  in a string into uppercase characters:
````python
print(Example_text.upper())
````
- The method lower() returns the lowercased string from the given string:
````python
print(Example_text.lower())
````
- The capitalize() method converts first character of a string to uppercase letter:
````python
print(Example_text.capitalize()) # capitalises first letter of the string
````
- The replace() method replaces the occurrences of the old substring with the new substring:
````python
print(Example_text.replace("with", ",")) # will replace the world "with" , in this case
````

### *Concatenation and Casting*

- We use the symbol `+` to concatenate: <br/>
````python
First_name = "James"
Last_name = "Bond"
print(First_name + " " + Last_name)
````
- F- String is an amazing magical formatting f
````python
print(f"Your Fist Name is {First_name} and Last Name is {Last_name} and you are {age} old")
````
- Casting is when you convert a variable value from one type to another: <br/>
In Python, done with functions such as int() or float() or str()
````python
x = "100"
y = "-90"
print(x + y) # 100-90 is printed
print(int(x) + int(y)) # 10 is printed
````
