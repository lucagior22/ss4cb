def cocktail_shaker_sort(array: list[int], ascending: bool = True) -> list[int]:
    """
    Sorts a list of integers using the Cocktail Shaker Sort algorithm.

    Cocktail Shaker Sort is a variation of Bubble Sort that traverses the list
    in both directions alternately, improving performance slightly by moving
    both the largest and smallest elements toward their correct positions
    in each full pass.
    

    This function does not modify the original list; instead, it returns a
    new sorted list.

    Args:
        array (list[int]): The list of integers to be sorted.
        ascending (bool, optional): If True, sorts the list in ascending order.
            If False, sorts the list in descending order. Defaults to True.

    Returns:
        list[int]: A new list containing the sorted elements.
    """

    # Create a copy of the input list to avoid modifying the original
    arr = array.copy()

    # Initialize boundaries for the unsorted section of the list
    start = 0
    end = len(arr) - 1

    # Flag to track if any swaps were made in a pass
    swapped = True

    while swapped:
        swapped = False

        # Forward pass: move the largest (or smallest) element to the end
        for i in range(start, end):
            if (arr[i] > arr[i + 1] and ascending) or \
               (arr[i] < arr[i + 1] and not ascending):
                # Swap adjacent elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

        # Reduce the upper bound since the last element is now correctly placed
        end -= 1

        swapped = False

        # Backward pass: move the smallest (or largest) element to the start
        for i in range(end, start, -1):
            if (arr[i] < arr[i - 1] and ascending) or \
               (arr[i] > arr[i - 1] and not ascending):
                # Swap adjacent elements if they are in the wrong order
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Increase the lower bound since the first element is now correctly placed
        start += 1

    return arr
