from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    course_num = db.Column(db.Integer, db.ForeignKey('course.course_num'),primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'),primary_key=True)
    grade = db.Column(db.Integer)
    student = db.relationship("Student", backref="course_enrollments")

class Course(db.Model):
    __tablename__ = 'course'
    course_num = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.Text)
    room = db.Column(db.Integer)
    students = db.relationship('Enrollment', backref='course')
    
class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

db.drop_all()    
db.create_all()

s1 = Student(student_id=1,first_name='Brad',last_name='Miller')
s2 = Student(student_id=2,first_name='Jane',last_name='Miller')
s3 = Student(student_id=3,first_name='Josh',last_name='Miller')
db.session.add_all([s1,s2,s3])

c1 = Course(course_num=150,building='Olin',room='202')
c2 = Course(course_num=365,building='Olin',room='202')
db.session.add(c1)
db.session.add(c2)
# 
# s4 = Student(student_id=4,first_name='John',last_name='Doe',courses=[c1,c2])
# db.session.add(s4)
# 
en = Enrollment(student=s1,grade=1)
c1.students.append(en)
en = Enrollment(student=s1,grade=2)
c2.students.append(en)
en = Enrollment(student=s2,grade=2)
c1.students.append(en)

db.session.commit()

#res = Student.query.filter(Student.student_id.in_([x.student_id for x in c1.students]))
#for row in res:
#    print(row)
