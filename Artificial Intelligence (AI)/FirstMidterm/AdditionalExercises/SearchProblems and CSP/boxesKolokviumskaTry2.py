from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

##from searching_framework import *

class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal=None):
        super().__init__(initial, goal)
        self.size = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        filled_boxes = state[1]
        return len(filled_boxes) == len(self.boxes)

    def successor(self, state):
        successors = dict()
        #initial = (man_pos, tuple(), num_boxes)
        #problem = Boxes(initial, n, boxes)
        x,y = state[0]
        filled_boxes = state[1]
        remaining_balls = state[2]

        #Down
        new_x,new_y = x, y - 1
        if new_y >= 0 and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_boxes)
            new_remaining_balls = remaining_balls
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]),abs(new_y - box[1])) == 1 \
                        and new_remaining_balls >0 :
                    new_filled_boxes.append(box)
                    new_remaining_balls -= 1
            successors["Down"] = ((new_x, new_y), tuple(new_filled_boxes),new_remaining_balls)

        # Left
        new_x, new_y = x - 1, y
        if new_x >= 0 and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_boxes)
            new_remaining_balls = remaining_balls
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]), abs(new_y - box[1])) == 1 \
                        and new_remaining_balls > 0:
                    new_filled_boxes.append(box)
                    new_remaining_balls -= 1
            successors["Left"] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining_balls)

        return successors



if __name__ == '__main__':
    n = int(input())
    man_pos = (n-1, n-1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    initial = (man_pos, tuple(), num_boxes)
    problem = Boxes(initial, n, boxes)

    result = breadth_first_graph_search(problem)
    if result is not None :
        print(result.solution())
    else :
        print("No Solution!")
