# Algorithm name
Binary Search

## Author
Ayrton Alvarez (2026-03-23)

## Algorithm description
Binary search is an efficient algorithm used to find a target value within a sorted list. Instead of scanning each element sequentially, it repeatedly divides the search space in half. The algorithm starts by comparing the target value with the middle element of the list. If they match, the search is complete. If the target is smaller, the algorithm continues searching in the left half; if larger, it searches in the right half. This process repeats until the element is found or the search interval becomes empty. Due to this divide-and-conquer approach, binary search has a time complexity of O(log n), making it significantly faster than linear search for large datasets.

## Model used to create the base code
gpt-5.3

### Prompt
```
Write a function that receives a sorted list of numbers and a target value, and returns the index of the target using the binary search algorithm, or -1 if the target is not found.
```

## Obfuscated version
python-minifier