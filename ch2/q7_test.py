from typing import Union, Optional

from utils import Node


# Time Complexity: O(n)
# Space Complexity: O(n)
def intersection(head_1: Node, head_2: Node) -> Union[Node, bool]:
    """
    Returns:
        False if linked lists do not intersect
        The first intersection Node if they intersect (by reference, not value)
    """
    node: Optional[Node] = head_1
    nodes: set = set()

    while node:
        nodes.add(node)
        node = node.next

    node = head_2

    while node:
        if node in nodes:
            return node

        node = node.next

    return False


class TestIntersection():
    def test_simple_case_pass(self):
        head_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        head_2 = Node(1, Node(2, Node(3)))

        intersect = Node(6, Node(7, Node(8)))
        head_1.next.next.next.next.next = intersect
        head_2.next.next.next = intersect

        assert intersection(head_1, head_2) is intersect

    def test_simple_case_fail(self):
        head_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        head_2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

        assert intersection(head_1, head_2) is False
