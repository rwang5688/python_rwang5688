class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(A):
    length = len(A)
    if length == 0:
        return None

    head = None
    curr = None
    i = 0
    while i < length:
        node = LinkedListNode(A[i])
        if head == None:
            head = node
            curr = node
        else:
            curr.next = node
            curr = node
        i = i + 1

    return head


def print_linked_list(head):
    if head == None:
        return "Linked List is empty."

    result = "Linked List Nodes: "
    curr = head
    while curr != None:
        if curr == head:
            result = result + str(curr.data)
        elif curr.next != None:
            result = result + ", " + str(curr.data)
        else: # curr is tail
            result = result + ", " + str(curr.data) + "."
        curr = curr.next

    return result

