my_string = "Hello, World!"
print(my_string[0:5])
print(my_string[7:]) 
print(my_string[:5])
print(my_string[-6:]) 

text = "Hello World"
print(text.split())  

text = "apple,banana,cherry"
print(text.split(",")) 

my_string = "Hello, World!"

my_string = 'Hello, World!'


my_string = "Hello, World!"
print(my_string[0]) # Output: H
print(my_string[7]) # Output: W

string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ' ' + string2
print(concatenated_string) # Output: Hello World


my_string = "Hello, World!"
length = len(my_string)
print(length) # Output: 13


text = "Hello World"
print(text.lower())  # Output: "hello world"


text = "Hello World"
print(text.upper())  # Output: "HELLO WORLD"

text = "   Hello World   "
print(text.strip())  # Output: "Hello World"

text = "Hello World"
print(text.split())  # Output: ["Hello", "World"]

text = "apple,banana,cherry"
print(text.split(","))  # Output: ["apple", "banana", "cherry"]


text = "Hello World"
print(text.replace("World", "Python"))  # Output: "Hello Python"

text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Python"))  # Output: -1


my_string = "Hello, World!"
print(my_string.lower()) # Output: hello, world!
print(my_string.upper()) # Output: HELLO, WORLD!
print(my_string.strip()) # Output: Hello, World! (no leading/trailing whitespace)
print(my_string.split(',')) # Output: ['Hello', ' World!']
print(my_string.replace('Hello', 'Hi'))# Output: Hi, World!
print(my_string.find('World')) # Output: 7


name = "Alice"
age = 25
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string) # Output: My name is Alice and I am 25 years old.

name = "Alice"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string) # Output: My name is Alice and I am 25 years old.

name = "John"
age = 25
message = f"Hello, my name is {name} and I am {age} years old."
print(message) # Hello, my name is John and I am 25 years old.


num = 42
result = f"The answer is {num * 2}"
print(result)


{
"s": "Rany ElHousieny",
}

{
"s": "Rany",
}


def find_first_occurrence(s, to_find):
    
    try:
        i = s.index(to_find)
        return i
    except ValueError:
        return -1
        
        
def find_first_occurrence(s, to_find):
    
     if (s.count(to_find) > 0):
        return s.index(to_find)
     else:
        return -1
        
def count_alphabets(s):
    
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
            
    return count
    
    
    
