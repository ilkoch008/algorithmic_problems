from typing import List, Optional
from collections import deque


class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.depth = 0
        self.left = None
        self.right = None


def get_tree_border(root: Node, res: set):
    pipe = deque()
    root.depth = 0
    pipe.append(root)
    prev_depth = 0
    prev_node = root
    while len(pipe) > 0:
        node = pipe.popleft()
        depth = node.depth
        if node.left is not None:
            node.left.depth = depth+1
            pipe.append(node.left)
        if node.right is not None:
            node.right.depth = depth+1
            pipe.append(node.right)
        if prev_depth < depth:
            res.add(prev_node.id)
            res.add(node.id)
            prev_depth = depth
        prev_node = node
    print(*res)


def read_tree(res: set) -> Node:
    size, root_id = map(int, input().split())
    nodes = [Node(i) for i in range(size)]
    for i in range(size):
        left, right = map(int, input().split())
        nodes[i].left = nodes[left] if left != -1 else None
        nodes[i].right = nodes[right] if right != -1 else None
        if left == -1 and right == -1:
            res.add(i)
    return nodes[root_id]


res = set()
tree = read_tree(res)
get_tree_border(tree, res)
