class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertTail(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: If the list is empty, the new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Step 3: Otherwise, find the last node
        current_node = self.head
        while current_node.next_element is not None:  # Traverse until the last node
            current_node = current_node.next_element

        # Step 4: Make the last node point to the new node
        current_node.next_element = new_node

    def PrintList(self):
        # Start from the head
        current_node = self.head
        if not current_node:  # If the list is empty
            print("List is empty!")
            return

        # Traverse and print each node's data
        while current_node:
            print(current_node.data, end=" -> " if current_node.next_element else " -> None")
            current_node = current_node.next_element
        print()  # Newline at the end


linked_list = LinkedList()

linked_list.InsertTail(10)
linked_list.InsertTail(20)
linked_list.InsertTail(30)
linked_list.InsertTail(40)


linked_list.PrintList()  # Expected output: 10 -> 20 -> 30 -> 40 -> None
