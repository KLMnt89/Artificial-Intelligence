from searching_framework.utils import Problem;
from searching_framework.uninformed_search import *;

class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities;

    def successor(self,state):
        succesors = dict()
        j0,j1 = state
        c0,c1 = self.capacities;

        if j0 > 0:
            succesors["Isprazni go sadot J0 "]=(0,j1)
        if j1 > 0:
            succesors["Isprazni go sadot J1 "] = (j0, 0)
        if j0 > 0 and j1 < c1:
            delta=min(j0,c1-j1)
            succesors["Preturi od J0 vo J1 "]= (j0-delta,j1+delta)
        if j1 > 0 and j0 < c0:
            delta=min(j1,c0-j0)
            succesors["Preturi od J1 vo J0 "]= (j0+delta,j1-delta)
        if j0 < c0:
            succesors["Napolni go sadot J0"]= (c0,j1)
        if j1 < c1:
            succesors["Napolni go sadot J1"]= (j0,c1)
        return succesors;

    def actions(self,state):
        return self.successor(state).keys();

    def result(self,state,action):
        return self.successor(state)[action];

    def goal_test(self,state):
        return state == self.goal;

if __name__ == "__main__":
    container= Container([15,5],(5,5),(10,5))
    result=breadth_first_graph_search(container);
    print(result.solution());
    #print("-----");
    print("Најдена патека:", result.solve())
