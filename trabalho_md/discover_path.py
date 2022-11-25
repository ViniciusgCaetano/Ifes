from random import *

def discover_path(matrix):
    even_nodes = [True if sum(line)//2==0 else False for line in matrix]
    path_stack = []


    if all(even_nodes):
        start_node_index = randint(0, len(matrix))
        start_node = matrix[start_node_index]
    else:
        start_node_index = even_nodes.index(False)
        start_node = matrix[start_node_index]

    if sum(start_node) == 0:
        path_stack.append(start_node_index)
    else:
        neighboors = [i for i in range(len(start_node)) if start_node[i] == 1]

        
        

