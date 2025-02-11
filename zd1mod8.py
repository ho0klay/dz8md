import sqlite3

conn = sqlite3.connect('db_school.sqlite')
cursor = conn.cursor()

#cursor.execute('''CREATE TABLE Students(id int, name text, surname text, age int, city text)''')
#cursor.execute('''CREATE TABLE Courses(id int, name text, time_start text, time_end text)''')
#cursor.execute('''CREATE TABLE Student_courses(student_id int,course_id int, FOREIGN KEY(student_id) REFERENCES Students(id), FOREIGN KEY(course_id) REFERENCES Courses(id)''')
#conn.commit()

#cursor.executemany('INSERT INTO Courses VALUES(?, ?, ?, ?)', [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')])
#cursor.executemany('INSERT INTO Students VALUES(?, ?, ?, ?, ?)',[(1, 'Max', 'Brooks', 24, 'Spb'), (2,'John', 'Stones', 15, 'Spb'),(3, 'Andy', 'Wings', 45, 'Manchester'),(4, 'Katy', 'Brooks', 34, 'Spb')])
#cursor.executemany('INSERT INTO Student_courses VALUES(?, ?)',[(1, 1), (2, 1), (3, 1), (4, 2)])
#conn.commit()

#cursor.execute('SELECT * FROM Students WHERE age > 30')
#print(cursor.fetchall())
#cursor.execute('''SELECT Students. * FROM Students JOIN Courses ON Student.id = Student_courses.student_id JOIN Courses ON Student_courses.course_id = Courses.id WHERE Courses.name = 'python' ''')
#print(cursor.fetchall())
#cursor.execute('''SELECT Students. * FROM Students JOIN Courses ON Student.id = Student_courses.student_id JOIN Courses ON Student_courses.course_id = Courses.id WHERE Courses.name = 'python' AND Students.city = 'Spb' ''')
#print(cursor.fetchall())
#conn.close()

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def fetch_all_students_over_30(self):
        self.cursor.execute("SELECT * FROM Students WHERE age > 30")
        return self.cursor.fetchall()

    def fetch_students_in_course(self, course_name):
        self.cursor.execute('''
        SELECT Students.* FROM Students  JOIN Student_courses ON Students.id = Student_courses.student_id 
        JOIN Courses ON Student_courses.course_id = Courses.id 
        WHERE Courses.name = ?
        ''', (course_name,))
        return self.cursor.fetchall()

    def fetch_students_in_course_from_city(self, course_name, city):
        self.cursor.execute('''
        SELECT Students.* 
        FROM Students 
        JOIN Student_courses ON Students.id = Student_courses.student_id 
        JOIN Courses ON Student_courses.course_id = Courses.id 
        WHERE Courses.name = ? AND Students.city = ?
        ''', (course_name, city))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

db = Database('db_school.sqlite')
#print(db.fetch_all_students_over_30())
#print(db.fetch_students_in_course('python'))
print(db.fetch_students_in_course_from_city('python', 'Spb'))
db.close()
