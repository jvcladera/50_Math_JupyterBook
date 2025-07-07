# 19 Calculus

**Calculus** is the mathematical study of **change**. It provides tools to understand how quantities vary and accumulate, enabling us to model and solve problems in physics, engineering, economics, and many other fields. Developed independently by **Isaac Newton** and **Gottfried Leibniz** in the *17th century*, calculus remains one of the most powerful intellectual achievements in human history.

## Differential Calculus: The Study of Rates of Change

**Differential calculus** focuses on the concept of the **derivative**, which measures the instantaneous rate at which a function changes. Geometrically, the derivative at a point represents the slope of the tangent line to the function's graph at that point.

Key concepts in differential calculus:
*   **Limits:** The foundation of calculus, describing the behavior of a function as its input approaches a certain value.
*   **Derivatives:** Used to find velocities, accelerations, and optimization problems (finding maximum or minimum values).

## Integral Calculus: The Study of Accumulation

**Integral calculus** deals with the concept of the **integral**, which can be thought of as the process of summing up infinitesimally small quantities. Geometrically, the definite integral of a function over an interval represents the area under the curve of the function.

Key concepts in integral calculus:
*   **Antiderivatives:** The reverse process of differentiation.
*   **Definite Integrals:** Used to calculate areas, volumes, and total changes over an interval.

## The Fundamental Theorem of Calculus

The **Fundamental Theorem of Calculus** establishes a profound connection between differential and integral calculus. It states that differentiation and integration are inverse operations, meaning that if a function is integrated and then differentiated, the original function is recovered (and vice-versa). This theorem greatly simplifies the calculation of definite integrals.

## Applications of Calculus

Calculus is indispensable in virtually every scientific and engineering discipline:
*   **Physics:** Describing motion, forces, and energy.
*   **Engineering:** Designing structures, optimizing processes, and analyzing systems.
*   **Economics:** Modeling economic growth, optimizing profits, and analyzing market trends.
*   **Biology:** Modeling population growth and spread of diseases.

# the condensed idea

# The mathematics of change and accumulation

```python
# Python demo: Numerical Differentiation and Integration

# We'll use a simple function: f(x) = x^2

# Numerical Differentiation (approximating the derivative)
def numerical_derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

def f_x_squared(x):
    return x**2

# Example: Derivative of x^2 at x=3 (should be 2*3 = 6)
x_val = 3
derivative_at_x = numerical_derivative(f_x_squared, x_val)
print(f"Numerical derivative of x^2 at x={x_val}: {derivative_at_x}")

# Numerical Integration (approximating the area under the curve using Riemann sum)
def numerical_integration(f, a, b, n_rectangles):
    delta_x = (b - a) / n_rectangles
    total_area = 0
    for i in range(n_rectangles):
        x_i = a + i * delta_x
        total_area += f(x_i) * delta_x
    return total_area

# Example: Integral of x^2 from 0 to 3 (should be x^3/3 from 0 to 3 = 27/3 = 9)
a_val = 0
b_val = 3
num_rectangles = 1000
integral_result = numerical_integration(f_x_squared, a_val, b_val, num_rectangles)
print(f"Numerical integral of x^2 from {a_val} to {b_val} with {num_rectangles} rectangles: {integral_result}")
```