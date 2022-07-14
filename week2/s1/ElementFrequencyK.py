# Problem #1: Remove Duplicates from Sorted List

# Examples:

# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Input: 1->1->2
# Output: 1->2

# Input: 1->1->2->3->3
# Output: 1->2->3


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None  # points to the next node


# these will be the memeber function used on the linked list
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return None

    def RemovingDuplicates(self):

        ptr = self.head
        while ptr.nextval != None:
            if ptr.dataval == ptr.nextval.dataval:
                new = ptr.nextval.nextval
                ptr.next = None

                ptr.nextval = new
            else:
                ptr = ptr.nextval

    def PrintList(self):

        ptr = self.head

        while ptr != None:
            print(ptr.dataval)
            ptr = ptr.nextval


if __name__ == "__main__":
    llist = SLinkedList()

    llist.head = Node(1)

    second = Node(2)
    third = Node(2)

    fourth = Node(3)

    llist.head.nextval = second
    # Link first node with second
    second.nextval = third

    third.nextval = fourth
    llist.PrintList()

    llist.RemovingDuplicates()

    llist.PrintList()
