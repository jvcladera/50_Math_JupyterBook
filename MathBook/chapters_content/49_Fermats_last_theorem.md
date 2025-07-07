# 49 Fermat’s last theorem

**Fermat's Last Theorem** is one of the most famous theorems in the history of mathematics. It states that no three positive integers *a, b*, and *c* can satisfy the equation *aⁿ + bⁿ = cⁿ* for any integer value of *n* greater than *2*. This seemingly simple statement, scribbled in the margin of a book by **Pierre de Fermat** in the *17th century*, baffled mathematicians for over *350 years* before finally being proven in *1994*.

## The Theorem

**Pierre de Fermat**, a French mathematician, wrote in the margin of his copy of **Diophantus's** *Arithmetica* around *1637* that he had a truly marvelous proof of this proposition, but the margin was too narrow to contain it. The theorem states:

There are no positive integers *a, b*, and *c* such that *aⁿ + bⁿ = cⁿ* for any integer *n > 2*.

For *n = 1*, *a + b = c* has infinite integer solutions (e.g., *1+2=3*).
For *n = 2*, *a² + b² = c²* has infinite integer solutions, known as **Pythagorean triples** (e.g., *3²+4²=5²*).

## The Long Quest for a Proof

For centuries, mathematicians attempted to prove or disprove Fermat's Last Theorem. Many famous mathematicians, including **Euler, Sophie Germain**, and **Kummer**, made significant contributions, proving the theorem for specific values of *n* or classes of numbers. However, a general proof remained elusive.

## Andrew Wiles's Proof

The theorem was finally proven by British mathematician **Andrew Wiles** in *1994*, building on the work of many others, particularly the **Taniyama-Shimura-Weil conjecture** (now the **modularity theorem**). Wiles's proof was a monumental achievement, spanning over *100 pages* and using highly advanced mathematical concepts that were not available in Fermat's time. His proof involved connecting **elliptic curves** and **modular forms**, demonstrating the deep interconnectedness of different areas of mathematics.

## Significance

Fermat's Last Theorem is significant not just for its solution, but for the vast amount of mathematics that was developed in the attempts to prove it. These developments led to new fields and theories that have had far-reaching impacts on modern mathematics.

# the condensed idea

# The margin that baffled the world

```python
# Python demo: Checking Fermat's Last Theorem for small exponents

def check_fermat_theorem(limit, exponent):
    solutions_found = []
    print(f"Checking a^n + b^n = c^n for n = {exponent} up to limit = {limit}")
    if exponent <= 2:
        print("Fermat's Last Theorem applies for n > 2. For n=1 or n=2, solutions exist.")
        return

    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            # Calculate c_n_power = a^n + b^n
            c_n_power = (a**exponent) + (b**exponent)
            
            # Check if c_n_power is a perfect nth power of an integer
            # We can find the nth root and check if it's an integer
            c_candidate = round(c_n_power**(1/exponent))
            
            if (c_candidate**exponent) == c_n_power:
                # If a solution is found, it contradicts Fermat's Last Theorem
                # (which is proven true, so this code should not find solutions for n > 2)
                solutions_found.append((a, b, c_candidate))
                
    if solutions_found:
        print(f"Found unexpected solutions for n={exponent}: {solutions_found}")
        print("This indicates a logical error in the code or an misunderstanding of the theorem.")
    else:
        print(f"No integer solutions found for a^n + b^n = c^n for n = {exponent} within the given limit.")
        print("This is consistent with Fermat's Last Theorem.")

# Example usage:
# For n=3, no solutions should be found
check_fermat_theorem(limit=20, exponent=3)

# For n=2, solutions (Pythagorean triples) should be found
print("\n--- Checking for n=2 (Pythagorean Triples) ---")
check_fermat_theorem(limit=10, exponent=2)
```
