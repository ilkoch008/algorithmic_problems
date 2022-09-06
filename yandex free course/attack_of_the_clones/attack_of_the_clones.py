# from node import Node


# Comment it before submitting
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []


def cloneGraph(node) -> Node:
    stack = []
    old_new_map = {}
    new_root_node = Node(node.val)
    old_new_map[node] = new_root_node
    stack.append(node)
    while len(stack) > 0:
        cur_old_node = stack[-1]
        stack.pop()
        cur_new_node = old_new_map[cur_old_node]
        for neighbour in cur_old_node.neighbours:
            if neighbour in old_new_map:
                cur_new_node.neighbours.append(old_new_map[neighbour])
            else:
                new_node = Node(neighbour.val)
                old_new_map[neighbour] = new_node
                cur_new_node.neighbours.append(new_node)
                stack.append(neighbour)
    return new_root_node
