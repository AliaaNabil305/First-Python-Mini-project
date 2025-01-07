class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_student_info(self):
        """Displays the student's name, age, and grades."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
    
    def calculate_average_grade(self):
        """Calculates the average of the student's grades."""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        """Adds a new student to the database."""
        self.students.append(student)
    
    def display_all_students(self):
        """Displays information about all students in the database."""
        for student in self.students:
            student.display_student_info()
            print(f"Average Grade: {student.calculate_average_grade():.2f}\n")

student_db = StudentDatabase()
student1 = Student("John Doe", 20, [85, 90, 92])
student_db.add_student(student1)
student2 = Student("Jane Smith", 22, [88, 93, 89, 91])
student_db.add_student(student2)

student_db.display_all_students()

