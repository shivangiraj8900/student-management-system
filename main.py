def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    with open("students.txt", "a") as f:
        f.write(name + "," + roll + "\n")

    print("Student added successfully")

while True:
    print("1 Add Student")
    print("2 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        break
