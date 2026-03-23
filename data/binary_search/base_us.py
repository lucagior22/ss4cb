def binary_search(sorted_numbers: list[int], target_value: int) -> int:
    """
    Perform binary search on a sorted list.

    Args:
        sorted_numbers (list[int]): A list of integers sorted in ascending order.
        target_value (int): The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """

    # Initialize the boundaries of the search space
    left_index = 0
    right_index = len(sorted_numbers) - 1

    # Continue searching while the search space is valid
    while left_index <= right_index:

        # Find the middle index of the current search space
        middle_index = (left_index + right_index) // 2
        middle_value = sorted_numbers[middle_index]

        # Case 1: Target found
        if middle_value == target_value:
            return middle_index

        # Case 2: Target is smaller → search in the left half
        elif target_value < middle_value:
            right_index = middle_index - 1

        # Case 3: Target is larger → search in the right half
        else:
            left_index = middle_index + 1

    # Target not found
    return -1