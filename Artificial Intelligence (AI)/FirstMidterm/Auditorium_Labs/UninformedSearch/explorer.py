from searching_framework.utils import Problem;
from searching_framework.uninformed_search import *;


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        successors = dict()
        #(x,y,(x_o1,y_o1,d_o1),(x_o2,y_o2,d_o2))
        man_x = state[0]
        man_y = state[1]
        obstacle1=list(state[2])
        obstacle2=list(state[3])
            #БИДЕЈЌИ ТОРКИТЕ СЕ НЕПРОМЕНЛИВИ НИЕ ЌЕ ГИ ДЕФИНИРАМЕ ВО ЛИСТИ

        # d = -1 (down) ; d = 1 (up)
        # move for obstacles
        if obstacle1[2] == 1: # up
            if obstacle1[1] == self.grid_size[1]-1: # max vrednost za Y koordinatata
                obstacle1[2] = -1
                obstacle1[1] -= 1
            else:
                obstacle1[1] += 1 # ne stignala do gore pa uste ja pridvizuvame
        else: # down
            if obstacle1[1] == 0: # min vrednosta na Y koordinatata
                obstacle1[2] = 1 # direction switch
                obstacle1[1] += 1 # move one up
            else:
                obstacle1[1] -= 1 # ne stignala najdolu pa samo ja pridvizuvame

        if obstacle2[2] == 1: # up
            if obstacle2[1] == self.grid_size[1]-1:
                obstacle2[2] = -1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else: # down
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles=[(obstacle1[0],obstacle1[1]),(obstacle2[0],obstacle2[1])]

        # (x,y,(x_o1,y_o1,d_o1),(x_o2,y_o2,d_o2))
        # RIGHT x+=1
        if man_x+1 < self.grid_size[0] and (man_x+1,man_y) not in obstacles:
            successors["Right"] = (man_x+1,man_y,(obstacle1[0],obstacle1[1],obstacle1[2]),
                                   (obstacle2[0],obstacle2[1],obstacle2[2]))
        # LEFT x-=1
        if man_x > 0 and (man_x-1,man_y) not in obstacles:
            successors["Left"] = (man_x-1,man_y,(obstacle1[0],obstacle1[1],obstacle1[2]),
                                  (obstacle2[0],obstacle2[1],obstacle2[2]))
        # UP y+=1
        if man_y < self.grid_size[1] and (man_x , man_y + 1) not in obstacles:
            successors["Up"] = (man_x , man_y+1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                  (obstacle2[0], obstacle2[1], obstacle2[2]))
        # DOWN y-=1
        if man_y > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = (man_x, man_y - 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                (obstacle2[0], obstacle2[1], obstacle2[2]))

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        # (x,y,(x_p1,y_p1,n_p1),(x_p2,y_p2,n_p2))
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == "__main__":
    goal_state = (7,4)
    initial_state = (0,2)
    obstacle1 = (2, 5, -1)
    obstacle2 = (5, 0, 1)
    explorer = Explorer((initial_state[0],initial_state[1],(obstacle1[0],obstacle1[1],obstacle1[2]),
                         (obstacle2[0],obstacle2[1],obstacle2[2])),goal_state)
    print(breadth_first_graph_search(explorer).solution())
