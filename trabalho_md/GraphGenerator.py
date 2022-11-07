from streamlit_agraph import agraph, Node, Edge, Config
import streamlit as st

def graph_generator(matrix: list[list[int]]):
    nodes = []
    edges = []
    for node_index in range(0, len(matrix)):
        new_node = Node(
                    id=f"A{node_index +1 }",
                    size=100
        )
        nodes.append(new_node)

    for node_index in range(0, len(matrix)):
        for index, node_connection in enumerate(matrix[node_index]):
            if node_connection:
                new_edge = Edge(source=f"A{node_index+1}",
                                target=f"A{index + 1}")
                edges.append(new_edge)

    config = Config(directed=False,
                width=500, 
                height=500
                ) 

    plot = agraph(nodes=nodes, 
                    edges=edges, 
                    config=config) 

