from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



# class Enrollment(db.Model):
#     __table__ = 'enrollment'
#     course_num = db.Column(db.Integer, db.ForeignKey('course.course_num'))
#     student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))


enrollment = db.Table('enrollment',
    db.Column('course_num',db.Integer, db.ForeignKey('course.course_num')),
    db.Column('student_id',db.Integer, db.ForeignKey('student.student_id')),
    db.Column('grade',db.Integer)
)

class Course(db.Model):
    __tablename__ = 'course'
    course_num = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.Text)
    room = db.Column(db.Integer)
    students = db.relationship('Student', secondary=enrollment,
                                backref=db.backref('courses',lazy='dynamic'))

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
c1 = Course(course_num=150,building='Olin',room='202',students=[s1,s2])
c2 = Course(course_num=365,building='Olin',room='202')
db.session.add(c1)
db.session.add(c2)

s4 = Student(student_id=4,first_name='John',last_name='Doe',courses=[c1,c2])
db.session.add(s4)

db.session.commit()
