# Author : Junth Basnet

import pydot


class Puzzle:
    goal_state = [
        1, 2, 3,
        8, 0, 4,
        7, 6, 5]

    num_of_instances = 0

    def __init__(self, state, parent, action, depth):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth
        self.goal_state = [
            1, 2, 3,
            8, 0, 4,
            7, 6, 5]

        if self.goal_test():
            color = "green"
        elif self.depth >= 5:
            color = "gray"
        else:
            color = "orange"
        self.graph_node = pydot.Node(str(self), fontsize='30',style="filled", fillcolor=color, )
        Puzzle.num_of_instances += 1

    def display(self):
        list_state = self.state
        string = ""
        for i in range(9):
            if (i + 1) % 3 != 0:
                if list_state[i] == 0:
                    string += "|   "
                else:
                    string += ("| %d " % list_state[i])
            else:
                if list_state[i] == 0:
                    string += "|   \n"
                else:
                    string += ("| %d |\n" % list_state[i])
        string += "\n"
        return string

    def __str__(self):
        return self.display()

    def goal_test(self):
        return self.state == self.goal_state

    @staticmethod
    def find_legal_actions(i, j):
        legal_action = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        """UP and DOWN Disable Condition"""
        if i == 0:
            legal_action.remove('UP')
        elif i == 2:
            legal_action.remove('DOWN')

        """LEFT and RIGHT Disable Condition"""
        if j == 0:
            legal_action.remove('LEFT')
        elif j == 2:
            legal_action.remove('RIGHT')
        return legal_action

    def generate_child(self):
        children = []
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions = self.find_legal_actions(i, j)
        depth = self.depth + 1

        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'UP':
                new_state[x], new_state[x - 3] = new_state[x - 3], new_state[x]
            elif action is 'DOWN':
                new_state[x], new_state[x + 3] = new_state[x + 3], new_state[x]
            elif action is 'LEFT':
                new_state[x], new_state[x - 1] = new_state[x - 1], new_state[x]
            elif action is 'RIGHT':
                new_state[x], new_state[x + 1] = new_state[x + 1], new_state[x]
            children.append(Puzzle(new_state, self, action, depth))
        return children

    def find_solution(self):
        solution = [self.action]
        path = self
        while path.parent is not None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution
