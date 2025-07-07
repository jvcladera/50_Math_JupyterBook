## 23 Topology

**Topology is a branch of mathematics concerned with the properties of geometric objects that are preserved under continuous deformations, such as stretching, twisting, crumpling, and bending, but not tearing or gluing. It's often called "rubber sheet geometry" because it studies properties that remain unchanged even if the object is made of a flexible material.**

### What Topology Studies

Topology focuses on properties like:

*   **Connectedness:** Whether an object is in one piece or multiple pieces.
*   **Compactness:** Roughly, whether an object can be contained within a finite space.
*   **Orientability:** Whether an object has a consistent "inside" and "outside" (e.g., a Möbius strip is non-orientable).
*   **Number of Holes:** A key topological invariant. A donut (torus) has one hole, a sphere has zero.

### Topological Equivalence

Two objects are topologically equivalent if one can be continuously deformed into the other without cutting or gluing. For example, a coffee cup with a single handle is topologically equivalent to a donut, because you can stretch and deform the clay of one into the other without breaking it or adding new holes.

### Famous Topological Objects

*   **Möbius Strip:** A surface with only one side and one boundary component. You can create one by taking a strip of paper, giving one end a half-twist, and then joining the ends.
*   **Klein Bottle:** A non-orientable surface with no distinct inside or outside, and no boundary. It's a 3D analogue of the Möbius strip, but it cannot be fully realized in three-dimensional Euclidean space without self-intersection.
*   **Torus:** The shape of a donut or an inner tube, characterized by having one hole.

### Applications of Topology

Topology, despite its abstract nature, has practical applications in various fields:

*   **Knot Theory:** A subfield of topology that studies mathematical knots, with applications in DNA research and quantum physics.
*   **Computer Graphics:** Used in mesh simplification and shape analysis.
*   **Robotics:** Path planning and motion control.
*   **Cosmology:** Exploring the possible shapes of the universe.
*   **Data Analysis:** Topological data analysis (TDA) is a new field that uses topological concepts to find structures in complex datasets.

# the condensed idea

# Rubber sheet geometry

```python
# Python demo: Conceptual Topological Transformation

# This example conceptually demonstrates how a shape can be deformed
# while preserving its topological properties (e.g., number of holes).
# Actual visualization would require a graphics library.

class Shape:
    def __init__(self, name, num_holes):
        self.name = name
        self.num_holes = num_holes

    def __repr__(self):
        return f"Shape('{self.name}', Holes={self.num_holes})"

    def deform(self, new_name):
        # In topology, continuous deformation doesn't change the number of holes
        print(f"Deforming {self.name} into a {new_name}...")
        self.name = new_name
        print(f"Result: {self}")

# Example usage:

# A donut (torus) has one hole
donut = Shape("Donut", 1)
print(donut)

# A coffee cup with one handle is topologically equivalent to a donut
coffee_cup = Shape("Coffee Cup with Handle", 1)
print(coffee_cup)

# Deform the coffee cup into a donut (conceptually)
coffee_cup.deform("Donut")

# A sphere has no holes
sphere = Shape("Sphere", 0)
print(sphere)

# A cube is topologically equivalent to a sphere
cube = Shape("Cube", 0)
print(cube)

# Deform the cube into a sphere (conceptually)
cube.deform("Sphere")

# This demonstrates that the number of holes (a topological invariant)
# remains the same despite the change in geometric shape.
```