from typing import Dict


class Node:
    def __init__(self, weight, parent) -> None:
        self.weight = weight
        self.parent = parent
        self.cur_chil = 0
        self.children = []


def get_number_of_upgoing_paths(root: Node, x: int) -> int:
    counter = 0
    seen_sums = {0: 1}
    prefix_sum = 0
    cur_node = root
    cur_node.parent = None
    while True:
        if cur_node.cur_chil == 0:  # we came at this node for the first time
            prefix_sum += cur_node.weight
            counter += seen_sums.get(prefix_sum - x, 0)
            if prefix_sum in seen_sums:
                seen_sums[prefix_sum] += 1
            else:
                seen_sums[prefix_sum] = 1
        if cur_node.cur_chil < len(cur_node.children):  # check all children
            next_node = cur_node.children[cur_node.cur_chil]
            next_node.parent = cur_node
            cur_node.cur_chil += 1
            cur_node = next_node
        else:  # we checked all children and go back
            seen_sums[prefix_sum] -= 1
            prefix_sum -= cur_node.weight
            cur_node = cur_node.parent
            if cur_node is None:
                break
    return counter


def read_tree(tree_size: int) -> Node:
    nodes = []
    root = None
    for i in range(tree_size):
        p, w = map(int, input().split())
        nodes.append(Node(w, p))
        if p == -1:
            root = nodes[i]
    for i in range(tree_size):
        if nodes[i].parent != -1:
            nodes[nodes[i].parent].children.append(nodes[i])
    return root


n, x = map(int, input().split())
tree = read_tree(n)
print(get_number_of_upgoing_paths(tree, x))