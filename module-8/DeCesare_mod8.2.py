import json
import os

def load_students(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def print_students(student_list, message):
    print(f"\n{message}")
    for student in student_list:
        print(f"{student['F_Name']}, {student['L_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

def save_students(json_file, student_list):
    with open(json_file, 'w') as file:
        json.dump(student_list, file, indent=4)
    print("\nThe .json file was updated successfully.")

def main():
    json_file = os.path.join(os.path.dirname(__file__), 'students.json')

    # Load students from JSON file
    students = load_students(json_file)

    # Print original student list
    print_students(students, "Original Student List:")

    # Add new student
    new_student = {
        "F_Name": "Anton",
        "L_Name": "DeCesare",
        "Student_ID": 99999,
        "Email": "anton@example.com"
    }
    students.append(new_student)

    # Print updated student list
    print_students(students, "Updated Student List:")

    # Save updated list back to JSON file
    save_students(json_file, students)

if __name__ == "__main__":
    main()
