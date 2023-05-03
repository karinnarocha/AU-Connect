
from aep import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedSerializer as Serializer
from flask import current_app
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Worker.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'Role'
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(30), unique=False, nullable=False)
    
class Department(db.Model):
    __tablename__ = 'Department'
    Department_ID = db.Column(db.Integer, primary_key=True)
    Department_Name = db.Column(db.String(30), unique=False, nullable=False)

class Sport(db.Model):
    __tablename__ = 'Sport'
    Sport_ID = db.Column(db.Integer, primary_key = True)
    Sport_Name = db.Column(db.String(100), unique=False, nullable=False)
    Sport_Image = db.Column(db.String(100), unique=False, nullable=False)
    
    def __repr__(self):
        return '[Sport {}]'.format(self.Sport_Name)
    
class Sport_Essential(db.Model):
    __tablename__ = 'Sport_Essential'
    SportEssential_ID = db.Column(db.Integer, primary_key = True)
    SportEssential_Name = db.Column(db.String(70), unique=False, nullable=False)
    SportEssential_Category = db.Column(db.String(20), unique=False, nullable=False)
    SportEssential_Minimum = db.Column(db.Integer, unique=False, nullable=False)
    SportEssential_Maximum = db.Column(db.Integer, unique=False, nullable=False)
    
class Sporting_Event(db.Model):
    __tablename__ = 'Sporting_Event'
    SportingEvent_ID = db.Column(db.Integer, primary_key = True)
    SportingEvent_Name = db.Column(db.String(100), unique=False, nullable=False)
    SportingEvent_Date = db.Column(db.String, unique=False, nullable=False)
    SportingEvent_Time= db.Column(db.String, unique=False, nullable=False)
    Venue_ID = db.Column(db.Integer, db.ForeignKey('Venue.Venue_ID'))
    Sport_ID = db.Column(db.Integer, db.ForeignKey('Sport.Sport_ID'))
    
class SportingEvent_Detail(db.Model):
    __tablename__ = 'SportingEvent_Detail'
    SportingEventDetail_ID = db.Column(db.Integer, primary_key = True)
    TransportationVan_Driver = db.Column(db.String(30), unique=False, nullable=False)
    SportEssential_Quantity = db.Column(db.Integer, unique=False, nullable=False)
    Worker_ID = db.Column(db.Integer, db.ForeignKey('Worker.Worker_ID'))
    Transportation_ID = db.Column(db.Integer, db.ForeignKey('Transportation.Transportation_ID'))
    SportEssential_ID = db.Column(db.Integer, db.ForeignKey('SportEssential.SportEssential_ID'))
    SportingEvent_ID = db.Column(db.Integer, db.ForeignKey('SportingEvent.SportingEvent_ID'))
   
    
    
class Transportation(db.Model):
    __tablename__ = 'Transportation'
    Transportation_ID = db.Column(db.Integer, primary_key = True)
    Transportation_VanName = db.Column(db.String(5), unique=False, nullable=False)
    Transportation_PlateNumber = db.Column(db.CHAR(7), unique=False, nullable=False)
    Transportation_VanAvailability = db.Column(db.Integer, unique=False, nullable=False)
    
class Venue(db.Model):
    __tablename__ = 'Venue'
    Venue_ID = db.Column(db.Integer, primary_key = True)
    Venue_Location = db.Column(db.String(100), unique=False, nullable=False)
    Venue_City = db.Column(db.String(50), unique=False, nullable=False)
    Venue_State = db.Column(db.String(2), unique=False, nullable=False)
    Venue_ZipCode = db.Column(db.String(5), unique=False, nullable=False)


    def __repr__(self):
        return '[Venue {}]'.format(self.Venue_Location)

class Worker(db.Model, UserMixin):
    __tablename__ = 'Worker'
    Worker_ID = db.Column(db.Integer, primary_key=True)
    Worker_FirstName = db.Column(db.String(length=100), nullable=False)
    Worker_LastName = db.Column(db.String(length=100), nullable=False)
    Worker_Email = db.Column(db.String(length=100), unique=True, nullable=False)
    Worker_Password = db.Column(db.String(length=25), nullable=False)
    Department_ID = db.Column(db.Integer, db.ForeignKey('Department.Department_ID'))
    Role_ID = db.Column(db.Integer, db.ForeignKey('Role.Role_ID'))    
    role = db.relationship("Role", backref=db.backref("workers", lazy=True))
    
    def get_id(self):
        return str(self.Worker_ID)

    



