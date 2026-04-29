import os

class StudentManager:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def add_student(self):
        """Adds a new student record to the file."""
        name = input("Enter student name: ").strip()
        while True:
            try:
                marks = float(input("Enter marks: "))
                break
            except ValueError:
                print("❌ Invalid input. Please enter a numeric value for marks.")

        try:
            with open(self.filename, "a") as f:
                f.write(f"{name},{marks}\n")
            print(f"✅ Record for {name} added successfully!")
        except IOError as e:
            print(f"❌ Error writing to file: {e}")

    def view_students(self):
        """Reads and displays all student records."""
        if not os.path.exists(self.filename):
            print("📝 No records found. Start by adding a student!")
            return

        print(f"\n--- {'Student Records':^20} ---")
        try:
            with open(self.filename, "r") as f:
                records = f.readlines()
                if not records:
                    print("The file is empty.")
                    return
                
                for line in records:
                    name, marks = line.strip().split(",")
                    print(f"👤 Name: {name:<10} | 🎓 Marks: {marks}")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
        print("-" * 30)

def main():
    manager = StudentManager()
    
    menu = {
        "1": manager.add_student,
        "2": manager.view_students,
        "3": exit
    }

    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        action = menu.get(choice)
        if action:
            if choice == "3":
                print("Goodbye!")
                action()
            action()
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
