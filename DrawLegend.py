# Author : Junth Basnet

import pydot


def draw_legend(graph):
    graphlegend = pydot.Cluster(graph_name="legend", label="Labels", fontsize="20", color="red",
                                fontcolor="blue", style="filled", fillcolor="white", fontname='Arsenal')

    legend1 = pydot.Node('Explored State (ES)', shape="plaintext", fontname='Arsenal', fontsize="20")
    graphlegend.add_node(legend1)

    legend2 = pydot.Node('UnExplored State (UES)', shape="plaintext", fontname='Arsenal', fontsize="20")
    graphlegend.add_node(legend2)

    legend3 = pydot.Node('Goal State (GS)', shape="plaintext", fontname='Arsenal', fontsize="20")
    graphlegend.add_node(legend3)

    node1 = pydot.Node("1", style="filled", fillcolor="orange", label="")
    graphlegend.add_node(node1)
    node2 = pydot.Node("2", style="filled", fillcolor="gray", label="")
    graphlegend.add_node(node2)
    node3 = pydot.Node("3", style="filled", fillcolor="green", label="")
    graphlegend.add_node(node3)

    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(legend1, legend2, style="invis"))
    graph.add_edge(pydot.Edge(legend2, legend3, style="invis"))

    graph.add_edge(pydot.Edge(node1, node2, style="invis"))
    graph.add_edge(pydot.Edge(node2, node3, style="invis"))
