class Node:
    def __init__(self, dataval=None, nextval=None):
        self.dataval = dataval
        self.nextval = nextval  # points to the next node


# these will be the memeber function used on the linked list
class SLinkedList:
    def __init__(self):
        self.head = None

    def removeNthfromend(self, head: Node, n: int) -> Node:
        dummy = Node(0, head)
        left = dummy
        right = head
