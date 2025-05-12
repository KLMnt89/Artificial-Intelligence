from constraint import *

def not_adjacent(tree1, tree2):
    return max(abs(tree1[0] - tree2[0]), abs(tree1[1] - tree2[1])) > 1

if __name__ == '__main__':
    problem = Problem()

    n = int(input())
    trees = []
    for _ in range(n):
        line = input().split(" ")
        tree =(int(line[0]), int(line[1]))
        trees.append(tree)

    directions = [(0,1),(0,-1),(-1,0),(1,0)]

    for tree in trees:
        x, y = tree
        domain = []

        # Проверка за сите валидни соседни позиции
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 6 and 0 <= new_y < 6:  # Ограничување на таблата 6x6
                domain.append((new_x, new_y))

        problem.addVariable(tree, domain)  # Ограничен домен

    problem.addConstraint(AllDifferentConstraint(), trees)
    for tree1 in trees:
        for tree2 in trees:
            if tree1 == tree2:
                continue
            problem.addConstraint(not_adjacent,(tree1, tree2))

    solution = problem.getSolution()

    for tree in trees :
        print(solution[tree][0], solution[tree][1])

