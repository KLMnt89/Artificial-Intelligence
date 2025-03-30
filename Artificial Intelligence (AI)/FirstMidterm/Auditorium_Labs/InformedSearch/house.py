from searching_framework.utils import Problem
from searching_framework.informed_search import *

class House(Problem):
    #initial = (player, house, dir)
    #game = House(initial, allowed)

    def __init__(self, initial, allowed):
        super().__init__(initial)
        self.allowed = allowed

    def successor(self, state):
        successors = dict()
        actions = ("Stoj","Gore 1","Gore 2","Gore-desno 1","Gore-desno 2","Gore-levo 1","Gore-levo 2")
        directions = ((0,0),(0,1),(0,2),(1,1),(2,2),(-1,1),(-2,2))

        for action, direction in zip(actions, directions):
            rez = self.move(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors

    def move(self, state, direction):
        # initial = (player, house, dir)
        # game = House(initial, allowed)
        #---initialization
        player_move = list (state[0])
        house_move = list(state[1])
        house_direction = int(state[2])

        #---moving
        if house_move[0] == 0 or house_move[0] == 4: #if house is on the edge of the grid
            house_direction *= -1 #change direction of moving
        house_move[0] += house_direction #moving the house
        player_move[0] += direction[0] #moving the player on X axis
        player_move[1] += direction[1] #moving the player on Y axis

        if player_move[0] < 0 or player_move[0] >4 or player_move[1] < 0 or player_move[1] > 8: # if with next move player is out of boundaries return none
            return None
        if tuple(player_move) not in self.allowed: # if player wants to stay on non green place
            if player_move != house_move: #if player isn`t in the house
                return None

        playerNew = tuple(player_move)
        houseNew = tuple(house_move)
        dirNew = house_direction
        final_state=(playerNew,houseNew,dirNew)
        return final_state

    def goal_test(self, state):
        return state[0] == state[1] # dali coveceto e vo kukjata

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):

        return ((8-node.state[0][1])/2)-1


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    player = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    direction = input()
    dir=1 if direction == "desno" else -1 # levo=-1 desno=1

    initial = (player, house, dir)
    game = House(initial, allowed)
    result = astar_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("Nema Resenie")