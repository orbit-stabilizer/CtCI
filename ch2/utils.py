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
