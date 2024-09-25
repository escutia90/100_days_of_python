def is_prime(num):
    isPrime = True
    if num != 1:
        for i in range(2,num -1):
            if num % i == 0:
                isPrime = False
    return isPrime
    

print(is_prime(1))