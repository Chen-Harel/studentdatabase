import sqlite3
try:
  con  = sqlite3.connect('school.db')
except:
  pass


cur = con.cursor()

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
def createTable():
  try:
    cur.execute(
        '''CREATE TABLE students (fName text, lName text, Age int, Class, Grade int)''')
  except:
    pass

# Insert a row of data
def addSingleData():
  cur.execute("INSERT INTO students VALUES(?, ?, ?, ?,?)", (input('Insert the students first name: '), input('Insert the students last name: '), input('What is the students age? '), input('What class is he/she in? '), input('What is his/her grade? ')))

#show table
def showTable():
  cur.execute("SELECT * FROM students")
  print(cur.fetchall())



# Save (commit) the changes
def save():
  con.commit()
  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  con.close()
  
def main():
  while(True):
    print("What do you want to do?")
    print("1 - Update a student")
    print("2 - show the current table")
    print("3 - save database")
    print("4 - create table")
    print("5 - add a single row of data")
    print("6 - delete a student")
    print("x - Quit the program")
    userChoice = input().lower()
    if userChoice == "1":
      updateStudent()
    elif userChoice == "2":
      showTable()
    elif userChoice == "3":
      save()
    elif userChoice == "4":
      createTable()
    elif userChoice == "5":
      addSingleData()
    elif userChoice == "6":
      deleteStudent()
    elif userChoice == "x":
      print("Goodbye!")
      return
    else:
      print("Please select an item from the menu list.")

if __name__ == "__main__":
  main()





# Insert data from a list
# manyStudents = [
  # ("Chen", "Harel", 30, 7731, 100),
  # ("Ron", "Harel", 25, 123, 90)
# ]

#Add many to table
#  cur.executemany("INSERT INTO students VALUES (?,?,?,?,?)", manyStudents)

