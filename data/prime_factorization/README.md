# Algorithm name
Prime Factorization

## Author
Damián Bicocchi (2026-03-26)

## Algorithm description
Prime factorization is the process of decomposing a positive integer into a product of prime numbers. A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.

The result of prime factorization expresses the original number as a multiplication of primes, which is unique for each number (except for the order of the factors). This process is fundamental in number theory and is commonly used in areas such as cryptography, simplification of fractions, and finding greatest common divisors (GCD) or least common multiples (LCM).

The algorithm typically works by repeatedly dividing the number by the smallest possible prime factor until the remaining value becomes 1.

## Model used to create the base code
GPT-5.3

### Prompt
```
Write a Python 3.12 implementation of algorithm Prime factorization. The function "prime_factorization" receives one argument: "n", which is an int
The function must return a list with the prime factors of n. If n is less than 2 the list should return empty
Requirements
* Provide docstring adjusting to PEP-8 standards
* Do not use libraries
* Provide explanatory english comments
```

## Obfuscated version
manually obfuscated