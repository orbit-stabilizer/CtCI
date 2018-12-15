from typing import Optional, Union

from utils import Node


# Time Complexity: O(n)
# Space Complexity: O(n)
def loop_detection(head: Node) -> Union[Node, bool]:
    """
    Returns:
        If there is a loop, returns the node at the start of the loop
        Else returns False
    """
    nodes: set = set()
    node: Optional[Node] = head

    while node:
        if node in nodes:
            return node
        else:
            nodes.add(node)
            node = node.next

    return False


class TestLoopDetection():
    def test_simple_case_loop(self):
        head = Node(1, Node(2))
        loop_node = Node(3, Node(4))
        head.next.next = loop_node
        head.next.next.next.next = loop_node

        assert loop_detection(head) is loop_node
    
    def test_simple_case_no_loop(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

        assert loop_detection(head) is False