class Student:
    def __init__(self, name, roll):
        # Initialize data members
        self.name = name
        self.roll = roll
        self.marks = []  # List to store marks

    def show_data(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
    
    def show_marks(self):
        if self.marks:
            print("Marks: ", end="")
            for mark in self.marks:
                print(mark, end=" ")
            print()  
        else:
            print("No marks available.")

    def set_marks(self, marks_list):
        self.marks = marks_list




student1 = Student("Soumali", "657")
student1.set_marks([85, 90, 92, 87])
student1.show_data()
student1.show_marks()
