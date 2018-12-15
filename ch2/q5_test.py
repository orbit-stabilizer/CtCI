import pytest
from typing import Callable, List, Optional, Tuple

from utils import Node, LinkedList


# Time Complexity: O(n)
# Space Complexity: O(n)
def sum_lists(head_1: Node, head_2: Node) -> Node:
    """
    The lists are given in reverse order of the number. For example,
    if the number is 91321, the linked list will be: 1 -> 2 -> 3 -> 1 -> 9

    Returns:
        The head node of a linked list that is the sum the two input
        linked lists.
    """

    carry: bool = False
    sum_list: List[Node] = []

    node_1: Optional[Node] = head_1
    node_2: Optional[Node] = head_2

    while node_1 or node_2:
        node_1_val: int = node_1.data if node_1 else 0
        node_2_val: int = node_2.data if node_2 else 0
        sum_val: int = node_1_val + node_2_val

        if carry:
            sum_val += 1
            carry = False

        if sum_val >= 10:
            sum_val -= 10
            carry = True

        sum_list.append(Node(sum_val))

        node_1 = node_1.next if node_1 else None
        node_2 = node_2.next if node_2 else None

    for i in range(len(sum_list) - 1):
        sum_list[i].next = sum_list[i+1]

    return sum_list[0]


# Time Complexity: O(n)
# Space Complexity: O(n)
def sum_lists_reverse(head_1: Node, head_2: Node) -> Node:
    """
    The lists are given in the same order as the number. For example,
    if the number is 91321, the linked list will be 9 -> 1 -> 3 -> 2 -> 1

    Returns:
        The head of a linked list that is the sum of the two input
        linked lists.
    """
    def _sum_lists_reverse_helper(head: Node) -> Node:
        """
        Helper for sum_lists_reverse.
        """
        prev: Optional[Node] = None
        curr: Optional[Node] = head
        nex: Optional[Node] = head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            nex = nex.next if nex else None

        return prev

    head_1_rev = _sum_lists_reverse_helper(head_1)
    head_2_rev = _sum_lists_reverse_helper(head_2)

    return _sum_lists_reverse_helper(sum_lists(head_1_rev, head_2_rev))


class TestSumLists():

    @pytest.fixture
    def create_lists(self) -> Tuple[Callable, Callable]:
        def _create_lists(start_1: int, hop_1: int, max_1: int, start_2: int, hop_2: int, max_2: int) -> Tuple[Node, Node]:
            ll_1: LinkedList = LinkedList(Node(start_1))
            ll_2: LinkedList = LinkedList(Node(start_2))
            i: int = start_1 + hop_1
            j: int = start_2 + hop_2

            while i < max_1:
                ll_1.append(Node(i))
                i += hop_1

            while j < max_2:
                ll_2.append(Node(j))
                i += hop_2

            return ll_1.head, ll_2.head

        return _create_lists

    def test_sum_lists_with_fixture(self, create_lists):
        s_1, s_2 = create_lists(1, 2, 6, 3, 2, 1)
        head = sum_lists(s_1, s_2)

        assert head.data == 4
        assert head.next.data == 3
        assert head.next.next.data == 5

    def test_sum_lists(self):
        ll_1 = LinkedList(Node(1))
        ll_2 = LinkedList(Node(7))

        ll_1.append(Node(2))
        ll_1.append(Node(3))
        ll_1.append(Node(1))
        ll_1.append(Node(9))

        ll_2.append(Node(8))
        ll_2.append(Node(7))

        sum_head = sum_lists(ll_1.head, ll_2.head)

        assert sum_head.data == 8
        assert sum_head.next.data == 0
        assert sum_head.next.next.data == 1
        assert sum_head.next.next.next.data == 2
        assert sum_head.next.next.next.next.data == 9

    def test_sum_lists_reversed(self):
        ll_1 = LinkedList(Node(9))
        ll_2 = LinkedList(Node(7))

        ll_1.append(Node(1))
        ll_1.append(Node(3))
        ll_1.append(Node(2))
        ll_1.append(Node(1))

        ll_2.append(Node(8))
        ll_2.append(Node(7))

        sum_head = sum_lists_reverse(ll_1.head, ll_2.head)

        assert sum_head.data == 9
        assert sum_head.next.data == 2
        assert sum_head.next.next.data == 1
        assert sum_head.next.next.next.data == 0
        assert sum_head.next.next.next.next.data == 8
