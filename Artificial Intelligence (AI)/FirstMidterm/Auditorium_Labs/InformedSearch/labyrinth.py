#from searching_framework import Problem, astar_search
from searching_framework.utils import Problem
from searching_framework.informed_search import *

class LabyrinthProblem(Problem):
    def __init__(self, initial, walls, wallsN):
        self.initial = initial
        self.walls = walls
        self.size=wallsN


    def successor(self, state):
        #initial = (person, house)
        #result = LabyrinthProblem(initial,walls,wallsN)
        successors = dict()

        actions = ("Desno 2","Desno 3","Gore","Dolu","Levo")
        directions = ((2,0),(3,0),(0,1),(0,-1),(-1,0))
        for action, direction in zip(actions,directions):
            rez = self.move(state,direction)

            if rez != None:

                print (rez)
                successors[action] = rez

        return successors

    def move(self, state, direction):
        # initial = (person, house)
        # result = LabyrinthProblem(initial,walls,wallsN)
        move_player = list(state[0])
        move_player[1] += direction[1]
        if move_player[1] < 0 or move_player[1] >= self.size:
            return None
        if direction[0] > 0: # imame dvizenje na desno a toa e 2 ili 3 pati na desno
            for i in range(direction[0]):
                move_player[0] += 1
                if tuple(move_player) in self.walls:
                    return None
        if direction[0] < 0 : # imame dvizenje na levo
            move_player[0] += direction[0]
        if move_player[0] < 0 or move_player[0] >= self.size: # pri dvizenje stranicno izbegal od gridot
            return None
        if tuple(move_player) in self.walls:
            return None

        final_player = tuple(move_player)
        final_state = (final_player,state[1])

        return tuple(final_state)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self,node):
        playerX,playerY=node.state[0]
        houseX,houseY=node.state[1]
        return (abs(playerX-houseX)+abs(playerY-houseY))/3 # najmnogu moze po tri polinja na desno




if __name__ == '__main__':
    tableSize = int(input())
    wallsN = int(input())
    walls = tuple(tuple(map(int, input().split(","))) for _ in range(wallsN))
    person = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    initial = (person, house)
    result = LabyrinthProblem(initial,walls,tableSize)

    game = astar_search(result)
    if game is not None:
        print(game.solution())
    else:
        print("Nema Resenie")