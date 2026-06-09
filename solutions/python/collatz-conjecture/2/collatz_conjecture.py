def steps(number):
    """Function that determines the number of steps it takes to reduce a given number to 1 using     the Collatz Conjecture"""
    if number == 0 or number < 0:
        raise ValueError("Only positive integers are allowed")

    num_steps = 0
    while number > 1:
        if number % 2 == 0:
            number /= 2
            num_steps += 1
        else:
            number = number * 3 + 1
            num_steps += 1

    return num_steps
