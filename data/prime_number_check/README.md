# Algorithm name
Prime Number Check

## Author
Joaquin Bogado (2026-03-21)

## Algorithm description
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. This algorithm determines whether a given integer is prime by first handling simple edge cases (numbers less than or equal to 1, and even numbers). It then checks for divisibility only up to the square root of the number, reducing the number of necessary operations. By iterating through odd divisors only, the algorithm improves efficiency compared to naive approaches.

## Model used to create the base code
gpt-5.3

### Prompt
```
Write a functions that receives a number `number` and returns True if the number is prime and False if it is not.
```

## Obfuscated version
none

