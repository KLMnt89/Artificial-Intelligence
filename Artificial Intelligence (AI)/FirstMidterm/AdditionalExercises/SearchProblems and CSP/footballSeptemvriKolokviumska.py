from searching_framework.utils import *
from searching_framework.uninformed_search import *

class Football(Problem):
    def __init__(self, initial,referees, goal=None):
        super().__init__(initial, goal)
        self.goal = ((0,2),(0,3))
        self.width = 7
        self.height = 6
        self.referees = referees

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal

    def successor(self, state):
        successors = dict()
        #initial = (player, ball)
        #problem = Football(initial, referees)
        actions = ("Pomesti coveche gore", "Pomesti coveche dolu",
                   "Pomesti coveche desno", "Pomesti coveche gore-levo",
                   "Pomesti coveche dolu-levo", "Turni topka gore",
                   "Turni topka dolu", "Turni topka desno",
                   "Turni topka gore-levo", "Turni topka dolu-levo")
        directions = (
            ((0,1),(0,0)),  #gore
            ((0, -1), (0, 0)),  #dolu
            ((1, 0), (0, 0)),  #desno
            ((-1, 0), (0, 0)),  #levo
            ((-1, 1), (0, 0)),  #gore-levo
            ((-1, -1), (0, 0)),#dolu-levo
            ((0, 1), (0, 1)),  # gore + topka
            ((0, -1), (0, -1)),  # dolu + topka
            ((1, 0), (1, 0)),  # desno + topka
            ((-1, 0), (-1, 0)),  # levo + topka
            ((-1, 1), (-1, 1)),  # gore-levo + topka
            ((-1, -1), (-1, -1))  # dolu-levo+ topka
        )

        for action, direction in zip(actions,directions):
            rez = self.move(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors

    def move(self, state, direction):
        # initial = (player, ball)
        # problem = Football(initial, referees)
        move_player = list(state[0])
        move_ball = list(state[1])
        if tuple(move_player) in self.referees or tuple(move_ball) in self.referees:
            return None

        if direction[1][0] != 0 or direction[1][1] != 0 :
            check_ball = (move_ball[0] + direction[1][0] , move_ball[1] + direction[1][1] )
            if tuple(check_ball) in self.referees:
                return None
        else:
            if (direction[0][0] == -1 and direction[0][1] == -1) or (direction[0][0] == -1 and direction[0][1] == 1):
                return None

        move_ball[0] += direction[1][0]
        move_ball[1] += direction[1][1]
        move_player[0] += direction[0][0]
        move_player[1] += direction[0][1]

        move_player = tuple(move_player)
        move_ball = tuple(move_ball)
        new_state = (move_player, move_ball)
        return new_state


if __name__ == "__main__":
    size = (7,6)

    n = int(input())
    referees = tuple(tuple(map(int, input().split(","))) for _ in range(n))
    player = tuple(map(int,input().split(",")))
    ball = tuple(map(int, input().split(",")))

    initial = (player, ball )
    problem = Football(initial, referees, size)
    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")