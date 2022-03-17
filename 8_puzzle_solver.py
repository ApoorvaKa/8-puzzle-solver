import heapq
import copy

MOVES = {"L" : (0,-1), "R" : (0,1), "U" : (1,0), "D" : (-1,0)}
VALID = [0, 1, 2]
COLS = 3

class Node:
    def __init__(self, arrangement, fn = None):
        self.puzzle = arrangement
        self.fn_value = fn

    def make_dict(self):
        coordinate_dict = {}
        for x, row in enumerate(self.puzzle):
            for y, value in enumerate(row):
                coordinate_dict[value] = (x, y)
        return coordinate_dict
    
    def manhattan_distance(self, goal):
        manhattan_distance = 0
        current_vals = self.make_dict()
        goal_vals = goal.make_dict()
        for key in current_vals:
            curr_x, curr_y = current_vals[key]
            goal_x, goal_y = goal_vals[key]
            if key != "0":
                manhattan_distance += abs(goal_x - curr_x) + abs(goal_y - curr_y)
            # print("{} at {},{} distance: {}".format(key, curr_x, curr_y, single_distance))
        print("manhattan distance: ", manhattan_distance)
        return manhattan_distance
    
    def nillson_sequence_score(self, goal):
        pass

class Puzzle:
    def __init__(self, filename):
        self.current = None
        self.goal = None
        self.path_cost = 0
        self.reached = []
        self.frontier = []
        self.get_input(filename)
    
    def try_moves(self):
        row, col = self.current.make_dict()["0"]
        for move in MOVES:
            original = copy.deepcopy(self.current.puzzle)
            if move == "L" and col - 1 in VALID:
                original[row][col], original[row][col - 1] = original[row][col - 1], original[row][col]
            elif move == "R" and col + 1 in VALID:
                original[row][col], original[row][col + 1] = original[row][col + 1], original[row][col]
            elif move == "U" and row + 1 in VALID:
                original[row][col], original[row + 1][col] = original[row + 1][col], original[row][col]
            elif move == "D" and col - 1 in VALID:
                original[row][col], original[row - 1][col] = original[row - 1][col], original[row][col]
            new_node = Node(original, self.current.fn_value + 1)
                
            print(new_node.puzzle)
            

    def get_input(self, filename):
        try:
            file = open(filename, 'r')
        except FileNotFoundError:
            print("{} not found".format(filename))
            return
        
        is_goal = False
        goal = []
        start = []
        for line in file:
            if line == "\n":
                is_goal = True
            else:
                line = line.strip()
                line = line.split(" ")
                if is_goal:
                    goal.append(line)
                else:
                    start.append(line)  
        self.current = Node(start, 0)
        self.goal = Node(goal)

    def a_star(self):
        pass

def main():
    puzz = Puzzle("input_example.txt")
    puzz.current.manhattan_distance(puzz.goal)
    puzz.try_moves()

if __name__ == "__main__":
    main()