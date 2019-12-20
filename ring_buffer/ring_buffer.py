from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # buffer cap
        self.current = None
        self.storage = DoublyLinkedList()
        # self.next = None
        # self.prev = None

    def append(self, item):
        # WHY DOESNT THIS WORK!!!! NVM didnt set to next oldest
        # if buffer full
        if self.storage.length == self.capacity:
            # Make item oldest
            self.current.value = item
            # if tail is oldest
            if self.current is self.storage.tail:
                # Make it the new head
                self.current = self.storage.head
            else:  # it becomes the next
                self.current = self.current.next

        elif self.storage.length < self.capacity:
            # Add item to fail
            self.storage.add_to_tail(item)
            # head is next oldest item
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer = []
        tmp = self.storage.head
        while tmp:
            list_buffer.append(tmp.value)
            tmp = tmp.next
        return list_buffer

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
