# 1. ZeroDivisionError
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. ValueError
# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer!")

# 3. FileNotFoundError
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

# 4. TypeError
# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Inputs must be numbers (int or float).")

# 5. PermissionError
# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open("/root/secret.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Permission denied.")

# 6. IndexError
# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range.")

# 7. KeyboardInterrupt
# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# 8. ArithmeticError
# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

# 9. UnicodeDecodeError
# Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open("textfile.txt", encoding="ascii") as file:
        print(file.read())
except UnicodeDecodeError:
    print("Unicode decode error.")

# 10. AttributeError
# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    lst = [1, 2, 3]
    lst.upper()
except AttributeError:
    print("List object has no attribute 'upper'.")

# 1. Read entire text file
with open("sample.txt", "r") as file:
    print(file.read())

# 2. Read first n lines of file
n = 3
with open("sample.txt") as file:
    for i in range(n):
        print(file.readline().strip())

# 3. Append text to a file and display the text
with open("sample.txt", "a") as file:
    file.write("\nNew line added.")
with open("sample.txt", "r") as file:
    print(file.read())

# 4. Read last n lines of file
from collections import deque
n = 2
with open("sample.txt") as file:
    for line in deque(file, n):
        print(line.strip())

# 5. Read file line by line into list
with open("sample.txt") as file:
    lines = file.readlines()
print(lines)

# 6. Read file line by line into variable
with open("sample.txt") as file:
    content = "".join(file.readlines())
print(content)

# 7. Read file line by line into array
with open("sample.txt") as file:
    arr = [line.strip() for line in file]
print(arr)

# 8. Find longest words
with open("sample.txt") as file:
    words = file.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)

# 9. Count number of lines
with open("sample.txt") as file:
    line_count = sum(1 for line in file)
print("Number of lines:", line_count)

# 10. Count frequency of words
from collections import Counter
with open("sample.txt") as file:
    words = file.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)

# 11. Get file size
import os
print("File size:", os.path.getsize("sample.txt"), "bytes")

# 12. Write list to file
lst = ["apple", "banana", "cherry"]
with open("list.txt", "w") as file:
    for item in lst:
        file.write(item + "\n")

# 13. Copy contents to another file
with open("sample.txt", "r") as src:
    with open("copy.txt", "w") as dest:
        dest.write(src.read())

# 14. Combine lines from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

# 15. Read random line from file
import random
with open("sample.txt") as file:
    lines = file.readlines()
    print(random.choice(lines).strip())

# 16. Check if file is closed
f = open("sample.txt")
print("Closed:", f.closed)
f.close()
print("Closed:", f.closed)

# 17. Remove newline characters
with open("sample.txt") as file:
    lines = [line.strip() for line in file]
print(lines)

# 18. Count words in text file
with open("sample.txt") as file:
    text = file.read().replace(",", " ")
    words = text.split()
print("Word count:", len(words))

# 19. Extract characters from text files into list
import glob
chars = []
for filename in glob.glob("*.txt"):
    with open(filename) as file:
        chars.extend(list(file.read()))
print(chars)

# 20. Generate 26 text files from A.txt to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt\n")

# 21. Create a file with alphabet, n letters per line
n = 5
alphabet = string.ascii_lowercase
with open("alphabet.txt", "w") as file:
    for i in range(0, len(alphabet), n):
        file.write(alphabet[i:i+n] + "\n")
