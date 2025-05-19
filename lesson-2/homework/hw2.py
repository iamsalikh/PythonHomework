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


