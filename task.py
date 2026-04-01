# Student class
class Student:
    def __init__(self, student_id, name, course, attendance):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.attendance = attendance

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Attendance:", self.attendance, "%")
        print("-------------------------")


# Attendance System class
class AttendanceSystem:
    def __init__(self):
        self.students = []
        self.next_id = 1  # auto ID generator

    # Add student
    def add_student(self):
        name = input("Enter student name: ")
        course = input("Enter course name: ")
        attendance = float(input("Enter attendance (%): "))

        student = Student(self.next_id, name, course, attendance)
        self.students.append(student)

        print("Student added with ID:", self.next_id)
        self.next_id += 1

    # Display all students
    def display_all(self):
        if len(self.students) == 0:
            print("No records found.")
        else:
            for student in self.students:
                student.display()

    # Update student
    def update_student(self):
        search_id = int(input("Enter student ID to update: "))
        found = False

        for student in self.students:
            if student.student_id == search_id:
                print("Student found!")
                student.course = input("Enter new course: ")
                student.attendance = float(input("Enter new attendance (%): "))
                print("Record updated successfully.")
                found = True
                break

        if not found:
            print("Student not found.")

    # Calculate average attendance
    def average_attendance(self):
        if len(self.students) == 0:
            print("No records to calculate average.")
            return

        total = 0
        for student in self.students:
            total += student.attendance

        average = total / len(self.students)
        print("Average Attendance:", round(average, 2), "%")


# Main program
system = AttendanceSystem()

while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Average Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.display_all()
    elif choice == "3":
        system.update_student()
    elif choice == "4":
        system.average_attendance()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")