from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

##from searching_framework import *
# from utils import *
# from uninformed_search import *
# from informed_search import *

class Boxes(Problem):
    def __init__(self, initial,n, boxes, goal=None):
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
        #initial = (coveceto, tuple(), m)  # ((0,0),(,),br_topki)
        #problem = Boxes(initial, n, pozicii)

        succesors = dict()
        x,y = state[0]
        filled_boxes = state[1]
        remaining_balls = state[2]

        #Gore
        new_x,new_y = x, y + 1
        if new_y < self.size and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_boxes)
            new_remaining_balls = remaining_balls
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]),abs(new_y - box[1])) == 1 and \
                        new_remaining_balls > 0:
                    new_filled_boxes.append(box)
                    new_remaining_balls -= 1
            succesors["Gore"] = ((new_x, new_y), tuple(new_filled_boxes),new_remaining_balls)

        # Desno
        new_x, new_y = x + 1, y
        if new_x < self.size and (new_x, new_y) not in self.boxes:
            new_filled_boxes = list(filled_boxes)
            new_remaining_balls = remaining_balls
            for box in self.boxes:
                if box not in new_filled_boxes and max(abs(new_x - box[0]), abs(new_y - box[1])) == 1 and \
                        new_remaining_balls > 0:
                    new_filled_boxes.append(box)
                    new_remaining_balls -= 1
            succesors["Desno"] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining_balls)


        return succesors





if __name__ == '__main__':
    n = int(input()) #golemina na tabla
    m = int(input()) #broj na topki
    pozicii = tuple(tuple(map(int,input().split(",")))for _ in range(m))
    coveceto = (0,0)


    initial = (coveceto, tuple(), m) #((0,0),(,),br_topki)
    problem = Boxes(initial,n, pozicii)
    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")

