class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def append(self, data):
        for i in range(self.size):
            if self.array[i] is None:
                self.array[i] = data
                return
        print("Array is full, cannot append element")

    def insert(self, data, position):
        if position < 0 or position >= self.size:
            print("Invalid position")
            return
        if self.array[position] is not None:
            print("Position already occupied")
            return
        self.array[position] = data

    def delete(self, data):
        if data in self.array:
            index = self.array.index(data)
            self.array[index] = None
        else:
            print("Element not found in the array")

    def search(self, data):
        if data in self.array:
            print("Element found in the array")
        else:
            print("Element not found in the array")

    def display(self):
        print("Array:", self.array)

    def menu(self):
        while True:
            print("\nArray Operations:")
            print("1. Append")
            print("2. Insert")
            print("3. Delete")
            print("4. Search")
            print("5. Display")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                data = input("Enter the data to append: ")
                self.append(data)
            elif choice == 2:
                data = input("Enter the data to insert: ")
                position = int(input("Enter the position to insert: "))
                self.insert(data, position)
            elif choice == 3:
                data = input("Enter the data to delete: ")
                self.delete(data)
            elif choice == 4:
                data = input("Enter the data to search: ")
                self.search(data)
            elif choice == 5:
                self.display()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")


# Usage example:
if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    array = Array(size)
    array.menu()
