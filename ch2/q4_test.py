import pytest
from typing import Optional

class Node():
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional[Node] = None
    
class LinkedList():
    def __init__(self, head: Node):
        self.head: Node = head
        self.tail: Node = head
        self.count = 1
    
    def append(self, node: Node) -> None:
        self.tail = node
        self.count += 1

        curr: Node = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node
    

def partition(linked_list: LinkedList, p_val: int) -> None:
    count: int = linked_list.count
    i: int = 0

    prev: Node = linked_list.head
    curr: Node = linked_list.head
    while i < count:
        if curr.data > p_val:
            prev.next = curr.next
            curr.next = None
            linked_list.append(curr)

        prev = curr
        curr = curr.next


