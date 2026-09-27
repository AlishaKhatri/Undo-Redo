# Import the Node class you created in node.py
from node import Node


# Implement your Stack class here
class Stack:
    def __init__(self):
        # The top of the stack starts empty
        self.top = None

    def push(self, value):
        # Create a new node
        new_node = Node(value)

        # Point the new node to the current top
        new_node.next = self.top

        # Make the new node the new top
        self.top = new_node

    def pop(self):
        # If stack is empty, return None
        if self.top is None:
            return None

        # Save the value at the top
        value = self.top.value

        # Move the top pointer to the next node
        self.top = self.top.next

        return value

    def peek(self):
        # If stack is empty, return None
        if self.top is None:
            return None

        return self.top.value

    def print_stack(self):
        # Check if stack is empty
        if self.top is None:
            print("Stack is empty.")
            return

        # Start at the top of the stack
        current = self.top

        # Print every value from top to bottom
        while current is not None:
            print(f"- {current.value}")
            current = current.next


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")

            # Push the action onto the undo stack
            undo_stack.push(action)

            # Clear the redo stack when a new action happens
            redo_stack = Stack()

            print(f"Action performed: {action}")

        elif choice == "2":
            # Pop an action from the undo stack
            action = undo_stack.pop()

            # If an action exists, move it to redo stack
            if action is not None:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo")

        elif choice == "3":
            # Pop an action from the redo stack
            action = redo_stack.pop()

            # If an action exists, move it back to undo stack
            if action is not None:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo")

        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_undo_redo()