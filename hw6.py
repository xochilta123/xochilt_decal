import numpy as np
def is_prime(n):
    if n <= 1:
        return False
    if n== 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def containsPrime(arr):
    prime_mask = np.vectorize(is_prime)(arr)
    return arr[np.any(prime_mask, axis = 1)]
arr = np.array([[2,3,5],[4,6,8],[11,13,17],[7,10,13]])
result = containsPrime(arr)
print(result)