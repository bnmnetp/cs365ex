from flask import Flask, render_template, request, session
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.debug = True   # need this for autoreload as well as stack trace
app.secret_key = 'luthercollege'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy(app)



class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    tasks = db.relationship('Task', backref='project', lazy='dynamic')

    def __repr__(self):
        return '<Project %r>' % self.name
        
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), unique=True, index=True)
    due = db.Column(db.Date)
    done = db.Column(db.Boolean)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return '<Task %r>' % self.description

db.drop_all()
db.create_all()

schoolp = Project(name='Luther')
homep = Project(name='Home')
prep1 = Task(description='prep for IProg',project=schoolp,done=False)
prep2 = Task(description='hot tub maintenance',project=homep,done=False)
prep3 = Task(description='wind the clock',project=homep,done=False)
prep4 = Task(description='water the rosemary',due=datetime.now(),project=homep,done=False)

db.session.add_all([schoolp, homep]) #, prep1, prep2, prep3, prep4])
db.session.commit()

allproj = Project.query.all()
for p in allproj:
    print(p.tasks.all())
    
lproj = Project.query.filter_by(name='Luther').first()
lproj = Project.query.filter(Project.name=='Luther')
# filter
# filter_by
# limit
# order_by
# group_by
#
print(str(lproj))

# query executors
# all()
# first()
# get(id)
# count()

#
# http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#common-filter-operators
#

# raw sql
res = db.engine.execute('select * from project')
for row in res:
    print(row)
