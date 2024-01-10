def factorial(number):
    factorial_result = 1

    for count in range(1, number + 1):
        factorial_result *= count
    
    return factorial_result

def double(number):
    return number * 2

def triple(number):
    return number * 3
