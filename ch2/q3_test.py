import pytest

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self, head: Node):
        self.head: Node = head
    
    def append(self, node: Node) -> None:
        curr: Node = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node

# Time Complexity: O(1)
# Space Complexity: O(1)
# More accurate to say O(data)
def delete_middle_node(node: Node) -> None:
    """
    Assumptions:
        Given a node that is not the first or last node.
    Purpose:
        Deletes given node.
    """
    node.data = node.next.data
    node.next = node.next.next


class TestDeleteMiddleNode():

    @pytest.fixture
    def head(self):
        """
        Initialize linked list.
        """
        head = Node(1)
        linked_list = LinkedList(head)

        linked_list.append(Node('hello'))
        linked_list.append(Node('why'))
        linked_list.append(Node('34'))
        linked_list.append(Node('0293148'))
        linked_list.append(Node(2034820))
        linked_list.append(Node(True))
        linked_list.append(Node(False))

        return head
    
    def test_remove_34_from_linked_list(self, head):
        delete_middle_node(head.next.next.next)

        assert head.next.next.next.data == '0293148'
    
    def test_remove_why_from_linked_list(self, head):
        delete_middle_node(head.next.next)

        assert head.next.next.data == '34'
    
    def test_remove_true_from_linked_list(self, head):
        delete_middle_node(head.next.next.next.next.next.next)

        assert head.next.next.next.next.next.next.data is False
    
    def test_remove_hello_from_linked_list(self, head):
        delete_middle_node(head.next)

        assert head.data == 1
        assert head.next.data == 'why'
        assert head.next.next.data == '34'
        assert head.next.next.next.data == '0293148'
        assert head.next.next.next.next.data == 2034820
        assert head.next.next.next.next.next.data == True
        assert head.next.next.next.next.next.next.data == False
        assert head.next.next.next.next.next.next.next is None