def input_students():
    num_students = int(input("Enter the number of students: "))
    return [
        (input("Enter student ID: "), 
         input("Enter student name: "), 
         input("Enter student DoB: ")) 
         for _ in range(num_students)]

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    return [
        {'id': input("Enter course ID: "), 
         'name': input("Enter course name: "), 
         'marks': {}} 
         for _ in range(num_courses)]

def input_marks(students, courses):
    for course in courses:
        print(f"\nEntering marks for course: {course['name']} ({course['id']})")
        for student in students:
            course['marks'][student[0]] = float(input(f"Enter mark for {student[1]}: "))

def list_courses(courses):
    print("\nList of Courses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course['id']}: {course['name']}")

def list_students(students):
    print("\nList of Students:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. ID: {student[0]} - Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(students, courses):
    for i, course in enumerate(courses, start=1):
        print(f"\n{i}. {course['name']} ({course['id']}) - Student Marks:")
        for student in students:
            marks = course['marks'].get(student[0], 'N/A (Not graded)')
            print(f"   {student[1]}: {marks}")

if __name__ == "__main__":
    students_list = input_students()
    courses_list = input_courses()

    input_marks(students_list, courses_list)
    list_courses(courses_list)
    list_students(students_list)
    show_student_marks(students_list, courses_list)
