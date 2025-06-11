## 1. Modify String with Underscores
def modify_string(txt):
    vowels = 'aeiou'
    result = ''
    i = 0
    count = 0  

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
            if (txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_')):
                if i + 1 < len(txt) - 1:
                    result += txt[i + 1]
                    result += '_'
                    i += 1
            else:
                if i < len(txt) - 1: 
                    result += '_'
            count = 0  
        i += 1

    return result

## 2. Integer Squares Exercise
n = int(input())

for i in range(n):
    print(i ** 2)

## Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Print pattern 1 2 ... using nested loop
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Calculate sum of all numbers from 1 to given number
n = int(input("Enter number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum is:", total)

# Print multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)

# Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100 and num % 5 == 0:
        print(num)

# Count total digits in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Total digits:", count)

# Print reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Print list in reverse order using loop
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)

# Display message “Done” after loop finishes
for i in range(5):
    print(i)
print("Done!")

# Print all prime numbers between 25 and 50
for num in range(25, 51):
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)

# Display first 10 terms of Fibonacci series
n1, n2 = 0, 1
count = 0

while count < 10:
    print(n1, end=' ')
    n1, n2 = n2, n1 + n2
    count += 1

# Find factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")

# Return elements not common between two lists
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for elem in c1:
        diff = c1[elem] - c2.get(elem, 0)
        if diff > 0:
            result.extend([elem] * diff)

    for elem in c2:
        diff = c2[elem] - c1.get(elem, 0)
        if diff > 0:
            result.extend([elem] * diff)

    return result
