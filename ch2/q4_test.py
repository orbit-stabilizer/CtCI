import pytest
from typing import List, Optional

from utils import Node, LinkedList


# Time Complexity: O(n)
# Space Complexity: O(n)
def partition(head: Node, p_val: int) -> None:
    """
    Partitions a linked list given the head node and a partition value.
    Partition:
        Every node with value less than p_val will come before every node
        with value greater than or equal to p_val.
    """
    vals_less_than_p_val: List[int] = []
    vals_greater_than_p_val: List[int] = []

    curr: Optional[Node] = head
    while curr:
        if curr.data < p_val:
            vals_less_than_p_val.append(curr.data)
        else:
            vals_greater_than_p_val.append(curr.data)

        curr = curr.next

    curr = head
    while curr:
        if vals_less_than_p_val:
            curr.data = vals_less_than_p_val.pop()
        else:
            curr.data = vals_greater_than_p_val.pop()

        curr = curr.nex


class TestPartition():

    @pytest.fixture
    def head(self):
        """
        Initialize the linked list.
        """
        head = Node(5)
        linked_list = LinkedList(head)

        linked_list.append(Node(4))
        linked_list.append(Node(3))
        linked_list.append(Node(2))
        linked_list.append(Node(1))

        return head

    def test_simple(self, head):
        assert head.data == 5

        partition(head, 3)

        assert head.data != 5
