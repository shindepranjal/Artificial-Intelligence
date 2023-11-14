# Pranjali Shinde(TA63) - Experiment 1: DFS & BFS

from collections import deque


def main():
    numVertices = int(input("Enter the number of vertices: "))
    adjacencyMatrix = [[0] * (numVertices + 1) for _ in range(numVertices + 1)]

    for i in range(1, numVertices + 1):
        for j in range(1, numVertices + 1):
            adjacencyMatrix[i][j] = int(
                input(f"Enter 1 if 'Node {i}' has an edge with 'Node {j}', else enter 0: "))

    while True:
        visited = [0] * (numVertices + 1)

        print("\nMENU")
        print("1. Depth First Search (DFS)")
        print("2. Breadth First Search (BFS)")
        choice = int(input("Enter your choice: "))
        startVertex = int(input("Enter the Source Vertex: "))

        if choice == 1:
            depthFirstSearch(adjacencyMatrix, visited,
                             startVertex, numVertices)
        elif choice == 2:
            breadthFirstSearch(adjacencyMatrix, startVertex, numVertices)

        cont = input("\nDO YOU WANT TO CONTINUE (Y/N)? ").strip().lower()
        if cont != 'y':
            break


def depthFirstSearch(adjacencyMatrix, visited, currentVertex, numVertices):
    print(currentVertex, end=" ")
    visited[currentVertex] = 1
    for i in range(1, numVertices + 1):
        if adjacencyMatrix[currentVertex][i] != 0 and visited[i] == 0:
            depthFirstSearch(adjacencyMatrix, visited, i, numVertices)


def breadthFirstSearch(adjacencyMatrix, startVertex, numVertices):
    visited = [0] * (numVertices + 1)
    vertexQueue = deque([startVertex])
    visited[startVertex] = 1

    while vertexQueue:
        currentVertex = vertexQueue.popleft()
        print(currentVertex, end=" ")
        for i in range(1, numVertices + 1):
            if adjacencyMatrix[currentVertex][i] != 0 and visited[i] == 0:
                visited[i] = 1
                vertexQueue.append(i)


if __name__ == "__main__":
    main()
