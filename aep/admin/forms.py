from aep.models import Sporting_Event, SportingEvent_Detail, Venue, Sport
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField
from wtforms_alchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

def venue_query():
    return Venue.query

def sport_query():
    return Sport.query

    


class SportingEventForm(FlaskForm):
    event_name = StringField('Sporting Event Name', validators=[DataRequired()])
    event_date = DateField('Sporting Event Date', validators=[DataRequired()])
    event_time = StringField('Sporting Event Time', validators=[DataRequired()])
    venue_list = SelectField('Venue', coerce=int)
    sport_list = SelectField('Sport', coerce=int)
    submit_event = SubmitField('Save Event')

class SportingEventForm2(FlaskForm):
    event_name = StringField('Sporting Event Name', validators=[DataRequired()])
    event_date = StringField('Sporting Event Date', validators=[DataRequired()])
    event_time = StringField('Sporting Event Time', validators=[DataRequired()])
    venue_name = QuerySelectField(query_factory=venue_query,allow_blank='False')
    sport_name = QuerySelectField(query_factory=sport_query,allow_blank='False')
    submit_event = SubmitField('Save Event')

class SportingEventDetailedForm(FlaskForm):
    transportation_van_driver = StringField('Transportation Van Driver', validators=[DataRequired()])
    sport_essential_quantity = IntegerField('Sport Essential Quantity', validators=[DataRequired()])
    submit_event_detail = SubmitField('Submit Event Detail')
#    worker_id = IntegerField('Worker ID', validators=[DataRequired()])
#    transportation_id = IntegerField('Transportation ID', validators=[DataRequired()])
#    sports_essential_id = IntegerField('Sports Essential ID', validators=[DataRequired()])
#    sporting_event_id = IntegerField('Sporting Event ID', validators=[DataRequired()])  
    
class VenueForm(FlaskForm):
    venue_id   = IntegerField('Venue ID', validators=[DataRequired()])
    venu_name  = StringField('Venue Name', validators=[DataRequired()])

class SportForm(FlaskForm):
    sport_id   = IntegerField('Sport ID', validators=[DataRequired()])   
    sport_name = StringField('Sport Name', validators=[DataRequired()])
