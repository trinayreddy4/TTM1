from queue import PriorityQueue
class PuzzleState:
    def _init_(self, puzzle, cost, heuristic):
        self.puzzle = puzzle
        self.cost = cost
        self.heuristic = heuristic
    def _lt_(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
def h(state, goal):
    # Heuristic function (Manhattan distance)
    return sum(abs(state.puzzle[i] // 4 - i // 4) + abs(state.puzzle[i] % 4 - i % 4) for i in range(16) if state.puzzle[i] != 0)
def astar(initial, goal):
    visited = set()
    pq = PriorityQueue()
    start_state = PuzzleState(initial, 0, h(PuzzleState(initial, 0, 0), goal))
    pq.put(start_state)
    while not pq.empty():
        current_state = pq.get()
        if current_state.puzzle == goal:
            return current_state.puzzle
        if tuple(current_state.puzzle) not in visited:
            visited.add(tuple(current_state.puzzle))
            for neighbor in generate_neighbors(current_state.puzzle):
                new_cost = current_state.cost + 1
                new_state = PuzzleState(neighbor, new_cost, h(PuzzleState(neighbor, new_cost, 0), goal))
                pq.put(new_state)
    return None
def generate_neighbors(puzzle):
    empty_index = puzzle.index(0)
    neighbors = []
    for move in [-4, 4, -1, 1]:
        new_index = empty_index + move
        if 0 <= new_index < 16 and (move == 1 or move == -1 or move == 4 or move == -4):
            new_puzzle = list(puzzle)
            new_puzzle[empty_index], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[empty_index]
            neighbors.append(new_puzzle)
    return neighbors
def print_puzzle(puzzle):
    for i in range(0, 16, 4):
        print(puzzle[i:i+4])
# Example usage:
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
result = astar(initial_state, goal_state)
if result:
    print("Solution found:")
    print_puzzle(result)
else:
    print("No solution found.")