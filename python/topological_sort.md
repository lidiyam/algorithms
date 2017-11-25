## Topological sort 

A topological sort of a directed graph is a way of ordering the list of nodes such that if (a, b)
is an edge in the graph then a will appear before b in the list. 

If a graph has cycles or is not directed, then there is **no** topological sort.

### Constructing a topological sort

1. Identify all nodes with no incoming edges and add them to the result
2. Remove identified nodes from the graph, repeat step 1 until the graph is epmty
