def f(lst, t):
    i = 0
    while i < len(lst):
        if lst[i] == t:
            return i
        i += 1
    return -1