from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

f = Faker()

# create connection with SQLite
engine = create_engine('sqlite:///students_courses.db')
Base = declarative_base()

# intermediate table for many-to-many relationship between students and courses
student_course_association = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Course", secondary=student_course_association, back_populates="students")

# Course model
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship("Student", secondary=student_course_association, back_populates="courses")

# create tables in DB
Base.metadata.drop_all(engine)  # for correct testing
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# create list of students, use Faker lib
if not session.query(Student).first():
    students = [
        Student(name=f'test-{f.name()}')
    for k in range(10)
    ]

# add all students in Student table
    session.add_all(students)
    session.commit()
    print('Students was successfully added!')

# create list with courses title
if not session.query(Course).first():
    courses = [
        Course(title="Mathematics"),
        Course(title="History"),
        Course(title="Biology"),
        Course(title="Computer Science"),
        Course(title="Philosophy")
    ]

# add all title name of courses into table "courses"
    session.add_all(courses)
    session.commit()
    print('Courses was successfully added!')

# add new users on "History" courses:
# 1. Create student(s) which will adding to the course of 'History' and add in 'Student' table
new_students = [
    Student(name="Valerii"),
    Student(name="Lana")
    ]
if new_students:
    session.add_all(new_students)
    session.commit()
    print('New student(s) was successfully added to Student table')
else:
    print('ERROR: New students were not added to the Student table')

# 2. Add new user on "History" courses, where "History" is title in table "courses"
course_title = "History"
course = session.query(Course).filter_by(title=course_title).first()
if course:
    course.students.extend(new_students)
    session.commit()
    print(f'New student(s) was successfully added on {course_title} course')
else:
    print(f'ERROR: Course with title {course_title} does not exist')


# add an existing student to another course:
# 1. Get student by name
student = session.query(Student).filter_by(name="Valerii").first()

# 2. Get course by title - "Mathematics"
new_course = session.query(Course).filter_by(title="Mathematics").first()

# 3. Verify and add the course to the student "Valerii"
if student and new_course:
    student.courses.append(new_course)
    session.commit()
    print(f"Student {student.name} also enrolled in course:\n"
          f" {new_course.title}")
else:
    print("ERROR: Student or course not found.")

# query(request) the courses for which a specific student is registered
student_name = "Valerii"
student = session.query(Student).filter_by(name=student_name).first()
if student:
    courses = student.courses
    for course in courses:
        print(f"Student {student_name} is registered on:\n"
              f" Course ID: {course.id}, Course Title: {course.title}")
else:
    print(f'ERROR: Student with name {student_name} not found.')

# query(request) on students which has records on "History" courses
course_name = "History"
course = session.query(Course).filter_by(title=course_name).first()
if course:
    students = course.students
    for student in students:
        print(f"Student ID: {student.id}, Student Name: {student.name}, "
              f"who are enrolled in the course {course_name}")
else:
    print(f'ERROR: Course with name {course_name} not found.')

# Update student name
student_name = "Valerii"
upd_name = "Valerii-Update"
student = session.query(Student).filter_by(name=student_name).first()
if student:
    student.name = upd_name
    session.commit()
    print(f'Student with name {student_name} was successfully updated on {upd_name}')
else:
    print(f'ERROR: Student with name {student_name} not found.')

# Remove student from Student by ID
student_id = 12
student = session.query(Student).filter_by(id=student_id).first()
if student:
    session.delete(student)
    session.commit()
    print(f'Student with ID={student_id} was successfully deleted.')
else:
    print(f'ERROR: Student with ID={student_id} not found or does not exist')
