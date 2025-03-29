from searching_framework import Problem, breadth_first_graph_search

#(xp,yp),(xb,yb)
class FootballProblem(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.goal=((7,2),(7,3))
        self.width=8
        self.height=6
        self.opponents=((3, 3), (5, 4))
    def goal_test(self, state):
        return state[1] in self.goal
    def successor(self,state):
        successors=dict()
        actions=("Pomesti coveche gore", "Pomesti coveche dolu",
                   "Pomesti coveche desno", "Pomesti coveche gore-desno",
                   "Pomesti coveche dolu-desno", "Turni topka gore",
                   "Turni topka dolu", "Turni topka desno",
                   "Turni topka gore-desno", "Turni topka dolu-desno")
        directions= (
            ((0, 1), (0, 0)),#gore
            ((0, -1), (0, 0)),#dolu
            ((1, 0), (0, 0)),#desno
            ((1, 1), (0, 0)),#gore-desno
            ((1, -1), (0, 0)),#dolu-desno
            ((0, 1), (0, 1)),#topkata odi vo pravec so coveceto
            ((0, -1), (0, -1)),
            ((1, 0), (1, 0)),
            ((1, 1), (1, 1)),
            ((1, -1), (1, -1))
        )
        for action, direction in zip(actions, directions):
            rez = self.check_state(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors
    def check_state(self,state,direction):
        move_player=list(state[0])
        move_ball=list(state[1])
        if move_ball==move_player:
            return None
        if direction[1][0] !=0 or direction[1][1] !=0:#ima dvizenje
            check_player=(move_ball[0]-direction[1][0],move_ball[1]-direction[1][1])
            check_player=list(check_player)

            if check_player != move_player:
                return None
        move_ball[0] += direction[1][0]
        move_ball[1] += direction[1][1]
        move_player[0] += direction[0][0]
        move_player[1] += direction[0][1]
        move_player = tuple(move_player)
        move_ball = tuple(move_ball)
        new_state = (move_player, move_ball)
        new_state = tuple(new_state)
        if self.check_valid(new_state):
            return new_state
        return None

    def check_valid(self,state):
        if state[0] == state[1]:#igracot e na ista pozicija so topkata
            return False
        if state[0] in self.opponents:#igracot e na protivnickite igraci
            return False
        x, y = state[0]
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        x, y = state[1]
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if self.opponents[0][0]+i==x and self.opponents[0][1]+j==y:#dali igracot ili topkata se vo neposredna blizina na prviot protivnicki igrac
                    return False
                if self.opponents[1][0]+i==x and self.opponents[1][1]+j==y:
                    return False
        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == '__main__':
    player = tuple(map(int, input().split(",")))
    ball = tuple(map(int, input().split(",")))

    initial_state = (player, ball)
    game = FootballProblem(initial_state)
    node = breadth_first_graph_search(game)
    if node is not None:
        print(node.solution())
    else:
        print("No solution")