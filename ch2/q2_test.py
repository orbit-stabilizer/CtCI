import pytest

# Time Complexity: O(n)
# Space Complexity: O(1)
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def kth_to_last(head: Node, k: int) -> Node:
    """
    Assumptions:
        k will always be less than the size of the linked list.
    Returns:
        The kth last element in a singly linked list.
    """

    i: int = 0
    lead: Node = head
    follow: Node = head

    while i < k:
        lead = lead.next
        i += 1
    
    while lead.next:
        lead = lead.next
        follow = follow.next
    
    return follow


class TestKthToLast():

    @pytest.fixture
    def linked_list_five(self):
        """
        Returns the head of a linked list with 5 elements.
        All elements have ints as data.
        """
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        return head
    
    @pytest.fixture
    def linked_list_seven(self):
        """"
        Returns the head of a linked list with 7 elements.
        Elements have str, int, float, and bool as data.
        """
        head = Node('hey')
        head.next = Node(1)
        head.next.next = Node(True)
        head.next.next.next = Node(False)
        head.next.next.next.next = Node(932)
        head.next.next.next.next.next = Node('testing')
        head.next.next.next.next.next.next = Node(324.22)

        return head

    def test_five_long_small_k(self, linked_list_five):
        k = 0

        assert kth_to_last(linked_list_five, k).data == 5

    def test_five_medium_k(self, linked_list_five):
        k = 2

        assert kth_to_last(linked_list_five, k).data == 3
    
    def test_five_large_k(self, linked_list_five):
        k = 4

        assert kth_to_last(linked_list_five, k).data == 1
    
    def test_seven_small_k(self, linked_list_seven):
        k = 3

        assert kth_to_last(linked_list_seven, k).data is False
    
    def test_seven_large_k(self, linked_list_seven):
        k = 6

        assert kth_to_last(linked_list_seven, k).data == 'hey'