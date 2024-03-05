from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1

    def dfs(self, start):
        visited = set()

        def dfs_util(node):
            visited.add(node)
            print(node, end=" ")

            for neighbor in range(self.vertices):
                if self.adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        print()

    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in range(self.vertices):
                if self.adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices in the graph: "))
    graph = Graph(vertices)

    while True:
        print("\nGraph Traversal Operations:")
        print("1. Add Edge")
        print("2. Depth-First Search (DFS)")
        print("3. Breadth-First Search (BFS)")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            u, v = map(int, input("Enter edge (u v): ").split())
            graph.add_edge(u, v)
        elif choice == 2:
            start = int(input("Enter starting node for DFS: "))
            print("Depth-First Search:")
            graph.dfs(start)
        elif choice == 3:
            start = int(input("Enter starting node for BFS: "))
            print("Breadth-First Search:")
            graph.bfs(start)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
'''Enter the number of vertices in the graph: 5

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 1
Enter edge (u v): 0 1

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 1
Enter edge (u v): 0 2

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 1
Enter edge (u v): 1 3

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 1
Enter edge (u v): 2 4

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 2
Enter starting node for DFS: 0
Depth-First Search:
0 1 3 2 4 

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 3
Enter starting node for BFS: 0
Breadth-First Search:
0 1 2 3 4 

Graph Traversal Operations:
1. Add Edge
2. Depth-First Search (DFS)
3. Breadth-First Search (BFS)
4. Exit
Enter your choice: 4
Exiting...
'''