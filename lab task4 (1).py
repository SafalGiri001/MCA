class Student:
    def __init__(self, faculty, subjects):
        self.faculty = faculty
        self.subjects = subjects

    def display(self):
        print("Faculty:", self.faculty)
        print("Subjects:", self.subjects)

student1 = Student("Computer Science", {"Python": 80, "Database": 75})
student2 = Student("Information Technology", {"Java": 85, "Networking": 78})

student1.display()
student2.display()