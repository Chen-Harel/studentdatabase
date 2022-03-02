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
    print("x - Exit to main menu")
    userChoice = input("")
    if userChoice == "1":
      studentFirstName = input("Who do you want to update? ")
      newFirstName = input("What do you want to update it to? ")
      cur.execute("UPDATE students SET fName=? WHERE fName = ?", (newFirstName, studentFirstName))
      print("Values have been updated...")
    elif userChoice == "x":
      main()


#show chosen table
def showTable():
  cur.execute("SELECT * FROM students")
  print(cur.fetchall())

# Save (commit) the changes
def save():
  con.commit()
  
def main():
  while(True):
    print("What do you want to do?")
    print("1 - Update a student")
    print("2 - show the current table")
    print("3 - save database")
    print("x - Quit the program")
    userChoice = input("").lower()
    if userChoice == "1":
      updateStudent()
    elif userChoice == "2":
      showTable()
    elif userChoice == "3":
      save()
    elif userChoice == "x":
      print("Goodbye!")
      return
main()

# Create table
try:
  cur.execute('''CREATE TABLE students (fName text, lName text, Age int, Class, Grade int)''')
except:
  pass

# Insert a row of data
# cur.execute("INSERT INTO students VALUES(?, ?, ?, ?,?)", (input('Insert the students first name: '), input('Insert the students last name: '), input('What is the students age? '), input('What class is he/she in? '), input('What is his/her grade? ')))

#Insert data from a list
# manyStudents = [
#   ("Chen", "Harel", 30, 7731, 100),
#   ("Ron", "Harel", 25, 123, 90)
# ]

#Add many to table
# cur.executemany("INSERT INTO students VALUES (?,?,?,?,?)", manyStudents)







# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

