


students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }
    students.append(student)
    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return
    print("\nList of Students:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Roll No: {student['roll_no']}, Course: {student['course']}")

def update_student():
    roll_no = input("Enter roll number of the student to update: ")
    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            print("Student updated successfully.")
            return
    print("Student not found.")

def delete_student():
    roll_no = input("Enter roll number of the student to delete: ")
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully.")
            return
    print("Student not found.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
