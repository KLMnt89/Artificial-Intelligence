from searching_framework.utils import Problem;
from searching_framework.uninformed_search import *;

#(xp,yp),(xb,yb)
class FootballProblem(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.goal=((7,2),(7,3))
        self.width=8
        self.height=6
        self.opponents=((5, 5), (5, 6))

    def goal_test(self, state):
        return state[1] in self.goal

    def successor(self,state):
        successors=dict()
        # initialState = ((p_x,p_y),(b_x,b_y))

        actions = ("Pomesti coveche gore", "Pomesti coveche dolu","Pomesti coveche desno",
                   "Pomesti coveche gore-desno","Pomesti coveche dolu-desno","Turni topka gore",
                   "Turni topka dolu","Turni topka desno","Turni topka gore-desno",
                   "Turni topka dolu-desno")

        directions = (
            ((0,1),(0,0)),   #gore
            ((0,-1),(0,0)),  #dolu
            ((1,0),(0,0)),   #desno
            ((1,1),(0,0)),   #gore-desno
            ((1,-1),(0,0)),  #dolu-desno
            ((0,1),(0,1)),   #gore + sut
            ((0,-1),(0,-1)), #dolu + sut
            ((1,0),(1,0)),   #desno + sut
            ((1,1),(1,1)),   #gore-desno + sut
            ((1,-1),(1,-1)),  #dolu-desno +sut
        )
        for action,direction in zip(actions,directions):
            rez = self.check_state(state,direction)
            if rez is not None:
                successors[action]=rez

        #print(f"Successors for {state}: {successors.keys()}")
        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        successors = self.successor(state)
        if action in successors:
            return successors[action]
        return state  # Ако не постои, врати ја истата состојба (или None ако сакаш грешка).

    def check_state(self, state, direction):
        # initialState = ((p_x,p_y),(b_x,b_y))
        move_player = list(state[0])
        move_ball = list(state[1])
        if move_ball == move_player:
            return None
        if direction[1][0] != 0 or direction[1][1] != 0:  #situacija koga imame sut na topkata
            check_player = (move_ball[0] - direction[1][0],move_ball[1] - direction[1][1])

            if list(check_player) != move_player: #ako igracot ne se naogja vo neposredna blizina udarot e nedozvoliv
                return None

        move_ball[0] += direction[1][0]  #azuriranje na pozicijata na topkata i na igracot
        move_ball[1] += direction[1][1]
        move_player[0] += direction[0][0]
        move_player[1] += direction[0][1]
        move_player = tuple(move_player)
        move_ball = tuple(move_ball)
        new_state = (move_player, move_ball)

        # Дополнително ќе ги поместуваме и противниците
        #new_opponents = self.move_opponents(move_ball)
        #self.opponents = new_opponents

        if self.check_valid(new_state):# kje proverime dali slucajno sme izlegle od granicite ili ne sme naisle na obstacles
            return new_state

        #print(f"Invalid state: {new_state}")
        return None

    def check_valid(self, state):
        if state[0] == state[1]: #topkata i igracot da se na ista pozicija
            return False
        if state[0] in self.opponents: #ako igracot naisol na protivnicki igrac odnosno prethodno do nego imalo obstacle
            return False
        x,y = state[0][0],state[0][1]
        if x < 0 or x >= self.width or y < 0 or y >= self.height: # dali igracot izlegol od ramkite na igralisteto
            return False
        x, y = state[1][0],state[1][1]
        if x < 0 or x >= self.width or y < 0 or y >= self.height: # dali topkata izlegla od ramkite na igralisteto
            return False
        for i in [-1,0,1]: # proveruvame dali topkata e vo radius 1 na nekoj od dvata protivnici
            for j in [-1,0,1]:
                if (self.opponents[0][0] + i == x and self.opponents[0][1] + j == y) or \
                        (self.opponents[1][0] + i == x and self.opponents[1][1] + j == y):
                    #print(f"Ball blocked by opponent at: {(x, y)}")
                    return False
        return True

    def move_opponents(self, ball_position):
        new_opponents = []
        for ox,oy in self.opponents:
            new_x,new_y = ox,oy

            if ox < ball_position[0]:   #topkata na desno i protivnicite trgnuvaat na desno
                new_x += 1
            elif ox > ball_position[0]: #topkata na levo i protivnicite trgnuvaat na levo
                new_x -= 1

            if oy < ball_position[1]:   #topkata na gore i protivnicite trgnuvaat na gore
                new_y += 1
            elif oy > ball_position[1]: #topkata na dolu i protivnicite trgnuvaat na dolu
                new_y -= 1

            new_opponents.append((new_x,new_y))

        #print(f"Opponents moved to: {new_opponents}")
        return tuple(new_opponents)

if __name__ == '__main__':
    player = tuple(map(int, input().split(",")))
    ball = tuple(map(int, input().split(",")))
    initialState = (player, ball)
    game = FootballProblem(initialState)
    result = breadth_first_graph_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("Nema Resenie")


