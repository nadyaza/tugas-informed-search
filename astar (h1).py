from queue import PriorityQueue

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def solve(self):
        queue = PriorityQueue()
        queue.put((self.heuristic(self.start), self.start, 0, None))
        visited = set()

        while not queue.empty():
            _, state, moves, parent = queue.get()

            if state == self.goal:
                path = []
                node = parent
                while node is not None:
                    path.append(node[1])
                    node = node[3]
                path.reverse()
                return path

            visited.add(state)

            for successor in self.get_successors(state):
                if successor not in visited:
                    queue.put((self.heuristic(successor) + moves + 1, successor, moves + 1, (state, successor, moves, parent)))

        return None

    def heuristic(self, state):
        misplaced = 0
        for i in range(len(state)):
            if state[i] != self.goal[i]:
                misplaced += 1
        return misplaced

    def get_successors(self, state):
        successors = []
        blank = state.index(0)
        if blank % 3 > 0:
            successors.append(self.swap(state, blank, blank - 1))
        if blank % 3 < 2:
            successors.append(self.swap(state, blank, blank + 1))
        if blank // 3 > 0:
            successors.append(self.swap(state, blank, blank - 3))
        if blank // 3 < 2:
            successors.append(self.swap(state, blank, blank + 3))
        return successors

    def swap(self, state, i, j):
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return tuple(state)

start = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)

puzzle = Puzzle(start, goal)
path = puzzle.solve()

if path is not None:
    print("Path found:")
    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("Path not found.")

if path is not None:
    for state in path:
        misplaced = 0
        for i in range(len(state)):
            if state[i] != goal[i]:
                misplaced += 1
        print("Misplaced tiles:", misplaced)
