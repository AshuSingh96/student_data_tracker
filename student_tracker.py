import csv

students=[]


def student_data():
    try: 
        name = input("Enter student name: ").strip()
        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabets.")

        roll_number = input("Enter roll number: ").strip()
        for student in students:
            if student['roll_number'] == roll_number:
                raise ValueError("Roll number already exists. Please enter a unique roll number.")

        marks = []
        for i in range(1, 4):
            mark = int(input(f"Enter marks for Subject {i}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")
            marks.append(mark)

        student = {
            "name": name,
            "roll_number": roll_number,
            "marks": marks
        }
        students.append(student)
        print("Student record added successfully!\n")
    except ValueError as e:
        print(f"Invalid input: {e}\n")
def display_students():
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Records:")
    for student in students:
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Marks: {student['marks']}")
    print()

def calculate_average():
    if not students:
        print("No records found.\n")
        return

    for student in students:
        average = sum(student['marks']) / len(student['marks'])
        print(f"Average marks for {student['name']} (Roll Number: {student['roll_number']}): {average:.2f}")
    print()

def save_to_csv():
    if not students:
        print("No records found.\n")
        return

    filename = input("Enter the filename to save the records (e.g., students.csv): ").strip()
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll Number", "Subject 1", "Subject 2", "Subject 3"])
            for student in students:
                writer.writerow([student['name'], student['roll_number']] + student['marks'])
        print(f"Records saved to {filename} successfully!\n")
    except Exception as e:
        print(f"Error saving to CSV: {e}\n")
    
def main():
    while True:
        print("\n")
        print("===== Student Data records =====")
        print("1. Add Student Record")
        print("2. Display Student Records")
        print("3. Calculate Average Marks")
        print("4. Save Records to CSV")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            student_data()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            save_to_csv()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__": 
    main()