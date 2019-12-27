# Author : Junth Basnet

from PriorityQueue import PriorityQueue as Queue
from Puzzle import Puzzle
from DrawLegend import draw_legend
import pydot


def a_star_algorithm(initial_state):
    graph = pydot.Dot(graph_type='digraph', label="8 Puzzle State Space Search using A* Algorithm", fontsize="30",
                      color="red",
                      fontcolor="black", fontname='Arsenal', fillcolor="black")

    start_node = Puzzle(initial_state, None, None, 0)

    if start_node.goal_test():
        return start_node.find_solution()

    frontier = Queue()
    frontier.push(start_node)
    explored = []
    star = "**********************************"

    print("\nInitial State ---------- Depth: {0}".format(start_node.depth))

    finished = False
    while not (frontier.is_empty()):
        v = frontier.pop()
        node = v[-1]
        print("{0}".format(node.display()))
        print(star)
        explored.append(node.state)
        graph.add_node(node.graph_node)

        if node.parent:
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,
                                      label="[h(n) = " + str(v[0]) + ",g(n) = " + str(node.depth) + "]",
                                      fontsize='15', fontcolor='#cc0099', fontname='Arsenal'))

        if not finished:
            children = node.generate_child()
            for child in children:
                if child.state not in explored:
                    print("Depth = {0} \n".format(child.depth))
                    print(child.display())
                    print("--------------------------------------------------")

                    if child.goal_test():
                        print("***************GOAL STATE FOUND*******************")
                        print("\n")
                        print(child.display())
                        graph.add_node(child.graph_node)
                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node,
                                                  label="[h(n) = " + str(v[0]) + ",g(n) = " + str(node.depth) + "]",
                                                  fontsize='15', fontcolor='#cc0099', fontname='Arsenal'))
                        draw_legend(graph)
                        return child.find_solution()
                        finished = True
                    else:
                        frontier.push(child)
        else:
            graph.write_png('Stace Space Search Tree(AStar).png')
            graph.write_pdf('Stace Space Search Tree(AStar).pdf')
    return
