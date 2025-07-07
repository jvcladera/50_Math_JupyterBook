## 30 The four-colour problem

**The Four-Colour Problem is one of the most famous and historically significant problems in mathematics. It states that any planar map (a map drawn on a flat surface) can be coloured using no more than four colours, such that no two adjacent regions (sharing a common border, not just a point) have the same colour. This seemingly simple problem remained unsolved for over a century and its eventual proof marked a controversial milestone in mathematical history.**

### The Problem's Origins

The problem was first posed in 1852 by Francis Guthrie, a student at University College London, who noticed that he only needed four colours to colour a map of the counties of England. He asked his brother, who was a mathematics student, about it, and the question eventually made its way to Augustus De Morgan, a prominent mathematician.

### Attempts at Proof

Many mathematicians attempted to prove the Four-Colour Theorem over the years, and several incorrect proofs were published. The most famous incorrect proof was by Alfred Kempe in 1879, which stood for 11 years before a flaw was found by Percy Heawood. Heawood's work, however, did prove that five colours are sufficient (the Five-Colour Theorem).

### The Computer-Assisted Proof

The Four-Colour Theorem was finally proven in 1976 by Kenneth Appel and Wolfgang Haken of the University of Illinois. Their proof was groundbreaking and controversial because it relied heavily on computer assistance. They reduced the infinite number of possible maps to a finite number of configurations (1,936 configurations, later reduced to 1,476), which were then checked by a computer. This was the first major mathematical theorem to be proven with significant computer aid, sparking debates about the nature of mathematical proof.

### Graph Theory Connection

The Four-Colour Problem can be translated into a problem in graph theory. Each region on the map can be represented as a vertex, and an edge connects two vertices if their corresponding regions share a border. The problem then becomes: can the vertices of any planar graph be coloured with at most four colours such that no two adjacent vertices have the same colour?

### Significance

Despite the controversy surrounding its proof, the Four-Colour Theorem is a significant result in graph theory and topology. It demonstrated the power of computational methods in mathematics and opened new avenues for research in algorithmic proofs and the intersection of mathematics and computer science.

# the condensed idea

# Four colours are enough

```python
# Python demo: Conceptual Graph Coloring (simplified)

# This is a conceptual example to illustrate the idea of graph coloring,
# which is at the heart of the Four-Colour Problem. Actual map coloring
# algorithms are much more complex and involve graph theory algorithms.

def color_graph_conceptual(graph_adj_list, colors):
    # graph_adj_list: A dictionary representing the graph (adjacency list)
    # colors: A list of available colors

    node_colors = {}
    for node in graph_adj_list:
        available_colors = set(colors)
        # Remove colors used by neighbors
        for neighbor in graph_adj_list[node]:
            if neighbor in node_colors:
                if node_colors[neighbor] in available_colors:
                    available_colors.remove(node_colors[neighbor])
        
        if not available_colors:
            print(f"Could not color node {node} with available colors. More colors might be needed.")
            node_colors[node] = "Uncolored"
        else:
            # Assign the first available color
            node_colors[node] = sorted(list(available_colors))[0]
    return node_colors

# Example Graph (simplified map: A-B, A-C, B-C, B-D, C-D)
# This is a planar graph, so it should be 4-colorable.
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

available_colors = ['Red', 'Green', 'Blue', 'Yellow']

colored_map = color_graph_conceptual(example_graph, available_colors)

print("Conceptual Map Coloring Result:")
for node, color in colored_map.items():
    print(f"Region {node}: {color}")

# Note: This is a greedy coloring algorithm and does not guarantee
# finding a minimal coloring or proving the 4-color theorem.
# It simply demonstrates the concept of assigning colors to nodes
# such that adjacent nodes have different colors.
```