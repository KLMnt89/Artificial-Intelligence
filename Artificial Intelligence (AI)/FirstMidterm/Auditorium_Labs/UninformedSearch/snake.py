from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial)
        self.red_apples = red_apples
        self.size = 10
        self.moves = ((0, -1),(1, 0),(0, 1),(-1, 0)) #dolu,desno,gore,levo

    def goal_test(self, state):
        return len(state[2]) == 0

    # Snake(initial_state, red_apples)   initial_state = (snake_segments, 2, green_apples)
    def successor(self, state):
        successors = dict()

        acts = ("ProdolzhiPravo", "SvrtiDesno", "SvrtiLevo")
        directions = (0, 1, -1)
        for action, direction in zip(acts, directions):
            rez = self.move(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors

    def move(self, state, direction):
        next_snake_direction = (state[1] + direction) % 4
        snake_segments = list(state[0])
        snake_head = (snake_segments[0][0]+self.moves[next_snake_direction][0], snake_segments[0][1]+ self.moves[next_snake_direction][1])
        apples = list(state[2])
        x,y= snake_head
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return None
        if (x, y) in self.red_apples: #jade jabolko
            return None
        if (x, y) in snake_segments[1:len(snake_segments)-1]:#se jade samata sebe
            return None
        snake_segments.insert(0, snake_head)
        if (x, y) in apples:
            apples.remove((x, y))
        else:
            snake_segments.pop()

        return tuple(snake_segments), next_snake_direction, tuple(apples)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    num_green_apples = int(input())
    green_apples_input = [tuple(map(int, input().split(',')))
                          for _ in range(num_green_apples)]
    green_apples = tuple((i, 9 - j) for i, j in green_apples_input)

    num_red_apples = int(input())
    red_apples_input = [tuple(map(int, input().split(',')))
                        for _ in range(num_red_apples)]
    red_apples = tuple((i, 9 - j) for i, j in red_apples_input)

    snake_segments = ((0, 2), (0, 1), (0, 0))
    initial_state = (snake_segments, 2, green_apples)

    game = Snake(initial_state, red_apples)
    result = breadth_first_graph_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("Nema Resenie")