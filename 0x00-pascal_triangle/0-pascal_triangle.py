def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to n rows.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
    
    Returns:
        list: A list of lists, where each inner list represents a row of Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle

