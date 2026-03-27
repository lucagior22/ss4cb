def prime_factorization(n: int) -> list[int]:
    """
    Compute the prime factorization of a given integer.

    This function returns a list containing the prime factors of the
    integer `n`. Each factor appears in the list as many times as it
    divides `n` (i.e., multiplicity is preserved).

    If `n` is less than 2, the function returns an empty list.

    Args:
        n (int): The integer to factorize.

    Returns:
        list[int]: A list of prime factors of `n`.
    """
    factors = []

    # Return empty list for invalid inputs
    if n < 2:
        return factors

    # Step 1: Extract all factors of 2 (the only even prime)
    while n % 2 == 0:
        factors.append(2)
        n //= 2  # Reduce n by dividing by 2

    # Step 2: Check for odd factors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        # While divisor divides n, add it and reduce n
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2  # Only check odd numbers

    # Step 3: If remaining n is greater than 1, it is a prime
    if n > 1:
        factors.append(n)

    return factors
