# 20 Constructions

**Geometric constructions**, particularly those using only a **compass** and **straightedge**, have been a cornerstone of geometry since ancient Greece. These fundamental tools allow us to create precise geometric figures and explore the relationships between points, lines, and circles, laying the groundwork for more complex mathematical ideas.

## The Rules of Construction

In classical **Euclidean geometry**, constructions are limited to two idealized tools:

*   **Compass:** Used to draw circles with a given center and radius, and to transfer lengths.
*   **Straightedge:** Used to draw straight lines through two given points. It has no markings for measurement.

These seemingly simple tools can be used to perform a surprising variety of constructions, from bisecting angles to constructing regular polygons.

## Basic Constructions

Some fundamental constructions include:

*   **Copying a Line Segment:** Creating a new line segment of the same length as a given one.
*   **Copying an Angle:** Creating a new angle with the same measure as a given one.
*   **Bisecting a Line Segment:** Dividing a line segment into two equal parts.
*   **Bisecting an Angle:** Dividing an angle into two equal angles.
*   **Constructing a Perpendicular Line:** Drawing a line perpendicular to a given line through a given point.
*   **Constructing a Parallel Line:** Drawing a line parallel to a given line through a given point.

## Constructible Numbers

The concept of **constructible numbers** is closely tied to geometric constructions. A number is constructible if it can be represented as the length of a line segment that can be constructed from a given unit length using only a compass and straightedge. For example, integers, rational numbers, and square roots of constructible numbers are constructible.

## Famous Unsolvable Problems

For centuries, mathematicians attempted to solve three famous problems using only compass and straightedge, which were later proven to be impossible:

*   **Squaring the Circle:** Constructing a square with the same area as a given circle (related to the transcendence of **π**).
*   **Doubling the Cube:** Constructing a cube with twice the volume of a given cube.
*   **Trisecting an Angle:** Dividing an arbitrary angle into three equal parts.

These impossibilities were proven using advanced algebraic techniques, demonstrating the limitations of classical geometric tools and highlighting the power of connecting geometry with algebra.

# the condensed idea

# Building with lines and circles

```python
# Python demo: Conceptual Geometric Constructions

# This script conceptually demonstrates geometric constructions.
# For actual visual output, a graphics library like matplotlib or turtle would be needed.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(Center={self.center}, Radius={self.radius})"

# Conceptual function to bisect a line segment (midpoint)
def bisect_line_segment(p1, p2):
    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2
    return Point(mid_x, mid_y)

# Conceptual function to find intersection of two circles
def intersect_circles(circle1, circle2):
    # This is a simplified conceptual representation.
    # Actual intersection calculation is complex and involves solving equations.
    print(f"\nConceptually intersecting {circle1} and {circle2}")
    # In a real scenario, this would return 0, 1, or 2 intersection points
    return "Intersection points (calculation omitted for simplicity)"

# Example usage:
p_a = Point(0, 0)
p_b = Point(5, 0)

midpoint_ab = bisect_line_segment(p_a, p_b)
print(f"Midpoint of line segment from {p_a} to {p_b}: {midpoint_ab}")

circle1 = Circle(Point(0, 0), 5)
circle2 = Circle(Point(3, 0), 4)
intersect_circles(circle1, circle2)
```
```