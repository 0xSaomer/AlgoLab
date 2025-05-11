class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertHead(self, data):
        # Create a new node
        new_node = Node(data)
        # Point the new node to the current head
        new_node.next_element = self.head
        # Update head to point new_node
        self.head = new_node

    def PrintList(self):
        # Start from the head
        current_node = self.head
        if not current_node:  # If the list is empty
            print("List is empty!")
            return

        # Traverse the list and print each node's data
        while current_node:
            print(current_node.data, end=" -> " if current_node.next_element else " -> None")
            current_node = current_node.next_element
        print()  # For a clean new line after printing the list


linked_list = LinkedList()

linked_list.InsertHead(10)
linked_list.InsertHead(20)
linked_list.InsertHead(30)

linked_list.PrintList()  # Expected output: 30 -> 20 -> 10 -> None