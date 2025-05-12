from searching_framework.utils import Problem;
from searching_framework.uninformed_search import *;

#(snakeSegments,0,greenApples),redApples
class Snake(Problem):
    def __init__(self, initial, redApples):
        super().__init__(initial)
        self.redApples=redApples
        self.size=10
        self.moves=((0,-1),(1,0),(0,1),(-1,0)) #dolu,desno,gore,levo

    def goal_test(self, state):
        return len(state[2]) == 0


    def successor(self, state):
        successors = dict()
        acts=("ProdolzhiPravo","SvrtiDesno","SvrtiLevo")
        directions=(0,1,-1)
        for action,direction in zip(acts,directions):
            rez = self.move(state,direction)
            if rez is not None:
                successors[action]=rez


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def move(self, state, direction):
        next_snake_direction = (state[1] + direction) % 4
        snakeSegments = list(state[0])
        snakeHead = (snakeSegments[0][0]+self.moves[next_snake_direction][0],
                     snakeSegments[0][1]+self.moves[next_snake_direction][1])
        greenApples = list(state[2])
        x,y = snakeHead
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return None
        if (x,y) in self.redApples:
            return None
        if (x,y) in snakeSegments[1:len(snakeSegments)-1]:
            return None
        snakeSegments.insert(0,snakeHead)
        if (x,y) in greenApples:
            greenApples.remove((x,y))
        else:
            snakeSegments.pop()
        return tuple(snakeSegments),next_snake_direction,tuple(greenApples)




if __name__ == '__main__':
    # Snake(initial_state, red_apples)   initial_state = (snake_segments, 2, green_apples)
    N_greenApples=int(input())
    greenApples=[tuple(map(int,input().split(','))) for _ in range(N_greenApples)]
    greenApples=tuple((i,9-j) for i,j in greenApples)

    N_redApples=int(input())
    redApples=[tuple(map(int,input().split(","))) for _ in range(N_redApples)]
    redApples=tuple((i,9-j) for i,j in redApples)

    snakeSegments=((0,2),(0,1),(0,0))
    initalState= (snakeSegments,2,greenApples)

    game=Snake(initalState,redApples)
    result=breadth_first_graph_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("Nema Resenie")
