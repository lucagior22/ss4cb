def linear_search(item_list, target_value):
    """
    Searches for target_value in item_list by checking each element sequentially.
    Returns the index of target_value if found, or -1 if not present.
    """
    current_index = 0
    while current_index < len(item_list):
        current_element = item_list[current_index]
        if current_element == target_value:
            return current_index
        current_index += 1
    return -1