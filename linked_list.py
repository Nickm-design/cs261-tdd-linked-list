# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Nick Morris

class LinkedList:

    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self
        
    def is_sentinel(self):
        return self.value == None
    
    def is_empty(self):
        return self.prev == self and self.next == self
    
    def is_last(self):
        return self.next.is_sentinel()

    def last(self):
        return self.prev

    def append(self, node):
        last = self.prev
        last.next = node
        node.prev = last
        node.next = self
        self.prev = node

    def delete(self):
        left = self.prev
        right = self.next
        left.next = right
        right.prev = left
        
    def insert(self, node):
        pass