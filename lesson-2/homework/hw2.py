# 1. Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input("Write your name: ")
year_of_birth = int(input("Write your year of birth: "))  # ← Закрыли скобку здесь
from datetime import datetime
current_year = datetime.now().year
age = current_year - year_of_birth
print(f"{name}, you are {age} years old.")

# 2. Extract car names from the following text:
txt = 'LMaasleitbtui'
car1 = txt[::2] 
print(car1)
car2 = txt[1::3] 
print(car2)     
print("Cars found:", car1.capitalize(), "and", car2.capitalize())

# 3. Extract car names from the following text:
txt = 'MsaatmiazD'
car = txt[::2]  
print("Car found:", car.capitalize()) 

# 4. Extract the residence area from the following text:
txt = "I'm John. I am from London"
start = txt.find("from") + len("from ")
residence = txt[start:]
print("Residence area:", residence)

# 5. Write a Python program that takes a user input string and prints it in reverse order.
txt = "I'm John. I am from London"
start = txt.find("from") + len("from ")
residence = txt[start:]
print("Residence area:", residence)

# 6. Write a Python program that counts the number of vowels in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# 7. Write a Python program that takes a list of numbers as input and prints the maximum value.
nums = input("Enter numbers: ").split()
max_value = int(nums[0])

for n in nums:
    if int(n) > max_value:
        max_value = int(n)

print("Max value:", max_value)

# 8. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("Write a word: ")
word = word.lower() 
reversed_word = word[::-1]  
if word == reversed_word:
    print("This is palindrome")
else:
    print("This is not palindrome")

# 9. Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter your email address: ")
domain = email.split('@')[-1]  
print("Domain:", domain)

# 10. Write a Python program to generate a random password containing letters, digits, and special characters.
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
chars = letters + digits + special
password = ""
for _ in range(12):
    password += random.choice(chars)
print("Password:", password)
