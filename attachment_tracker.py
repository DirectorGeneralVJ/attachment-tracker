import os


class AttachmentTracker:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_student(self, name, year, course):
        student = {
            "name": name.strip(),
            "year": year.strip(),
            "course": course.strip()
        }
        self.students.append(student)
        print("Student added successfully.")

    def list_students(self):
        if not self.students:
            print("No students recorded yet.")
            return

        print("\n--- Registered Students ---")
        for index, student in enumerate(self.students, start=1):
            print(
                f"{index}. {student['name']} | Year {student['year']} | {student['course']}"
            )

    def search_by_course(self, course_name):
        course_name = course_name.lower()
        results = [
            student for student in self.students
            if student["course"].lower() == course_name
        ]

        if not results:
            print(f"No students found for course: {course_name}")
            return

        print(f"\n--- Students in {course_name} ---")
        for student in results:
            print(
                f"{student['name']} | Year {student['year']} | {student['course']}"
            )

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                line = f"{student['name']},{student['year']},{student['course']}\n"
                file.write(line)

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                name, year, course = line.strip().split(",")
                self.students.append({
                    "name": name,
                    "year": year,
                    "course": course
                })


def show_menu():
    print("\n--- Attachment Tracker Menu ---")
    print("1. Add student")
    print("2. View students")
    print("3. Search students by course")
    print("4. Exit")


def main():
    tracker = AttachmentTracker()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter student name: ")
            year = input("Enter student year: ")
            course = input("Enter student course: ")

            tracker.add_student(name, year, course)
            tracker.save_to_file()

        elif choice == "2":
            tracker.list_students()

        elif choice == "3":
            course_name = input("Enter course name to search: ")
            tracker.search_by_course(course_name)

        elif choice == "4":
            tracker.save_to_file()
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
