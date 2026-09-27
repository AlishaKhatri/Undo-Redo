
from node import Node
class Queue:
    def __init__(self):
        # The queue starts empty
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # Create a new node
        new_node = Node(value)

        # If the queue is empty
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            # Add the new node to the end of the queue
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # If the queue is empty
        if self.front is None:
            return None

        # Save the value of the first customer
        value = self.front.value

        # Move front to the next customer
        self.front = self.front.next

        # If queue becomes empty, rear must also be None
        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        # Return the first customer without removing them
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        # If the queue is empty
        if self.front is None:
            print("Queue is empty.")
            return

        # Start at the front
        current = self.front

        # Print every customer in order
        while current is not None:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")

            # Add the customer to the queue
            queue.enqueue(name)

            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue
            customer = queue.dequeue()

            if customer is not None:
                print(f"Helped: {customer}")
            else:
                print("No customers waiting.")

        elif choice == "3":
            # Peek at the next customer in the queue
            customer = queue.peek()

            if customer is not None:
                print(f"Next customer: {customer}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
    
