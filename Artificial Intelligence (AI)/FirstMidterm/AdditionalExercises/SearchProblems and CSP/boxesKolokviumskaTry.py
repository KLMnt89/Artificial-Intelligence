from searching_framework.utils import *
from searching_framework.uninformed_search import *


class Box(Problem):
    def __init__(self, initial,n, boxes, goal=None):
        super().__init__(initial,goal)
        self.boxes = boxes
        self.size = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        filled_boxes = state[1]
        return len(filled_boxes) == len(self.boxes)

    def successor(self, state):
        successors = dict()
        #inital = (covece, tuple(),m)
        #problem = Box(inital, boxes)
        x,y = state[0]
        filled_boxes = state[1]
        remaining_boxes = state[2]

        # Gore
        new_x, new_y = x, y + 1
        if new_y < self.size and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_boxes)
            new_remaining_boxes = remaining_boxes
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]), abs(new_y - box[1])) == 1 \
                        and new_remaining_boxes > 0:
                    new_filled_boxes.append(box)
                    new_remaining_boxes -= 1
            successors["Gore"] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining_boxes)

        #Desno
        new_x,new_y = x + 1 , y
        if new_x < self.size and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_boxes)
            new_remaining_boxes = remaining_boxes
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]),abs(new_y - box[1])) == 1 \
                        and new_remaining_boxes > 0:
                    new_filled_boxes.append(box)
                    new_remaining_boxes -= 1
            successors["Desno"] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining_boxes)


        return successors



if __name__ == "__main__":
    n = int(input())
    m = int(input())
    boxes = tuple(tuple(map(int, input().split(","))) for _ in range(m))
    covece = (0,0)

    inital = (covece, tuple(),m)
    problem = Box(inital, n, boxes)
    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")