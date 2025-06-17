# 1. is_prime(n)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

# 2. digit_sum(k)
def digit_sum(k):
    return sum(int(d) for d in str(k))

# 3. power_of_two(N)
def power_of_two(N):
    power = 1
    result = []
    while (power := power * 2) <= N:
        result.append(power)
    print(*result)
