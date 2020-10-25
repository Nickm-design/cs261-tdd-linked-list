# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:

    def __init__(self, value=None):
        self.prev = self
        self.value = value
        self.next = self

    def is_sentinel(self):
        if self.value == None:
            return True
        else:
            return False
    
    def is_empty(self):
        if self.prev != self or self.next != self:
            return False
        return self.is_last()
    
    def is_last(self):
        return self.is_sentinel()

    def last(self):
        return self

    def append(self, value):
        if self.is_empty():
            self.prev = value
        self.next = value
