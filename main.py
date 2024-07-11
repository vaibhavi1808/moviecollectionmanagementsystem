from crud import create_student, read_students, update_student, delete_student 
from data_science import calculate_average_percentage, generate_report
def main():
    while True:
        print("\nStudent Management System")
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Calculate Average Percentage")
        print("6. Generate Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            city = input("Enter city: ")
            student_class = input("Enter class: ")
            total_percentage = float(input("Enter total percentage: "))
            create_student (roll, name, city, student_class, total_percentage)
        elif choice == '2':
            read_students()
        elif choice == '3':
            roll = input("Enter roll number to update: ")
            name = input("Enter new name (leave blank to skip): ")
            city = input("Enter new city (leave blank to skip): ")
            student_class = input("Enter new class (leave blank to skip): ")
            total_percentage = input("Enter new total percentage (leave blank to skip): ")

            update_student (roll, name or None, city or None, student_class or None, float(total_percentage) if total_percentage else None)
        elif choice == '4':
            roll = input("Enter roll number to delete: ")
            delete_student (roll)
        elif choice == '5':
            calculate_average_percentage()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()