## 1
year = 2000 
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap)

## 2 
n = 18 

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
## 3
a = 3
b = 10

if a % 2 != 0:
    a += 1

even_numbers = list(range(a, b + 1, 2))
print(even_numbers)
## 4
a = 3
b = 10

even_numbers = list(range(a + (a % 2), b + 1, 2))
print(even_numbers)
