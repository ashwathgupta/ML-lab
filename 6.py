class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("\nLinked List Operations:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to insert at the beginning: ")
            linked_list.insert_at_beginning(data)
        elif choice == 2:
            data = input("Enter data to insert at the end: ")
            linked_list.insert_at_end(data)
        elif choice == 3:
            print("Linked List:")
            linked_list.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
