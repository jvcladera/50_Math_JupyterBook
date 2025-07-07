# 21 Triangles

**Triangles** are the simplest polygons, yet they are fundamental building blocks in geometry, trigonometry, and many areas of mathematics and engineering. Their rigid structure and predictable properties make them indispensable for understanding shapes, forces, and spatial relationships.

## Types of Triangles

Triangles can be classified based on their side lengths or angles:

**By Side Lengths:**
*   **Equilateral Triangle:** All three sides are equal in length, and all three angles are *60 degrees*.
*   **Isosceles Triangle:** Two sides are equal in length, and the angles opposite those sides are equal.
*   **Scalene Triangle:** All three sides have different lengths, and all three angles are different.

**By Angles:**
*   **Right Triangle:** Has one angle that measures exactly *90 degrees*. The side opposite the right angle is called the **hypotenuse**.
*   **Acute Triangle:** All three angles are acute (less than *90 degrees*).
*   **Obtuse Triangle:** Has one angle that is obtuse (greater than *90 degrees*).

## Properties of Triangles

*   **Angle Sum Property:** The sum of the interior angles of any triangle is always *180 degrees*.
*   **Triangle Inequality Theorem:** The sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
*   **Area of a Triangle:** Can be calculated using various formulas, including:
    *   Base × Height / 2
    *   Heron's formula (using side lengths)
    *   ½ab sin(C) (using two sides and the included angle)

## Pythagoras's Theorem

For right triangles, **Pythagoras's Theorem** states that the square of the length of the hypotenuse (*c*) is equal to the sum of the squares of the lengths of the other two sides (*a* and *b*): *a² + b² = c²*.

## Congruence and Similarity

*   **Congruent Triangles:** Triangles that have the same size and shape. Their corresponding sides and angles are equal.
*   **Similar Triangles:** Triangles that have the same shape but different sizes. Their corresponding angles are equal, and their corresponding sides are proportional.

## Applications

Triangles are used extensively in:
*   **Architecture and Construction:** For structural stability and design.
*   **Navigation and Surveying:** Using triangulation to determine distances and positions.
*   **Computer Graphics:** Representing 3D objects as meshes of triangles.
*   **Physics:** Analyzing forces and vectors.

# the condensed idea

# The fundamental shape

```python
# Python demo: Calculate properties of a right triangle

import math

def calculate_right_triangle_properties(side_a, side_b):
    # Calculate hypotenuse using Pythagorean theorem
    hypotenuse = math.sqrt(side_a**2 + side_b**2)

    # Calculate area
    area = 0.5 * side_a * side_b

    # Calculate angles (in degrees)
    angle_a = math.degrees(math.atan(side_a / side_b))
    angle_b = math.degrees(math.atan(side_b / side_a))
    angle_c = 90 # Right angle

    return {
        "hypotenuse": hypotenuse,
        "area": area,
        "angle_a": angle_a,
        "angle_b": angle_b,
        "angle_c": angle_c
    }

# Example usage:
s_a = 3
s_b = 4
properties = calculate_right_triangle_properties(s_a, s_b)

print(f"Properties of a right triangle with sides {s_a} and {s_b}:")
for key, value in properties.items():
    print(f"  {key.replace('_', ' ').capitalize()}: {value:.2f}")

# Python demo: Check Triangle Inequality Theorem
def check_triangle_inequality(s1, s2, s3):
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
        return True
    else:
        return False

print(f"\nCan sides 3, 4, 5 form a triangle? {check_triangle_inequality(3, 4, 5)}")
print(f"Can sides 1, 2, 5 form a triangle? {check_triangle_inequality(1, 2, 5)}")
```