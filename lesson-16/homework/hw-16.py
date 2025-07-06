# 1. Convert List to 1D Array 
my_list = [12.23, 13.32, 100, 36.32]
array = np.array(my_list)

print(array)

# 2. Create 3x3 Matrix (2?10)
a = np.arange(2, 11).reshape(3, 3)
print(a)

# 3. Null Vector (10) & Update Sixth Value
nul = np.zeros(10)
nul[5] = 11

print(nul)

# 4. Array from 12 to 38
