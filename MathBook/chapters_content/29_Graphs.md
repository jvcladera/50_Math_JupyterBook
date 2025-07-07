# 29 Graphs

**Graph theory** is a branch of mathematics that studies **graphs**, which are mathematical structures used to model pairwise relations between objects. A graph consists of a set of **vertices** (or **nodes**) and a set of **edges** (or **links**) that connect pairs of vertices. Graphs are incredibly versatile and are used to represent a vast array of real-world systems, from social networks to transportation routes and computer networks.

## Basic Concepts

*   **Vertex (Node):** A fundamental unit of a graph, representing an object or entity.
*   **Edge (Link):** A connection between two vertices, representing a relationship or interaction.
*   **Directed Graph (Digraph):** Edges have a direction, indicating a one-way relationship (e.g., a one-way street).
*   **Undirected Graph:** Edges have no direction, indicating a two-way relationship (e.g., a friendship on a social network).
*   **Weighted Graph:** Edges have associated numerical values (weights), representing costs, distances, or capacities.
*   **Path:** A sequence of distinct vertices connected by edges.
*   **Cycle:** A path that starts and ends at the same vertex.

## Types of Graphs

*   **Simple Graph:** No loops (edges connecting a vertex to itself) and no multiple edges between the same pair of vertices.
*   **Complete Graph:** Every pair of distinct vertices is connected by a unique edge.
*   **Tree:** A connected undirected graph with no cycles.
*   **Bipartite Graph:** Vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to one in the other.

## Graph Traversal Algorithms

*   **Breadth-First Search (BFS):** Explores a graph level by level, useful for finding the shortest path in an unweighted graph.
*   **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking, useful for finding connected components or cycles.

## Famous Graph Problems

*   **The Seven Bridges of Königsberg:** A historical problem that led to the birth of graph theory, asking if it was possible to walk through the city crossing each of its seven bridges exactly once.
*   **Traveling Salesperson Problem (TSP):** Finding the shortest possible route that visits each city exactly once and returns to the origin city.
*   **Minimum Spanning Tree (MST):** Finding a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

## Applications of Graph Theory

Graph theory is a powerful tool with applications in:

*   **Computer Science:** Network design, algorithms (e.g., shortest path, sorting), data structures.
*   **Social Networks:** Analyzing relationships, influence, and community detection.
*   **Logistics and Transportation:** Route optimization, traffic flow analysis.
*   **Biology:** Modeling biological networks (e.g., protein-protein interaction networks).
*   **Operations Research:** Scheduling, resource allocation.

# the condensed idea

# Connecting the dots

```python
# Python demo: Representing and traversing a simple graph

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) # For undirected graph

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        bfs_path = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                bfs_path.append(vertex)
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return bfs_path

    def dfs(self, start_node, visited=None, dfs_path=None):
        if visited is None:
            visited = set()
        if dfs_path is None:
            dfs_path = []

        visited.add(start_node)
        dfs_path.append(start_node)

        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, dfs_path)
        return dfs_path

# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'E')
g.add_edge('D', 'F')

print("Graph representation:", g.graph)

bfs_result = g.bfs('A')
print(f"BFS traversal from A: {bfs_result}")

dfs_result = g.dfs('A')
print(f"DFS traversal from A: {dfs_result}")
```