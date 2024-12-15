#Amanda New
#CSD325-A311
#JSON Practice
#Module 8

import json

class Student:

    def __init__(self, first_name, last_name, id_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.email = email

def load_students(student):

    with open(student.json, 'r') as file:
        try: 
            data = json.load(student)
        except FileNotFoundError:
            print(f"Error: student.json not found")
            return []
        
    students = []
    for student_data in data:
        students.append(Student(student_data['first_name'],
                                student_data['last_name'],
                                student_data['id_number'],
                                student_data['email']))
        
    return students

def print_students(message, students):
    
    print(message)
    for student in students:
        print(f"{student.first_name} {student.last_name} : ID = {student.id_number}, Email = {student.email}")

def update_students(students, new_student):

    students.append(new_student)
    return students

def save_students(students):

    with open (students.json, 'w') as file:
        json.dump([student.__dict__ for student in students], file, indent=4)
        print(f"File 'student.json' updated successfully")

print_students()





    



