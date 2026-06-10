class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a node with data and set next to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize head to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new node and insert it at the front of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Create a new node and insert it at the end of the list.
        """
        new_node = Node(data)

        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise traverse to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        """

        def helper(node):
            # Base case: end of list
            if node is None:
                return 0

            # Recursive case: current data + sum of rest
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        """

        def helper(prev, current):
            # Base case: current is None, prev is new head
            if current is None:
                return prev

            # Save next node
            next_node = current.next

            # Reverse pointer
            current.next = prev

            # Recurse forward
            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        Return True if target is found in the list, otherwise False.
        """

        def helper(node):
            # Base case: target not found
            if node is None:
                return False

            # Base case: target found
            if node.data == target:
                return True

            # Recursive case: search next node
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        Print the contents of the list in a readable format.
        Example: 1 -> 2 -> 3 -> None
        """
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        values.append("None")
        print(" -> ".join(values))