    def manhattan_distance(self, goal):
        manhattan_distance = 0
        for curr_row in range(3):
            for curr_col in range(3):
                curr_num = self.puzzle[curr_row][curr_col]
                print(curr_row, curr_col, curr_num, end= " distance: ")
                for goal_row in range(3):
                    for goal_col in range(3):
                        if goal.puzzle[goal_row][goal_col] == curr_num:
                            single_distance = abs(goal_row - curr_row) + abs(goal_col - curr_col)
                            manhattan_distance += single_distance

                            if curr_num == 0:
                                manhattan_distance -= single_distance
                            print(single_distance)
        print("{} distance".format(manhattan_distance))