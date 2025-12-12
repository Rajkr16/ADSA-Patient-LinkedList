class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class AirlineReservation:
    def __init__(self):
        self.head = None

    # Insert name alphabetically
    def reserve_ticket(self):
        name = input("Enter passenger name: ")
        new_node = Node(name)

        # If list is empty OR insert at beginning
        if self.head is None or name < self.head.name:
            new_node.next = self.head
            self.head = new_node
            print("Ticket reserved successfully.")
            return

        temp = self.head
        # Find correct alphabetical position
        while temp.next is not None and temp.next.name < name:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        print("Ticket reserved successfully.")

    # Delete a reservation
    def cancel_reservation(self):
        name = input("Enter passenger name to cancel: ")

        if self.head is None:
            print("No reservations.")
            return

        # Delete first node
        if self.head.name == name:
            self.head = self.head.next
            print("Reservation cancelled.")
            return

        temp = self.head
        while temp.next is not None and temp.next.name != name:
            temp = temp.next

        if temp.next is None:
            print("Name not found.")
        else:
            temp.next = temp.next.next
            print("Reservation cancelled.")

    # Check if a reservation exists
    def check_reservation(self):
        name = input("Enter passenger name to check: ")
        temp = self.head

        while temp is not None:
            if temp.name == name:
                print(f"Ticket is reserved for {name}.")
                return
            temp = temp.next

        print("No reservation found.")

    # Display all passengers
    def display_passengers(self):
        if self.head is None:
            print("No passengers.")
            return

        temp = self.head
        print("Passenger List:")
        while temp is not None:
            print(temp.name)
            temp = temp.next


def main():
    system = AirlineReservation()

    while True:
        print("\n--- Airline Ticket Reservation System ---")
        print("1. Reserve Ticket")
        print("2. Cancel Reservation")
        print("3. Check Reservation")
        print("4. Display Passengers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.reserve_ticket()
        elif choice == "2":
            system.cancel_reservation()
        elif choice == "3":
            system.check_reservation()
        elif choice == "4":
            system.display_passengers()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
