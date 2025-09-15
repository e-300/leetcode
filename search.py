from collections import deque

"""
Find the shortest path from start to target using BFS

Args:
    graph: Dictionary representing adjacency list
    start: Starting node
    target: Target node

Returns:
    List representing the shortest path, or None if no path exists
"""


def bfs_shortest_path(graph, start, target):

    if start == target:
        return start
    
    deque(start)
    visited = {start}
    parent = {}



    while deque:
        current = deque.pop(0)

        for neighbor in graph[current]:
            deque.append(neighbor)

            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current






    # TODO: Implement BFS here
    # Hint: Use a queue, visited set, and parent dictionary
    pass

# Graph representation as adjacency list
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F', 'G'],
    'F': ['C', 'E'],
    'G': ['E']
}

# Test the function
if __name__ == "__main__":
    result = bfs_shortest_path(graph, 'A', 'G')
    print(f"Shortest path from A to G: {result}")
    
    # Additional test cases
    print(f"Path from A to F: {bfs_shortest_path(graph, 'A', 'F')}")
    print(f"Path from C to D: {bfs_shortest_path(graph, 'C', 'D')}")
















# SOLUTION (uncomment to see the answer):
"""
def bfs_shortest_path(graph, start, target):
    if start == target:
        return [start]
    
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
                
                if neighbor == target:
                    # Reconstruct path
                    path = []
                    node = target
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]  # Reverse to get start->target
    
    return None  # No path found
"""