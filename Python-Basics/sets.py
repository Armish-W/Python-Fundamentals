# print('hi')

# #sets are mutable
# #tuples can be stored in sets
# #sets elements are immutable as they are stores in hash table form
# #tuples can be stored in set as they are immutable
# #lists are mutable
# #we cannot store list in set as they are not immutable
# #if you have to remove duplicates, use set() as itll remove duplicates
# #list is passed not stored

# fruits = {"apple", "banana", "cherry"}
# numbers = set([1, 2, 2, 3]) # duplicates collapse -&gt; {1, 2, 3}
# empty = set()
# print(fruits)
# print(numbers)
# raw_labels = ["cat", "dog","cat","bird", "dog"]
# unique_labels = set(raw_labels)
# print(unique_labels)
# print(empty)
# vocabulary = {"the", "cat", "sat", "on", "mat"}
# print("cat" in vocabulary)      # True  -- fast, hash-based lookup
# print("dog" in vocabulary)      # False
# #time complexity is reduced, its big o 1 not big o n
# # set cannot come within set as its mutable
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a | b  )          # union            -> {1,2,3,4,5,6,7,8}
# print(a.union(b))       # same as a | b
# print(a & b)            # intersection     -> {4,5}
# print(a.intersection(b))
# print(a - b)            # difference       -> {1,2,3}   (in a, not in b)
# print(a.difference(b))
# print(a ^ b)            # symmetric diff   -> {1,2,3,6,7,8}  (in a or b, not both)
# print(a.symmetric_difference(b))
# x = {1, 2}
# y = {1, 2, 3, 4}
# print(x.issubset(y))     # True  -- every element of x is in y
# print(y.issuperset(x))   # True  -- every element of x is in y (from y's side)
# print(x.isdisjoint({9, 10}))   # True -- no elements in common
# s = {1, 2, 3}
# s.add(4)          # {1, 2, 3, 4}
# s.update([5, 6])  # {1, 2, 3, 4, 5, 6}  -- add several items at once
# s.discard(10)     # no error, even though 10 isn't in s
# s.remove(2)   # KeyError: 10
# s.clear()         # empties the set -> set()
# print(s)
# words = ["AI", "ai", "Data", "data", "AI"]
# normalised = {w.lower() for w in words}
# print(normalised)   # {'ai', 'data'}
# fs = frozenset([1, 2, 3]) #no modification
# #fs.add(4)   # AttributeError: 'frozenset' object has no attribute 'add'
# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])
# #frozen set is immutable so you can use frozen set in set where like you want dictionary keys, data saftey to not chnage
# set(a)
# set(b)
# print(a|b)

# tags_key = frozenset({"python", "ai", "lab"})
# article_cache = {tags_key: "Article #101"}
# print(article_cache[frozenset({"ai", "python", "lab"})])  # 'Article #101'
# print(article_cache[tags_key])
# article_cache[tags_key] = "Article #102" 
# # Order inside the frozenset does not matter for equality or hashing.

# bad_key = {"python", "ai", "lab"}         # a plain set
# article_cache[bad_key] = "Article #102"    # TypeError: unhashable type: 'set'
#its not frozen set thats why error
#exception handling
#zero division error
#type error
#import error
def myfunction(a,b):
    return a+b
# def myfunction(a, b):
#   return a + b
# try:
#   myfunction(100, "one hundred")
# except:
#   print("error")
#   raise
# try:
#     myfunction(100, "one hundred") except TypeError:
#     print('Cannot sum variables')
# try:
#   myfunction(100, "one hundred")
# except TypeError:
#     print("Cannot	sum	the	variables.	Please	pass	numbers only.")

# try:
#     myfunction(100, "one hundred")
# except TypeError as e:
#     print(f"Cannot sum	the variables. The exception was: {e}")

# try:
#     x = float(input("Your number: "))	
#     inverse = 1.0 / x 
# finally:
#     print("There may or may not have been an exception.") 
#     print("The inverse: ", inverse)

# try:
#     x = float(input("Your number: "))
#     inverse = 1.0 / x 
# except ValueError:
#     print("You should have given either an int or a float")
# except ZeroDivisionError:
#      print("Infinity")
# finally:
#     print("There may or may not have been an exception.")

# Q1: Write a Python program to find the length of a set, apply all sets operations(union,intersection) and print the results,find maximum and the minimum value in a set,create a shallow copy of sets,check if a set is a subset of another set, remove all elements
# from a given set,check if two given sets have no elements in common.check if a given set is superset of itself and superset of another given set.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
x= len(set1)
print(x)
y= len(set2)
print(y)
print(set1.intersection(set2))
print(set1.union(set2))
print(max(set1))
print(max(set2))
print(min(set1))
print(min(set2))
print(set1)
print(set2)
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
set1.clear()
set2.clear()

# Q2:Python program to count the number of vowels using sets in a given string.

# sample output

# Input : Hello World
# Output : No. of vowels :	3

vowels = {'a', 'e', 'i', 'o', 'u'}
x = input("Enter string:")
total= 0

# Loop through each character in the string
for char in x.lower():
    if char in vowels:
        total += 1

print("Total is", total)

# Q:3 Write a function to add, mul, divide two numbers x and y. Implement exception handling technique
# (try..except clause) for handling possible exceptions in the scenario.

def math_operations():
    try:
        # Prompt user for inputs
        x = float(input("Enter first number (x): "))
        y = float(input("Enter second number (y): "))
        
        # Addition
        print(f"Addition ({x} + {y}): {x + y}")
        
        # Multiplication
        print(f"Multiplication ({x} * {y}): {x * y}")
        
        # Division
        try:
            print(f"Division ({x} / {y}): {x / y}")
        except ZeroDivisionError:
            print("Division Error: Cannot divide by zero.")
            
    except ValueError:
        print("Input Error: Please enter valid numbers (int or float).")

# Call the function
math_operations()