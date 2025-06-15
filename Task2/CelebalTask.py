class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        if current is None:
            print("List is empty.")
            return

        while current:
            print(current.data, end=' -> ' if current.next else '\n')
            current = current.next

    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise ValueError("Index must be a positive integer.")

            if n == 1:
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if current is None or current.next is None:
                raise IndexError("Index out of range.")

            current.next = current.next.next

        except (IndexError, ValueError) as e:
            print(f"Error: {e}")


# User interaction
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\nOptions:")
        print("1. Add node")
        print("2. Delete nth node")
        print("3. Print list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = input("Enter data to add: ")
            ll.add_to_end(data)
        elif choice == '2':
            try:
                n = int(input("Enter the position to delete (1-based index): "))
                ll.delete_nth_node(n)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            ll.print_list()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")
