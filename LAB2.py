#Convert The Patient List to A Circular Linked List for a Round-Robin Check-Up System. Implement Insertion and Deletion.


class Patient:
    def __init__(self, name):
        self.name = name
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert new patient
    def insert_patient(self, name):
        new_patient = Patient(name)
        if self.head is None:
            self.head = new_patient
            new_patient.next = self.head
            print(f" Patient '{name}' added successfully.")
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_patient
        new_patient.next = self.head
        print(f"Patient '{name}' added successfully.")

    # Delete patient by name
    def delete_patient(self, name):
        if self.head is None:
            print(" No patients in the list.")
            return

        curr = self.head
        prev = None

        # Case 1: deleting head node
        if curr.name == name:
            # Only one node
            if curr.next == self.head:
                self.head = None
                print(f"Deleted last patient: {name}")
                return

            # Find last node to maintain circular link
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = curr.next
            last.next = self.head
            print(f" Deleted patient: {name}")
            return

        # Case 2: deleting non-head node
        prev = curr
        curr = curr.next
        while curr != self.head and curr.name != name:
            prev = curr
            curr = curr.next

        if curr == self.head:
            print(f" Patient '{name}' not found.")
            return

        prev.next = curr.next
        print(f" Deleted patient: {name}")

    # Display all patients
    def display_patients(self):
        if self.head is None:
            print(" No patients in the list.")
            return

        temp = self.head
        print("\n🩺 Patient List (Circular): ", end="")
        while True:
            print(temp.name, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to Head)\n")

    # Round-Robin Check-Up simulation
    def round_robin_checkup(self, rounds):
        if self.head is None:
            print(" No patients to check.")
            return

        temp = self.head
        print("\n --- Round Robin Check-Up ---")
        for i in range(1, rounds + 1):
            print(f"Round {i}: Checking {temp.name}")
            temp = temp.next
        print("------------------------------\n")


# -------------------------------
#  Menu-Driven Program
# -------------------------------
def main():
    cll = CircularLinkedList()

    while True:
        print("======== ROUND ROBIN PATIENT SYSTEM ========")
        print("1. Add Patient")
        print("2. Delete Patient")
        print("3. Display Patients")
        print("4. Round-Robin Check-Up")
        print("5. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter patient name: ")
            cll.insert_patient(name)

        elif choice == '2':
            name = input("Enter patient name to delete: ")
            cll.delete_patient(name)

        elif choice == '3':
            cll.display_patients()

        elif choice == '4':
            if cll.head is None:
                print(" No patients for check-up.")
            else:
                rounds = int(input("Enter number of rounds: "))
                cll.round_robin_checkup(rounds)

        elif choice == '5':
            print(" Exiting... Stay healthy!")
            break

        else:
            print(" Invalid choice! Please enter 1-5.")

        print()  # spacing between menu loops


# Run the program
if __name__ == "__main__":
    main()
