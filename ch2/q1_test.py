import pytest

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_dups(head: Node) -> None:
    """
    Purpose:
        Removes all duplicates in linked list.
    """
    data_collected: dict = dict()

    prev: Node = head 
    curr: Node = head 
    while curr:
        if curr.data in data_collected:
            prev.next = curr.next

        else:
            data_collected[curr.data] = True
            prev = curr

        curr = curr.next
    

class TestRemoveDups():

    def test_simple_linked_list(self) -> None:
        head = Node(1)
        head.next = Node(1)

        remove_dups(head)
        assert head.next is None
    
    def test_no_duplicates(self) -> None:
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        remove_dups(head)
        i = 0
        curr = head
        while curr:
            i += 1
            curr = curr.next

        assert i == 5
    
    def test_many_duplicates(self) -> None:
        head = Node('hah')
        head.next = Node('nah')
        head.next.next = Node('hah')
        head.next.next.next = Node('nah')

        remove_dups(head)
        i = 0
        curr = head
        while curr:
            i += 1
            curr = curr.next

        assert i ==  2

    def test_only_head(self) -> None:
        head = Node(True)

        remove_dups(head)

        assert head.next is None
        assert head.data is True
    
    def test_duplicate_at_end(self) -> None:
        head = Node('a')
        head.next = Node('A')
        head.next.next = Node('B')
        head.next.next.next = Node('c')
        head.next.next.next.next = Node('a')


        assert head.next.next.next.next.data is 'a'
        remove_dups(head)
        assert head.next.next.next.next is None