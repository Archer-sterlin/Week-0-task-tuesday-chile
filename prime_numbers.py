def is_prime_num(num):
    factor = []
    for i in range(1,num+1):
        if num % i == 0:
            factor.append(i)
    if len(factor) > 2:
        return f'{num} is not a prime number. {factor}' 
    return f"{num} is a prime number"



 
print(is_prime_num(7))
