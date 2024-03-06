class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def display(self):
        self._display_recursive(self.root)
        print()

    def _display_recursive(self, node):
        if node is not None:
            self._display_recursive(node.left)
            print(node.key, end=' ')
            self._display_recursive(node.right)

    def menu(self):
        while True:
            print("\nBinary Search Tree Operations:")
            print("1. Insert")
            print("2. Search")
            print("3. Display")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                key = int(input("Enter the key to insert: "))
                self.insert(key)
            elif choice == '2':
                key = int(input("Enter the key to search: "))
                if self.search(key):
                    print("Key {} found in the binary search tree.".format(key))
                else:
                    print("Key {} not found in the binary search tree.".format(key))
            elif choice == '3':
                print("Binary Search Tree:")
                self.display()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

# Usage example:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.menu()
