import json
import csv
import os
from datetime import datetime
def load_students():

    if not os.path.exists("student.json"):
        return {}

    try:
        with open("student.json", "r", encoding="utf-8") as file:
            students = json.load(file)

        if not isinstance(students, dict):
            print("Error: Student data must be a dictionary.")
            return None

        return students

    except (json.JSONDecodeError, OSError) as e:
        print("Error loading student records:", e)
        return None
    
student = load_students()

if student is None:
    print("Please fix the JSON file before continuing.")

else:
    print("Student records loaded successfully.")
    print("Total students:", len(student))

def save_students():

    try:
        with open("student.json", "w", encoding="utf-8") as file:
            json.dump(student, file, indent=4)

        print("Record saved to student.json.")

    except OSError as e:
        print("Error saving student records:", e)
def log_activity(message):
    try:
        with open("activity_log.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + " - " + message + "\n")

    except OSError as e:
        print("Error writing activity log:", e)


def add_student():

    student_id = input("Enter Student ID: ")

    if student_id in student:
        print("Error: Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    try:
        python_marks = float(input("Enter Python Marks: "))
        maths_marks = float(input("Enter Maths Marks: "))
        dbms_marks = float(input("Enter DBMS Marks: "))

    except ValueError:
        print("Error: Please enter numeric marks.")
        return

    if not (0 <= python_marks <= 100 and
            0 <= maths_marks <= 100 and
            0 <= dbms_marks <= 100):

        print("Error: Marks must be between 0 and 100.")
        return

    record = {
        "name": name,
        "department": department,
        "marks": {
            "Python": python_marks,
            "Maths": maths_marks,
            "DBMS": dbms_marks
        }
    }

    student[student_id] = record

    save_students()
    log_activity("Student added: " + student_id)
    print("Student record added successfully!")


def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in student:
        print("\nStudent Found!")
        print("ID:", student_id)
        print("Name:", student[student_id]["name"])
        print("Department:", student[student_id]["department"])
        print("Marks:", student[student_id]["marks"])
    else:
        print("Student not found!")
def view_students():
    if not student:
        print("No student records found!")
        return

    for student_id, record in student.items():
        print("\nStudent ID:", student_id)
        print("Name:", record["name"])
        print("Department:", record["department"])
        print("Marks:", record["marks"])
def export_csv():
    try:
        with open("students.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["Student ID", "Name", "Department",
                             "Python", "Maths", "DBMS"])

            # Student records
            for student_id, record in student.items():
                writer.writerow([
                    student_id,
                    record["name"],
                    record["department"],
                    record["marks"]["Python"],
                    record["marks"]["Maths"],
                    record["marks"]["DBMS"]
                ])
        log_activity("Student records exported to CSV")
        print("Student records exported successfully!")

    except OSError as e:
        print("Error exporting CSV:", e)
def log_activity(message):
    try:
        with open("activity_log.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + " - " + message + "\n")

    except OSError as e:
        print("Error writing activity log:", e)
def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id not in student:
        print("Student not found!")
        return

    name = input("Enter New Name: ")
    department = input("Enter New Department: ")

    try:
        python_marks = float(input("Enter New Python Marks: "))
        maths_marks = float(input("Enter New Maths Marks: "))
        dbms_marks = float(input("Enter New DBMS Marks: "))

    except ValueError:
        print("Please enter numeric marks.")
        return

    if not (0 <= python_marks <= 100 and
            0 <= maths_marks <= 100 and
            0 <= dbms_marks <= 100):
        print("Marks must be between 0 and 100.")
        return

    student[student_id] = {
        "name": name,
        "department": department,
        "marks": {
            "Python": python_marks,
            "Maths": maths_marks,
            "DBMS": dbms_marks
        }
    }

    save_students()
    log_activity("Student updated: " + student_id)

    print("Student record updated successfully")
def read_log():
    try:
        with open("activity_log.txt", "r", encoding="utf-8") as file:

            print("Using read():")
            file.seek(0)
            print(file.read())

            print("Using readline():")
            file.seek(0)
            print(file.readline())

            print("Using readlines():")
            file.seek(0)
            print(file.readlines())

    except FileNotFoundError:
        print("Activity log file not found!") 
def write_demo():
    try:
        with open("activity_log.txt", "a", encoding="utf-8") as file:
        
            file.write("This is a write() demonstration.\n")
            lines = [
                "This is first line using writelines().\n",
                "This is second line using writelines().\n"
            ]

            file.writelines(lines)

        print("Data written successfully!")

    except OSError as e:
        print("Error writing file:", e)
def json_demo():
    if not student:
        print("No student record available!")
        return
    record = next(iter(student.values()))

    json_string = json.dumps(record, indent=4)
    print("After json.dumps():")
    print(json_string)

    python_data = json.loads(json_string)
    print("After json.loads():")
    print(python_data)
if student is not None:

    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. View All Students")
        print("4. Export CSV")
        print("5. Update Student")
        print("6. JSON Demo")
        print("7. Write Demo")
        print("8. Read Activity Log")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            view_students()

        elif choice == "4":
            export_csv()

        elif choice == "5":
            update_student()

        elif choice == "6":
            json_demo()

        elif choice == "7":
            write_demo()

        elif choice == "8":
            read_log()

        elif choice == "9":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")