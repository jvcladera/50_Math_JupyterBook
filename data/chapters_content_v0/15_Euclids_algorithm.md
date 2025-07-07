## 15 Euclid’s algorithm

**Euclid’s algorithm is one of the oldest and most fundamental algorithms in mathematics. It provides an efficient method for computing the greatest common divisor (GCD) of two integers, a concept that has applications ranging from simplifying fractions to modern cryptography.**

### The Algorithm

Euclid’s algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. This process is repeated until one of the numbers becomes zero, and the other number is the GCD.

A more efficient version uses the remainder of the division. The GCD of two numbers also divides their remainder when one is divided by the other. This allows for a faster reduction of the numbers.

For example, to find the GCD of 252 and 105:
1.  Divide 252 by 105: 252 = 2 × 105 + 42
2.  Now find the GCD of 105 and 42: 105 = 2 × 42 + 21
3.  Now find the GCD of 42 and 21: 42 = 2 × 21 + 0

The last non-zero remainder is 21, so GCD(252, 105) = 21.

### Applications

Euclid’s algorithm has numerous applications:
*   **Simplifying Fractions:** To simplify a fraction like 105/252, you can divide both the numerator and the denominator by their GCD (21), resulting in 5/12.
*   **Cryptography:** It is a crucial component in public-key cryptography systems like RSA, where it's used in the extended Euclidean algorithm to find modular inverses.
*   **Diophantine Equations:** It can be used to solve linear Diophantine equations (equations where only integer solutions are sought).

### History

The algorithm is named after the ancient Greek mathematician Euclid, who described it in his work "Elements" around 300 BC. It is one of the earliest examples of an algorithm that has been formally described and widely used.

# the condensed idea

# Finding common ground

```python
# Python demo: Euclid's Algorithm for GCD

def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 252
num2 = 105
gcd_result = euclidean_algorithm(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")

num3 = 48
num4 = 18
gcd_result2 = euclidean_algorithm(num3, num4)
print(f"The GCD of {num3} and {num4} is: {gcd_result2}")

# Application: Simplifying a fraction
numerator = 105
denominator = 252
common_divisor = euclidean_algorithm(numerator, denominator)
simplified_numerator = numerator // common_divisor
simplified_denominator = denominator // common_divisor
print(f"\nThe fraction {numerator}/{denominator} simplified is: {simplified_numerator}/{simplified_denominator}")
```