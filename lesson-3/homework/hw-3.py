## 1: Create and Access List Elements
fruits = ["apple", "banana", "cocos", "persic", "cherry"]
print(fruits[2])

## 2: Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2 
print(combined)

## 3: Extract Elements from a List
listofnumbers = [1, 2, 3, 4, 5]
fml = [listofnumbers[0], listofnumbers[2], listofnumbers[4]]
print(fml)

## 4: Convert List to Tuple
favorites = ["Great Gatsy", "Passengers", "Wolf from Wall-Street", "Interstellar"]
favorites_tuple = tuple(favorites)
print(favorites_tuple)

## 5: Check Element in a List
cities = ["London", "New York", "Berlin", "Tokyo", "Madrid"]
print("Paris" in cities)

## 6: Duplicate a List Without Using Loops
nums = [1, 2, 3]
print(nums * 2)

## 7: Swap First and Last Elements of a List
numbers = [10, 20, 30, 40]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

## 8: Slice a Tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[3:7])

## 9: Count Occurrences in a List
colors = ["green", "white", "purple", "blue"]
print(colors.count("blue"))

## 10: Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger", "elephant")
print(animals.index("lion"))

## 11: Merge Two Tuples
num1 = (1, 2, 3)
num2 = (4, 5, 6)
nums = num1 + num2
print(nums)

## 12: Find the Length of a List and Tuple
my_list = [10, 20, 30, 40, 50]
my_tuple = (100, 200, 300)

print(f"List length is: {len(my_list)} and tuple length is: {len(my_tuple)}")

## 13: Convert Tuple to List
ttuple = (1, 2, 3, 4, 5)
converted_list = list(ttuple)
print(converted_list)

## 14: Find Maximum and Minimum in a Tuple
numbers = (7, 3, 9, 1, 5)
print(min(numbers), max(numbers))

## 15: Reverse a Tuple
words = ("apple", "banana", "cherry", "date")
print(words[::-1])
