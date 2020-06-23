# Written by Amritesh Singh for COMP9021

from quiz08_linked_list_adt import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L=None):
        super().__init__(L)

    def len(self):
        current_node = self.head
        length = 0

        while current_node:
            length += 1
            current_node = current_node.next_node

        return length

    def rearrange(self, step):
        length = self.len()

        if (step % length) > 1:
            list1 = LinkedList()
            list2 = LinkedList()
            ctr = 1
            temp_node1 = None
            temp_node2 = None
            current_node = self.head
            flag1 = False

            for i in range(length):
                flag = False

                while True:
                    if not ctr:
                        if not list1.head:
                            list1.head = current_node
                            temp_node1 = list1.head
                        else:
                            temp_node1.next_node = current_node
                            temp_node1 = temp_node1.next_node

                        flag = True
                    else:
                        if not list2.head:
                            list2.head = current_node
                            temp_node2 = list2.head
                        else:
                            temp_node2.next_node = current_node
                            temp_node2 = temp_node2.next_node

                    if not ctr:
                        flag1 = False

                    if not flag1:
                        ctr = (ctr + 1) % (step % length)
                    else:
                        ctr = (ctr + 1) % ((step + 1) % length)

                    if current_node.next_node:
                        current_node = current_node.next_node
                    else:
                        step -= 1

                        if step:
                            flag1 = True
                            current_node = list2.head
                            list2.head = None
                        else:
                            break

                    if flag:
                        break

                if not step:
                    break

            self.head = list1.head