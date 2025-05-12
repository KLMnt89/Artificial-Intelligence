from constraint import *

def diffirent(a,b):
    return a != b

if __name__ == '__main__':
    problem = Problem()

    variables = ["WA","NT","SA","Q","NSW","V","T"]
    domain = ["red","green","blue"]

    problem.addVariables(variables,domain)
    problem.addConstraint(diffirent,("WA","NT"))
    problem.addConstraint(diffirent, ("WA", "SA"))
    problem.addConstraint(diffirent, ("SA", "NT"))
    problem.addConstraint(diffirent, ("SA", "NSW"))
    problem.addConstraint(diffirent, ("SA", "Q"))
    problem.addConstraint(diffirent, ("SA", "V"))
    problem.addConstraint(diffirent, ("NT", "Q"))
    problem.addConstraint(diffirent, ("Q", "NSW"))
    problem.addConstraint(diffirent, ("NSW", "V"))

    solutions = problem.getSolutions()

    print(solutions)

