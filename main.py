import sqlite3
import os

try:
  con  = sqlite3.connect('school.db')
except:
  pass


cur = con.cursor()

#clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#update table
def updateStudent():
  while(True):
    print("What do you want to update?")
    print("1 - Update first name")
    print("2 - Update last name")
    print("3 - Update age")
    print("4 - Update class")
    print("5 - Update grade")
    print("x - return to main menu")
    userChoice = input().lower()
    if userChoice == "1":
      studentFirstName = input("What is the first name? ")
      studentLastName = input("What is the last name? ")
      newFirstName = input("What do you want to update the first name to? ")
      cur.execute("UPDATE students SET fName=? WHERE fName = ? and lName = ?", (newFirstName, studentFirstName, studentLastName))
      print("Values have been updated...")
    elif userChoice == "2":
      print("Unable to update last name at this time.")
    elif userChoice == "3":
      print("Unable to update last name at this time.")
    elif userChoice == "4":
      print("Unable to update class at this time.")
    elif userChoice == "5":
      studentFirstName = input("What is the first name? ")
      studentLastName = input("What is the last name? ")
      studentNewGrade = int(input("What is the students new grade? "))
      cur.execute("UPDATE students SET Grade=? WHERE fName = ? and lName = ?", (studentNewGrade, studentFirstName, studentLastName))
    elif userChoice == "x":
      return

# Create table
def createStudentsTable():
  try:
    cur.execute(
        '''CREATE TABLE students (fName text, lName text, Class int, Age int, Grade int)''')
    print("Table created!")
  except:
    pass

#delete table/db
def delete():
  tableOrDb = input("Do you want to remove a table or an entire database? ").lower()
  if tableOrDb == "table":
    print("THIS ACTION CANNOT BE UNDONE!!!!")
    whichTable = input("What is the table name? ")
    cur.execute('''DROP TABLE ?''', (whichTable))
    print("Table deleted...")
  elif tableOrDb == "database":
    print("THIS ACTION CANNOT BE UNDONE!!!!")
    whichDB = input("What is the database name? ")
    cur.execute("DROP DATABASE ?", (whichDB))

#remove student from 
def removeStudent():
  print("This will remove a student from the database. This CAN'T BE UNDONE!!!")
  studentFName = input("What is the students first name? ")
  studentLName = input("What is the students last name? ")
  studentClass = input("What class is the student in? ")
  sure = input("Are you sure you want to delete this student? Type 'y' or 'n' ")
  if sure == "y":
    print("Student removed from table")
    cur.execute("DELETE FROM students WHERE fName=? and lName=? and Class=?", (studentFName, studentLName, studentClass))
  elif sure == "n":
    print("No changes made.")
    pass

# Insert a row of data
def addSingleData():
  cur.execute("INSERT INTO students VALUES(?, ?, ?, ?,?)", (input('Insert the students first name: '), input(
      'Insert the students last name: '), input('What class is he/she in? '), input('What is the students age? '), input('What is his/her grade? ')))
  print("Table updated with info...")
#show table
def showTable():
  try:
    cur.execute("SELECT * FROM students")
    print(cur.fetchall())
  except:
    print("No tables to show...")

# Save (commit) the changes
def save():
  con.commit()
  closedb = input("Do you want to close the database? Type 'y' or 'n' ")
  if closedb == "y":
    print("Database has been closed.")
    con.close()
  elif closedb == "n":
    pass
  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.

def main():
  while(True):
    print("What do you want to do?")
    print("1 - Update a student")
    print("2 - show the current table")
    print("3 - save database")
    print("4 - create students table")
    print("5 - add a single row of data")
    print("6 - remove student from DB")
    print("7 - delete a table/DB")
    print("x - Quit the program")
    userChoice = input().lower()
    clearConsole()
    if userChoice == "1":
      updateStudent()
    elif userChoice == "2":
      showTable()
    elif userChoice == "3":
      save()
    elif userChoice == "4":
      createStudentsTable()
    elif userChoice == "5":
      addSingleData()
    elif userChoice == "6":
      removeStudent()
    elif userChoice == "7":
      print("Currently unavailable")
    elif userChoice == "x":
      print("Goodbye!")
      return
    else:
      print("Please select a number from the menu.")

if __name__ == "__main__":
  main()





# Insert data from a list
# manyStudents = [
#   ("Chen", "Harel", 30, 7731, 100),
#   ("Ron", "Harel", 25, 123, 90)
# ]

#Add many to table
#  cur.executemany("INSERT INTO students VALUES (?,?,?,?,?)", manyStudents)

