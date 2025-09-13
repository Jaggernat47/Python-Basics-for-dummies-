                                                  #===BASIC SYNTAX===

#---PRINTING--- 
print("Hello, Python!")
print("The sum is:", 2 + 3)


#---COMMENT---
"""
Multi-line comment
Good for documentation
"""

#---VARIABLES--- 
x = 10           # integer
pi = 3.14        # float
name = "Alice"   # string
is_ready = True  # boolean

#---INDENTATION---
if x > 5:
    print("x is greater than 5")   # indented with spaces






                                                    #===OPERATORS===

#---ARITHMETIC OPERATORS---
a + b   # addition
a - b   # subtraction
a * b   # multiplication
a / b   # division (returns float)
a // b  # floor division (integer division)
a % b   # modulus (remainder)
a ** b  # exponent (a^b)

#---COMPARISON OPERATORS---
a == b   # equal
a != b   # not equal
a > b    # greater than
a < b    # less than
a >= b   # greater or equal
a <= b   # less or equal

#---LOGICAL OPERATORS---
(a > 5) and (b < 10)   # True if both conditions are True
(a > 5) or (b < 10)    # True if at least one condition is True
not (a > 5)            # negates condition

#---IDENTITY OPERATORS---
a = [1, 2, 3]
b = a
print(a is b)  # True (same memory reference)
print(a == b   # True (Same Values)

#---ASSIGNMENT OPERATORS---
x = 10
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4







                                                     #===CONTROL FLOW===

#---IF ELSE---
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

#---FOR LOOP---
for i in range(5):   # 0, 1, 2, 3, 4
    print(i)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

#---WHILE LOOP---
x = 3
while x > 0:
    print("Countdown:", x)
    x -= 1

#---LOOP CONTROL---
for i in range(10):
    if i == 5:
        break      # stop loop at 5
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)







                                                #===DATA STRUCTURES===

#---STRINGS---
s = "  Hello, Python!  "

s.lower()          # "  hello, python!  "
s.upper()          # "  HELLO, PYTHON!  "
s.capitalize()     # "  hello, python!  "
s.title()          # "  Hello, Python!  "


s.strip()          # "Hello, Python!" (removes spaces)
s.lstrip()         # remove left spaces
s.rstrip()         # remove right spaces

s.find("Python")   # 9 → index where found
s.replace("Hello", "Hi")  # "  Hi, Python!  "

s.startswith("  H")  # True
s.endswith("!")      # True
s.isalpha()          # False (contains space/punctuation)
"123".isdigit()      # True

s.split(",")        # ['  Hello', ' Python!  ']
"-".join(["a", "b", "c"])  # "a-b-c"


#---LISTS---
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")   # add item
fruits.insert(1, "kiwi")  # insert at index
fruits.remove("banana")   # remove item
fruits.pop()              # removes last item
fruits.sort()             # sort list (A-Z)
fruits.reverse()          # reverse list
fruits.clear()            # empty list

fruits.index("apple")     # 0 → find position
fruits.count("apple")     # how many times "apple" appears


#---DICTIONARIES---
student = {"name": "Alice", "age": 20}

student.keys()        # dict_keys(['name', 'age'])
student.values()      # dict_values(['Alice', 20])
student.items()       # dict_items([('name', 'Alice'), ('age', 20)])
student.get("name")   # Alice
student.update({"age": 21})  # update key
student.pop("age")    # remove key-value
student.clear()       # remove all


#---SETS---
nums = {1, 2, 3}

nums.add(4)          # {1,2,3,4}
nums.remove(2)       # remove element (error if not found)
nums.discard(5)      # safely remove (no error if not found)
nums.union({5,6})    # {1,2,3,4,5,6}
nums.intersection({2,3,5}) # {3}
nums.difference({3,4})     # {1,2}


#---TYPE CONVERSION FUNCTIONS---
int("10")      # 10
float("3.14")  # 3.14
str(123)       # "123"
list("abc")    # ['a','b','c']
tuple([1,2,3]) # (1,2,3)
set([1,1,2])   # {1,2}
dict([("a",1), ("b",2)])  # {'a':1, 'b':2}




