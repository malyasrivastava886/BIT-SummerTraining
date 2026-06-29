#day 5 -solution
# Question 1: Create and Write a File
# Expected Output:
# File created successfully
file = open("student.txt", "w")
file.write("Name: Malya Srivastava\n")
file.write("Age: 20\n")
file.write("College: BIT\n")
file.close()
print("File created successfully")

# Question 2: Read a File
# Expected Output:
# Name: Malya Srivastava
# Age: 20
# College: BIT
file = open("student.txt", "r")
print(file.read())
file.close()

# Question 3: Append to a File
# Expected Output:
# Name: Malya Srivastava
# Age: 20
# College: BIT
# Course: Python Data AI
# City: Lucknow
file = open("student.txt", "a")
file.write("Course: Python Data AI\n")
file.write("City: Lucknow\n")
file.close()
file = open("student.txt", "r")
print(file.read())
file.close()

# Question 4: Count Lines in a File
# Expected Output:
# Total lines: 5
file = open("student.txt", "r")
lines = file.readlines()
print("Total lines:", len(lines))
file.close()

# Question 5: Write Multiple Students
# Expected Output:
# Aman
# Priya
# Shalu
# Raj
# Ansh
file = open("students.txt", "w")
file.write("Aman\n")
file.write("Priya\n")
file.write("Shalu\n")
file.write("Raj\n")
file.write("Ansh\n")
file.close()
file = open("students.txt", "r")
print(file.read())
file.close()



# Question 6: Search a Name in File
# Example Input:
# Priya
# Expected Output:
# Found
name = input("Enter student name: ")
file = open("students.txt", "r")
students = file.read().splitlines()
if name in students:
    print("Found")
else:
    print("Not Found")
file.close()

# Question 7: Copy File Content
# Expected Output:
# Backup created successfully
source = open("students.txt", "r")
content = source.read()
source.close()
backup = open("students_backup.txt", "w")
backup.write(content)
backup.close()
print("Backup created successfully")


#Question 8: Marks File Summary
# Expected Output:
# Total marks: 433
# Average marks: 86.6
file = open("marks.txt", "w")
file.write("85\n")
file.write("90\n")
file.write("78\n")
file.write("92\n")
file.write("88\n")
file.close()
file = open("marks.txt", "r")
marks = file.readlines()
total = 0
for mark in marks:
    total = total + int(mark)
average = total / len(marks)
print("Total marks:", total)
print("Average marks:", average)
file.close()