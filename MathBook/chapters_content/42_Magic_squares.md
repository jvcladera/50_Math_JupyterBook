# 42 Magic squares

**Magic squares** are square grids where numbers are arranged in such a way that the sum of the numbers in each row, each column, and both main diagonals is the same. These intriguing mathematical puzzles have fascinated people for millennia, appearing in various cultures and holding both mathematical and mystical significance.

## What is a Magic Square?

A magic square of order *n* is a square grid containing *n²* distinct integers, usually from *1* to *n²*, such that the sum of the numbers in each row, each column, and both main diagonals is equal. This constant sum is called the **magic constant** or **magic sum** (*M*).

For a normal magic square (containing integers from *1* to *n²*), the magic constant can be calculated using the formula:

`M = n * (n² + 1) / 2`

For example, for a *3x3* magic square (*n=3*):
`M = 3 * (3² + 1) / 2 = 3 * (9 + 1) / 2 = 3 * 10 / 2 = 15`

## Types of Magic Squares

*   **Normal Magic Squares:** Contain the integers from *1* to *n²*.
*   **Associative (Symmetric) Magic Squares:** In addition to being magic, every pair of numbers symmetrically opposite to the center sums to *n² + 1*.
*   **Pan-diagonal Magic Squares:** The numbers in the broken diagonals (diagonals that wrap around the edges of the square) also sum to the magic constant.

## Construction Methods

Various methods exist for constructing magic squares, depending on their order:

*   **Odd Order Squares (e.g., 3x3, 5x5):** Methods like the "**Siamese method**" or "**de la Loubère method**" are commonly used.
*   **Singly Even Order Squares (e.g., 4x4, 8x8):** Methods like the "**Strachey method**" or "**cross-out method**" are employed.
*   **Doubly Even Order Squares (e.g., 6x6, 10x10):** More complex methods are required.

## History and Significance

Magic squares have a rich history:

*   **Ancient China:** The earliest known magic square, the **Lo Shu Square** (a *3x3* magic square), dates back to ancient China (around *650 BC*).
*   **India and the Middle East:** Magic squares were studied and developed in these regions for centuries.
*   **Europe:** Introduced to Europe in the Middle Ages, they gained popularity during the **Renaissance**, often associated with **astrology** and **alchemy**. **Albrecht Dürer's** engraving "*Melencolia I*" features a famous *4x4* magic square.

Beyond their recreational appeal, magic squares have connections to **number theory, combinatorics**, and even **physics**.

# the condensed idea

# Numbers in harmony

```python
# Python demo: Check if a square is a Magic Square

def is_magic_square(square):
    n = len(square)
    if n == 0:
        return False

    # Calculate the magic constant (sum of the first row)
    magic_sum = sum(square[0])

    # Check row sums
    for row in square:
        if sum(row) != magic_sum:
            return False

    # Check column sums
    for col_idx in range(n):
        col_sum = 0
        for row_idx in range(n):
            col_sum += square[row_idx][col_idx]
        if col_sum != magic_sum:
            return False

    # Check main diagonal sum (top-left to bottom-right)
    diag1_sum = 0
    for i in range(n):
        diag1_sum += square[i][i]
    if diag1_sum != magic_sum:
        return False

    # Check anti-diagonal sum (top-right to bottom-left)
    diag2_sum = 0
    for i in range(n):
        diag2_sum += square[i][n - 1 - i]
    if diag2_sum != magic_sum:
        return False

    # Optional: Check if all numbers from 1 to n*n are present exactly once
    # This is for a "normal" magic square. For general magic squares, this check is not needed.
    # flat_list = [num for row in square for num in row]
    # if sorted(flat_list) != list(range(1, n*n + 1)):
    #     return False

    return True

# Example Magic Square (3x3)
magic_square_3x3 = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

# Example Non-Magic Square
non_magic_square = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Checking Magic Square 3x3:")
for row in magic_square_3x3:
    print(row)
print(f"Is it a magic square? {is_magic_square(magic_square_3x3)}")

print("\nChecking Non-Magic Square:")
for row in non_magic_square:
    print(row)
print(f"Is it a magic square? {is_magic_square(non_magic_square)}")

# Example Magic Square (4x4 - Dürer's Magic Square)
magic_square_4x4 = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]
print("\nChecking Magic Square 4x4 (Dürer's):")
for row in magic_square_4x4:
    print(row)
print(f"Is it a magic square? {is_magic_square(magic_square_4x4)}")
```
```