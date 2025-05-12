from constraint import *


def count_in_col_i(*trees):
    for i in range(6):
        tents_col = 0
        for tree in trees:
            if tree[0] == i:
                tents_col += 1
        if tents_col != cols[i]:
            return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    trees = []
    for _ in range(n):
        line = input().split(" ")
        tree = (int(line[0]),int(line[1]))
        trees.append(tree)
    cols = [int(x) for x in input().split(" ")]

    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    for tree in trees:
        x,y = tree
        domain = []
        for dx,dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 6 and 0 <= new_y < 6 and (new_x, new_y) not in trees:
                domain.append((new_x, new_y))
        problem.addVariable(tree, domain)

    problem.addConstraint(AllDifferentConstraint(),trees)
    problem.addConstraint(count_in_col_i, trees)

    solution = problem.getSolution()

    for tree in trees:
        print(solution[tree][0], solution[tree][1])


