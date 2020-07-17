class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        if node is None:
            return
        # how will i get to the next node on every recursive iteration
        # just set next to previous?
        # so kind of like the iterative way to just do while next node isnt none then RECURSION
        # but if the last nodes next node isnt anything then were at the end so thats the new head
        # how would i reverse this back?
        next_node = node.get_next()
        node.set_next(prev)

        if next_node is not None:
            self.reverse_list(next_node, node)
        if next_node is None:
            self.head = node
