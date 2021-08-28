"""
Linked lists stores elements in completly different locations in memory.
You don't need to pre-alocate space and the insertion is easier
These are great if you need to insert/delete elements at the start. 

"""


class Node:
    # represents element in the linked list
    def __init__(self, data=None, next=None):
        self.data = data  # the data that is stored
        self.next = next  # the pointer which points to the next element in linked list


class LinkedList:
    def __init__(self):
        self.head = None  # points to the head of the linked list

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        cur = self.head
        while cur:
            counter += 1
            cur = cur.next
        return counter

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        index_counter = 0
        cur = self.head
        while cur:
            if index_counter == index - 1:
                cur.next = cur.next.next
                break
            cur = cur.next
            index_counter += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        index_counter = 0
        cur = self.head
        while cur:
            if index_counter == index - 1:
                node = Node(data, cur.next)
                cur.next = node
                break

            cur = cur.next
            index_counter += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        cur = self.head
        while cur:
            if cur.data == data_after:
                node = Node(data_to_insert, cur.next)
                cur.next = node

            cur = cur.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                break
            cur = cur.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        cur = self.head
        linked_str = ''
        while cur:
            linked_str += str(cur.data) + ' ---> '
            cur = cur.next
        print(linked_str)

    def index_of(self, data):
        cur = self.head
        index_counter = 0
        while cur:
            if cur.data == data:
                return index_counter
            index_counter += 1
            cur = cur.next


class DoubleNode:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def get_last_node(self):
        cur = self.head
        while cur.next:
            cur = cur.next

        return cur

    def get_length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next

        return count

    def insert_at_begining(self, data):
        if self.head is None:
            node = DoubleNode(data, self.head, None)
            self.head = node
        else:
            node = DoubleNode(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = DoubleNode(data, None, None)
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = DoubleNode(data, None, cur)

    def insert_after_value(self, data_after, data_to_insert):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == data_after:
                self.insert_at_end(data_to_insert)
                return
            elif cur.data == data_after:
                node = DoubleNode(data_to_insert, cur.next, cur)
                cur.next = node
                cur.prev.next = node
            cur = cur.next

    def insert_before_value(self, data_before, data_to_insert):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == data_before:
                self.insert_at_begining(data_to_insert)
                return
            elif cur.data == data_before:
                node = DoubleNode(data_to_insert, cur, cur.prev)
                cur.prev = node
                cur.prev.prev.next = node

            cur = cur.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        cur = self.head
        while cur:
            if count == index - 1:
                node = DoubleNode(data, cur.next, cur)
                if node.next:
                    node.next.prev = node
                cur.next = node
                break

            cur = cur.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        cur = self.head
        while cur:
            if count == index:
                cur.prev.next = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                break

            cur = cur.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + ' --> '
            cur = cur.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        cur = last_node
        llstr = ''
        while cur:
            llstr += cur.data + '-->'
            cur = cur.prev
        print("Link list in reverse: ", llstr)
