import os


class AttachmentTracker:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_student(self, name, year, course):
        student = {
            "name": name,
            "year": year,
            "course": course
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
    print("3. Exit")


def main():
    tracker = AttachmentTracker()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            name = input("Enter student name: ")
            year = input("Enter student year: ")
            course = input("Enter student course: ")

            tracker.add_student(name, year, course)
            tracker.save_to_file()

        elif choice == "2":
            tracker.list_students()

        elif choice == "3":
            tracker.save_to_file()
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
