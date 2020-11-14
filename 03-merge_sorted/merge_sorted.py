from linked_list import LinkedListNode
from linked_list import create_linked_list
from linked_list import print_linked_list


def merge_sorted(head1, head2):
    if head1 is None and head2 is None:
        return None
    elif head1 is None:
        return head2
    elif head2 is None:
        return head1

    merged = None
    curr = None
    curr1 = head1
    curr2 = head2
    while curr1 != None and curr2 != None:
        if curr1.data <= curr2.data:
            if merged == None:
                # init list and advance curr1
                merged = curr1
                curr1 = curr1.next
                # set list curr pointer
                curr = merged
                curr.next = None
            else:
                # append list and advance curr1
                curr.next = curr1
                curr1 = curr1.next
                # advance list curr pointer
                curr = curr.next
                curr.next = None
        else: # curr2.data < curr1.data
            if merged == None:
                # init list and advance curr2
                merged = curr2
                curr2 = curr2.next
                # set list curr pointer
                curr = merged
                curr.next = None
            else:
                # append list and advance curr2
                curr.next = curr2
                curr2 = curr2.next
                # advance list curr pointer
                curr = curr.next
                curr.next = None

    if curr1 == None:
        # exhausted head1, append rest of head2
        curr.next = curr2
    else: # curr2 == None
        curr.next = curr1

    # merged is head of merged list
    return merged


def main():
    head1 = create_linked_list([4,8,15,19])
    head2 = create_linked_list([7,9,10,16])
    print("head1: " + print_linked_list(head1))
    print("head2: " + print_linked_list(head2))
    head1 = merge_sorted(head1, head2)
    print("merged (head1): " + print_linked_list(head1))


if __name__ == "__main__":
    main()

