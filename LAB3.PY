# Undo-Redo System using Two Stacks in Python

class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = []  # Stores actions performed
        self.redo_stack = []  # Stores actions undone

    def push(self, action):
        """Perform a new action and clear redo history"""
        self.undo_stack.append(action)
        self.redo_stack.clear()
        print(f"Action Performed '{action}' added.")

    def undo(self):
        """Undo the last action"""
        if not self.undo_stack:
            print("No action to undo.")
            return
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        print(f"Undo: '{action}' undone.")

    def redo(self):
        """Redo the last undone action"""
        if not self.redo_stack:
            print("No action to redo.")
            return
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        print(f"Redo: '{action}' reapplied.")

    def display(self):
        """Display current status of both stacks"""
        print("\n--- Current System State ---")
        print("Undo Stack:", self.undo_stack if self.undo_stack else "Empty")
        print("Redo Stack:", self.redo_stack if self.redo_stack else "Empty")
        print("----------------------------\n")


# --- Driver Code ---
if __name__ == "__main__":
    system = UndoRedoSystem()

    while True:
        print("1. Push Action")
        print("2. Undo")
        print("3. Redo")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            action = input("Enter action to perform: ")
            system.push(action)

        elif choice == '2':
            system.undo()

        elif choice == '3':
            system.redo()

        elif choice == '4':
            system.display()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Try again.")
