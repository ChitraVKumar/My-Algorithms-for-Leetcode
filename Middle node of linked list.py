class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head_node(self, value):
        self.head = Node(value, self.head)

    def add_tail_node(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value, None)

    def length_of_LL(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        liked_list = ''
        while current:
            liked_list += str(current.value) + '-->'
            current = current.next

        print(liked_list)

    def middle_of_LL(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        print(count)

        middle = count // 2

        #if middle % 2 == 0:
        new_head = middle + 1
        linked_list = ''
        c = 1
        current = self.head
        while current:
            if c == new_head:
                linked_list += str(current.value) + '-->'
                current = current.next
                continue

            c += 1
            current = current.next
        print(linked_list)
        #else:
        # new_head = middle + 1
        # linked_list = ''
        # c = 1
        # current = self.head
        # while current:
        #     if c == new_head:
        #         linked_list += str(current.value) + '-->'
        #         current = current.next
        #         continue
        #
        #     c += 1
        #     current = current.next
        # print(linked_list)

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_head_node(1)
    ll.add_tail_node(2)
    ll.add_tail_node(3)
    ll.add_tail_node(4)
    ll.add_tail_node(5)
    #ll.add_tail_node(6)

    ll.printLL()
    ll.middle_of_LL()

