# Function to create and print the initial list of student names
def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    print("Initial list of students:")
    for name in studentNames:
        print(f"{name} Evans")
    return studentNames

# Function to add a new name to the list and reprint the updated list
def addToList(studentNames):
    newName = input("Enter a new name to add to the list: ")
    studentNames.append(newName)
    print("\nUpdated list of students:")
    for name in studentNames:
        print(f"{name} Evans")

# Main program
if name_== "main":
    students = studList() # Create and print the initial list
    addToList(students)    # Add a new name and reprint the updated list