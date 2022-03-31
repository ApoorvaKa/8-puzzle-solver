import heapq
import copy

MOVES = {"L" : (0,-1), "R" : (0,1), "U" : (1,0), "D" : (-1,0)}
NILLSON_ORDER = [(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0),(1,1)]
VALID = [0, 1, 2]
COLS = 3

class Node:
    def __init__(self, arrangement, last_move = None, goal_node = None, path_cost = 0):
        self.puzzle = arrangement
        self.path_cost = path_cost
        self.last_move = last_move
        if goal_node != None:
            self.fn_value = path_cost + self.manhattan_distance(goal_node)
            #self.nillson_score(goal_node)
    
    def __str__(self):
        printer = str(self.last_move) +" " + str(self.fn_value) + "\n"

        for row in self.puzzle:
            printer += " ".join(row)
            printer += "\n"
        return printer
    
    def __eq__(self, other = None):
        if other == None:
            return False
        else:
            return self.puzzle == other.puzzle
    
    def __ne__(self, other):
        return not(self == other)
    
    def __lt__(self, other):
        return self.fn_value < other.fn_value

    def make_dict(self):
        # represent board as a dictionary for easier access
        coordinate_dict = {}
        for x, row in enumerate(self.puzzle):
            for y, value in enumerate(row):
                coordinate_dict[value] = (x, y)
        return coordinate_dict
    
    def manhattan_distance(self, goal):
        # calculate the manhattan distance between self Node and goal Node
        manhattan_distance = 0
        current_vals = self.make_dict()
        goal_vals = goal.make_dict()
        for key in current_vals:
            curr_x, curr_y = current_vals[key]
            goal_x, goal_y = goal_vals[key]
            if key != "0":
                manhattan_distance += abs(goal_x - curr_x) + abs(goal_y - curr_y)
            # print("{} at {},{} distance: {}".format(key, curr_x, curr_y, single_distance))
        #print("manhattan distance: ", manhattan_distance)
        return manhattan_distance
    
    def nillson_sequence_score(self, goal):
        nillson_score = 0
        for coord in NILLSON_ORDER:
            print(self.puzzle[coord[0]][coord[1]])
        
        # Check the center tile
        if self.arrangement[1][1] != goal.arrangement[1][1]:
            nillson_score += 1

class Puzzle:
    def __init__(self, input_filename, output_filename):
        self.current = None
        self.goal = None
        self.reached = []
        self.frontier = []
        self.num_nodes = 1 # this is the root node
        self.get_input(input_filename, output_filename)

    def try_moves(self):
        # Try all moves L, R, U, D
        row, col = self.current.make_dict()["0"]
        for move in MOVES:
            new_node = None
            original = copy.deepcopy(self.current.puzzle)
            if move == "L" and col - 1 in VALID:
                original[row][col], original[row][col - 1] = original[row][col - 1], original[row][col]
                new_node = Node(original, move, self.goal, self.current.path_cost + 1)
            elif move == "R" and col + 1 in VALID:
                original[row][col], original[row][col + 1] = original[row][col + 1], original[row][col]
                new_node = Node(original, move, self.goal, self.current.path_cost + 1)
            elif move == "U" and row - 1 in VALID:
                original[row][col], original[row - 1][col] = original[row - 1][col], original[row][col]
                new_node = Node(original, move, self.goal, self.current.path_cost + 1)
            elif move == "D" and row + 1 in VALID:
                original[row][col], original[row + 1][col] = original[row + 1][col], original[row][col]
                new_node = Node(original, move, self.goal, self.current.path_cost + 1)
            #print(new_node)
            # NOTE: Only add when not seen
            if new_node != None:
                seen = False
                for node in self.reached:
                    if node == new_node and node < new_node:
                        print("Same node seen")
                        seen = True
                
                if seen == False:
                    heapq.heappush(self.frontier, new_node)
                    self.reached.append(new_node)
                    self.num_nodes += 1
    
    def select_next_move(self, output_filename):
        output_file = open(output_filename, 'a')
        moves = ""
        f_vals = ""
        self.try_moves() # expand the first node
        not_solved = True
        while not_solved:
            if len(self.frontier) == 0:
                break
            self.current = heapq.heappop(self.frontier)
            moves += self.current.last_move + " "
            f_vals += str(self.current.fn_value) + " "
            print(self.current)
            if self.current.puzzle == self.goal.puzzle:
                not_solved = False
                print("We solved the puzzle!")
                output_file.write(str(self.current.path_cost) + "\n")
                output_file.write(str(self.num_nodes) + "\n")
                output_file.write(moves + "\n")
                output_file.write(f_vals)
            else:
                self.try_moves()
                self.frontier.sort()

    def get_input(self, input_filename, output_filename):
        # This function takes in the file name and populates goal and current states
        try:
            input_file = open(input_filename, 'r')
        except FileNotFoundError:
            print("{} not found".format(input_filename))
            return
        output_file = open(output_filename, 'w')
        is_goal = False
        goal = []
        start = []
        for line in input_file:
            output_file.write(line)
            if line == "\n":
                is_goal = True
            else:
                line = line.strip()
                line = line.split(" ")
                if is_goal:
                    goal.append(line)
                else:
                    start.append(line)  
        self.goal = Node(goal)
        self.current = Node(start, None, self.goal, 0)
        output_file.write("\n\n")
        input_file.close()
        output_file.close()

def main():
    puzz = Puzzle("input_example.txt", "output_example.txt")
    puzz.select_next_move("output_example.txt")

if __name__ == "__main__":
    main()