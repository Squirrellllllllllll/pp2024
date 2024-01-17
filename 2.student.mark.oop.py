class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.marks = {}

class Marks:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        self.students = [
            Student(input("Enter student ID: "), 
                    input("Enter student name: "), 
                    input("Enter student DoB: ")) for _ in range(num_students)]

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        self.courses = [
            Course(input("Enter course ID: "), 
                   input("Enter course name: ")) for _ in range(num_courses)]

    def input_marks(self):
        for course in self.courses:
            print(f"\nEnter marks for course: {course.name} ({course.course_id})")
            for student in self.students:
                course.marks[student.student_id] = float(input(f"Enter mark for student {student.name}: "))

    def list_courses(self):
        print("\nList of Courses:")
        for i, course in enumerate(self.courses, start=1):
            print(f"{i}. {course.name}({course.course_id})")

    def list_students(self):
        print("\nList of Students:")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. ID: {student.student_id} - Name: {student.name}, DoB: {student.dob}")

    def show_student_marks(self):
        print("\nStudent's Marks:")
        for i, course in enumerate(self.courses, start=1):
            print(f"{i}.{course.name} ({course.course_id}): ")
            for student in self.students:
                marks = course.marks.get(student.student_id, 'Input mark for student in this course')
                print(f"   {student.name}: {marks}")


if __name__ == "__main__":
    mark_system = Marks()

    mark_system.input_students()
    mark_system.input_courses()

    mark_system.input_marks()
    mark_system.list_courses()
    mark_system.list_students()
    mark_system.show_student_marks()
