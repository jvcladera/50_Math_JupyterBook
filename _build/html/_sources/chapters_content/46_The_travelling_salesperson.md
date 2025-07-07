## 46 The travelling salesperson

**The Travelling Salesperson Problem (TSP) is one of the most famous and extensively studied problems in combinatorial optimization. It asks: given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?**

### Problem Definition

*   **Cities (Nodes):** Represented as points in a graph.
*   **Distances (Edges):** The cost or distance of traveling between two cities, forming the edges of the graph.
*   **Goal:** Find a Hamiltonian cycle (a path that visits each node exactly once and returns to the starting node) with the minimum total weight (distance).

### Complexity

The TSP is an NP-hard problem, meaning that there is no known efficient algorithm that can solve it in polynomial time for all instances. As the number of cities increases, the number of possible routes grows factorially, making brute-force enumeration computationally infeasible.

*   For `n` cities, there are `(n-1)!` possible routes (if starting city is fixed).
    *   3 cities: 2! = 2 routes
    *   4 cities: 3! = 6 routes
    *   10 cities: 9! = 362,880 routes
    *   20 cities: 19! ≈ 1.2 x 10^17 routes

### Approaches to Solving TSP

Given its complexity, various approaches are used depending on the size and nature of the problem:

*   **Brute-Force (Exhaustive Search):** Checking every possible route. Only feasible for very small numbers of cities.
*   **Heuristics:** Algorithms that find good, but not necessarily optimal, solutions in a reasonable amount of time. Examples include nearest neighbor, insertion heuristics.
*   **Approximation Algorithms:** Algorithms that guarantee a solution within a certain factor of the optimal solution.
*   **Metaheuristics:** Optimization techniques that guide a search process, such as genetic algorithms, simulated annealing, and ant colony optimization.
*   **Exact Algorithms:** Algorithms that guarantee the optimal solution but are computationally expensive (e.g., branch and bound, cutting plane methods).

### Applications of TSP

The TSP, despite its abstract formulation, has numerous real-world applications:

*   **Logistics and Delivery:** Optimizing delivery routes for packages, mail, and goods.
*   **Vehicle Routing:** Planning routes for fleets of vehicles.
*   **Circuit Board Drilling:** Optimizing the path for drilling holes in circuit boards.
*   **DNA Sequencing:** Reconstructing DNA sequences from fragments.
*   **Computer Chip Manufacturing:** Optimizing the path for laser etching.
*   **Robotics:** Path planning for robots.

# the condensed idea

# The shortest path puzzle

```python
# Python demo: Brute-Force Solution for Traveling Salesperson Problem (TSP)

import itertools
import math

# Define cities and their coordinates (for distance calculation)
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (4, 0),
    'D': (2, 1)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def solve_tsp_brute_force(cities_dict):
    all_cities = list(cities_dict.keys())
    start_city = all_cities[0] # Fix the starting city
    other_cities = all_cities[1:]

    min_distance = float('inf')
    best_path = None

    # Generate all permutations of the other cities
    for permutation in itertools.permutations(other_cities):
        current_path = [start_city] + list(permutation) + [start_city]
        current_distance = 0

        for i in range(len(current_path) - 1):
            current_distance += calculate_distance(current_path[i], current_path[i+1])
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = current_path
            
    return best_path, min_distance

# Example usage:
path, distance = solve_tsp_brute_force(cities)

print("Cities:", cities)
print(f"Shortest path: {path}")
print(f"Total distance: {distance:.2f}")

# Note: This brute-force approach is only feasible for a very small number of cities.
# For larger instances, approximation algorithms or heuristics are used.
```