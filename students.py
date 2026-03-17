students = {}
def add_student(name, marks):
    students[name] = marks
    print("student added")

def display_students():
    for name, marks in students.items():
        print(name,":",marks)

add_student("anisha",90)
add_student("madhu",91)
display_students()
