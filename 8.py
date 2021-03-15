def is_prime(num):
 bl=False
 if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            return False
 return True
print(is_prime(22))