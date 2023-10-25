def prime_factorization(number):
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors
    

