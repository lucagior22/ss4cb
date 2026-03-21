def is_prime(number: int) -> bool:
    """
    Determine whether a given number is a prime number.

    Args:
        number (int): The number to evaluate.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Exclude even numbers greater than 2
    if number % 2 == 0:
        return False

    # Check divisibility from 3 up to the square root of the number
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True
