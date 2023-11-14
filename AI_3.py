# Pranjali Shinde(TA63) - Experiment 3: N queen
def solve_n_queens(n):
    def is_safe(board, row, col, n):
        for i in range(col):
            if board[row][i] == 1:
                return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
        return True

    def solve(board, col):
        if col == n:
            result.append(
                ["".join(["Q" if board[i][j] == 1 else "." for j in range(n)]) for i in range(n)])
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    result = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return result


def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    n = int(input("Enter the value of N for the N-Queens problem: "))
    solutions = solve_n_queens(n)
    print(
        f"Found {len(solutions)} solution(s) for N-Queens problem with N = {n}:\n")
    print_solutions(solutions)
