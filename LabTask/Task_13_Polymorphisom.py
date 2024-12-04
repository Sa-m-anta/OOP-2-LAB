class Department:
    def __init__(self, department_name):
        self.department_name = department_name

    def display_name(self):
        print(f"Department Name: {self.department_name}")


class Teacher(Department):
    def __init__(self, department_name, class_schedule):
        super().__init__(department_name)
        self.class_schedule = class_schedule

    def schedule_class(self):
        print(f"Class Scheduled: {self.class_schedule}")

    def grade_students(self):
        print("Grading Assignments...")

    def display_name(self):
        super().display_name()
        print("Role: Teacher")


class Author:
    def write_content(self):
        print("Drafting Content...")

    def publish_material(self):
        print("Publishing Learning Materials...")


class TeacherAuthor(Teacher, Author):
    def __init__(self, department_name, class_schedule):
        Teacher.__init__(self, department_name, class_schedule)

    def display_name(self):
        Teacher.display_name(self)
        print("Role: Teacher and Author")


# Create an instance of TeacherAuthor
teacher_author = TeacherAuthor("Mathematics", "Monday 10 AM")

# Access methods
teacher_author.schedule_class()
teacher_author.grade_students()
teacher_author.write_content()
teacher_author.publish_material()
teacher_author.display_name()
