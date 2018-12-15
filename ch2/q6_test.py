from typing import List, Optional

from utils import Node


# Time Complexity: O(n)
# Space Complexity: O(n)
def palindrome(head: Node) -> bool:
    """
    Returns:
        True if linked list is a palindrome, else False.
    """
    acc: List[Node] = []  # accumulator
    node: Optional[Node] = head

    while node:
        acc.append(node.data)
        node = node.next

    return acc == acc[::-1]


class TestPalindrome():
    def test_palindrome_1(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)

        assert palindrome(head) is False

    def test_palindrome_2(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(1)

        assert palindrome(head) is True
