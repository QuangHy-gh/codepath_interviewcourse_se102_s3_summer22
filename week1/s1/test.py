class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def deleteDuplicates(self, head):
        curr1 = self.head
        curr2 = self.head
        while curr1 is not None:
            while curr2:
                if curr2.next == curr1:
                    curr2.next = curr2.next.next
                curr2 = curr2.next
                if curr2.next is None:

                    curr1 = curr1.next
                    curr2.next = curr1.next

        return curr2


list = SLinkedList()
list.head = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
e4 = ListNode(2)
list.head.next = e2
e2.next = e3
e3.next = e4

list.deleteDuplicates(list.head)
list.listprint()
