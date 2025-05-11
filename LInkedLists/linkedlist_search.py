class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None

        # Insert Tail

    def InsertTail(self, data):
        # Create new node
        new_node = Node(data)
        # Check if list is empty
        if self.head is None:
            self.head = new_node
            return

        # find out the tail
        current_node = self.head
        while current_node.next_element:
            current_node = current_node.next_element

        current_node.next_element = new_node

    def Search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next_element
        return False

        # print the list
    def PrintList(self):
        current_node = self.head
        if self.head is None:
            print("list is empty")
            return

        # loop through the list
        while current_node:
            print(current_node.data, end="->" if current_node.next_element else " -> None")
            current_node = current_node.next_element
        print()


list = LinkedList()
list.InsertTail(10)
list.InsertTail(20)
list.InsertTail(30)
list.PrintList()
print(list.Search(20))