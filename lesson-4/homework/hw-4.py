## Dictionary Exercises
## 1. Sort a Dictionary by Value
my_dict = {'a': 3, 'b': 1, 'c': 2}
items = [('a', 3), ('b', 1), ('c', 2)]
items_asc = [('b', 1), ('c', 2), ('a', 3)]
items_desc = [('a', 3), ('c', 2), ('b', 1)]
asc_dict = dict(items_asc)
desc_dict = dict(items_desc)
print("Ascending:", asc_dict)
print("Descending:", desc_dict)

## 2. Add a Key to a Dictionary
dict = {0: 10, 1: 20}
dict[2] = 30
print(dict)

## 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic = dic1 | dic2 | dic3 
print(dic)

## 4. Generate a Dictionary with Squares
n = 1
result = {}

if n >= 1:
    result[1] = 1**2
if n >= 2:
    result[2] = 2**2
if n >= 3:
    result[3] = 3**2
if n >= 4:
    result[4] = 4**2
if n >= 5:
    result[5] = 5**2
    
print(result)

## 5. Dictionary of Squares (1 to 15)
n = 1
result = {}

if n >= 1:
    result[1] = 1**2
if n >= 2:
    result[2] = 2**2
if n >= 3:
    result[3] = 3**2
if n >= 4:
    result[4] = 4**2
if n >= 5:
    result[5] = 5**2
if n >= 6:
    result[6] = 6**2
if n >= 7:
    result[7] = 7**2
if n >= 8:
    result[8] = 8**2
if n >= 9:
    result[9] = 9**2
if n >= 10:
    result[10] = 10**2
if n >= 11:
    result[11] = 11**2
if n >= 12:
    result[12] = 12**2
if n >= 13:
    result[13] = 13**2
if n >= 14:
    result[14] = 14**2
if n >= 15:
    result[15] = 15**2

print(result)

## Set Exercises
## 1. Create a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)

## 2. Iterate Over a Set
my_set = {"apple", "banana", "cherry"}
my_list = list(my_set)

print(my_list[0])
print(my_list[1])
print(my_list[2])

## 3: Add Member(s) to a Set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

## 4: Remove Item(s) from a Set
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set) 

## 5: Remove an Item if Present in the Set
my_set = {"apple", "banana", "cherry"}

my_set.discard("banana")  # удалит "banana" если есть, без ошибки, если нет
print(my_set)

