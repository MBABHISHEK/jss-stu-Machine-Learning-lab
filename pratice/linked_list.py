class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        prev_node = None
        index = 0
        while current_node and index < position:
            prev_node = current_node
            current_node = current_node.next
            index += 1
        prev_node.next = new_node
        new_node.next = current_node

    def delete(self, key):
        current_node = self.head
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Element not found in the list")
            return
        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def menu(self):
        while True:
            print("\nLinked List Operations:")
            print("1. Append")
            print("2. Insert")
            print("3. Delete")
            print("4. Search")
            print("5. Display")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                data = int(input("Enter the data to append: "))
                self.append(data)
            elif choice == 2:
                data = int(input("Enter the data to insert: "))
                position = int(input("Enter the position to insert: "))
                self.insert(data, position)
            elif choice == 3:
                key = int(input("Enter the data to delete: "))
                self.delete(key)
            elif choice == 4:
                key = int(input("Enter the data to search: "))
                if self.search(key):
                    print("Element found in the linked list")
                else:
                    print("Element not found in the linked list")
            elif choice == 5:
                print("Linked list:")
                self.display()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")


# Usage example:
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()

    # Show menu
    linked_list.menu()
