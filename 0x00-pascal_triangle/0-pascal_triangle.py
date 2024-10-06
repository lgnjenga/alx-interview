def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n: An integer representing the number of rows in the triangle.

    Returns:
        A list of lists of integers representing the Pascal's triangle of n,
        or an empty list if n <= 0.
    """

    triangle = []
    if n <= 0:
        return triangle

    # First row is always [1]
    triangle.append([1])

    # Iterate for subsequent rows (starting from row 2)
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        # Fill the middle elements using the sum of elements above
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # Last element is always 1
        row.append(1)
        triangle.append(row)

    return triangle
