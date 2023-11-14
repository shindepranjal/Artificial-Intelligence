# Pranjali Shinde(TA63) - Experiment 2: 8 Puzzle Game Using A star Algorithm

from heapq import heappush, heappop
import copy

n = 3

rows = [1, 0, -1, 0]
cols = [0, -1, 0, 1]

# Priority Queue


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap

# Node class


class Node:
    def __init__(self, parent, state, empty_pos, cost, level):
        self.parent = parent
        self.state = state
        self.empty_pos = empty_pos
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost

# Calculate the Manhattan distance heuristic


def manhattan_distance(state, goal):
    distance = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, n)
                distance += abs(x - i) + abs(y - j)
    return distance

# Generate new nodes by moving the empty tile


def generate_new_nodes(node, goal):
    new_nodes = []
    x, y = node.empty_pos
    for dx, dy in zip(rows, cols):
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < n and 0 <= new_y < n:
            new_state = copy.deepcopy(node.state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            new_empty_pos = (new_x, new_y)
            cost = manhattan_distance(new_state, goal) + node.level + 1
            new_nodes.append(
                Node(node, new_state, new_empty_pos, cost, node.level + 1))
    return new_nodes

# Print the path from the initial state to the goal state


def print_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    for state in path:
        for row in state:
            print(" ".join(map(str, row)))
        print()

# Solve the 8-puzzle problem using A* with Branch and Bound


def solve_8_puzzle(initial, goal):
    start = Node(None, initial, (0, 0), manhattan_distance(initial, goal), 0)
    open_list = PriorityQueue()
    open_list.push(start)

    while not open_list.empty():
        current_node = open_list.pop()

        if current_node.state == goal:
            print("Path to the goal state:")
            print_path(current_node)
            return

        new_nodes = generate_new_nodes(current_node, goal)
        for new_node in new_nodes:
            open_list.push(new_node)


# Example initial and goal states
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Solve the 8-puzzle problem
print("Solving the 8-puzzle problem:")
solve_8_puzzle(initial_state, goal_state)
