def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    with open("data.txt", "a") as f:
        f.write(f"{name},{marks}\n")

def view_students():
    try:
        with open("data.txt", "r") as f:
            for line in f:
                name, marks = line.strip().split(",")
                print(f"Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("No records found.")

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")