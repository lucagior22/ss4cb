def levenshtein_distance(origin: str, end: str) -> int:
    """
    Compute the Levenshtein distance between two strings.

    The Levenshtein distance is defined as the minimum number of
    single-character edits (insertions, deletions, or substitutions)
    required to change one string into another.

    This implementation uses dynamic programming to build a matrix
    of distances between all prefixes of the two strings.

    Args:
        origin (str): The source string.
        end (str): The target string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """

    # Get lengths of both strings
    len_origin = len(origin)
    len_end = len(end)

    # Create a (len_origin + 1) x (len_end + 1) matrix
    # dp[i][j] will hold the distance between
    # origin[:i] and end[:j]
    dp = [[0 for _ in range(len_end + 1)] for _ in range(len_origin + 1)]

    # Initialize the first column (transform origin -> empty string)
    for i in range(len_origin + 1):
        dp[i][0] = i  # i deletions

    # Initialize the first row (transform empty string -> end)
    for j in range(len_end + 1):
        dp[0][j] = j  # j insertions

    # Fill the matrix
    for i in range(1, len_origin + 1):
        for j in range(1, len_end + 1):
            # If characters match, no operation is needed
            if origin[i - 1] == end[j - 1]:
                cost = 0
            else:
                cost = 1

            # Compute minimum of:
            # - Deletion
            # - Insertion
            # - Substitution
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )

    # The bottom-right cell contains the answer
    return dp[len_origin][len_end]
