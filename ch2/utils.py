class Node():
    def __init__(self, data, nex=None):
        self.data = data
        self.next = nex


class LinkedList():
    def __init__(self, head: Node):
        self.head: Node = head

    def append(self, node: Node) -> None:
        curr: Node = self.head
        while curr.next:
            curr = curr.next

        curr.next = node
