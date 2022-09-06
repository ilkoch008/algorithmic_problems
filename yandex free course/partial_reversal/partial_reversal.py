# from node import Node

# Comment it before submitting
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def Reverse(head: Node, left: int, right: int) -> Node:
    counter = 1
    left_edge_node = None

    while counter < left:
        if left_edge_node is None:
            left_edge_node = head
        else:
            left_edge_node = left_edge_node.next
        counter += 1

    if left_edge_node is not None:
        new_right_node = left_edge_node.next
    else:
        new_right_node = head

    one = left_edge_node
    two = new_right_node
    three = two.next

    while counter < right:
        one = two
        two = three
        three = three.next
        two.next = one
        counter += 1

    new_right_node.next = three
    if left_edge_node is not None:
        left_edge_node.next = two
    else:
        head = two

    return head


def print_linked_list(head: Node):
    node_iter = head
    res_str = ''
    while node_iter is not None:
        res_str = res_str + str(node_iter.value) + ' '
        node_iter = node_iter.next
    print(res_str)


linked_list = None

for i in range(20, 0, -1):
    new_node = Node(i, linked_list)
    linked_list = new_node

print_linked_list(linked_list)

print_linked_list(Reverse(linked_list, 1, 10))


