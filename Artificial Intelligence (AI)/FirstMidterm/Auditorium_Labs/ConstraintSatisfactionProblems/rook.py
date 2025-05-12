from constraint import *

def not_attacking(rook1,rook2):
    return rook1[0] != rook2[0] and rook1[1] != rook2[1]

if __name__ == '__main__':
    problem = Problem()
    domain = [(i,j) for i in range(0,8) for j in range(0,8)]
    variable = range(1,9)
    problem.addVariables(variable, domain)

    problem.addConstraint(AllDifferentConstraint(), variable)

    solutions = problem.getSolutions()
    print(solutions)