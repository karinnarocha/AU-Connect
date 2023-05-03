from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user
from aep.models import Sporting_Event,Venue, Sport,Sport_Essential,SportingEvent_Detail,Worker,Transportation
from aep import db
from datetime import datetime

#from datetime import DateTime
#from flask import jsonify

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def index():
# SECURITY CHECK AUTHENTICATION
     if current_user.is_authenticated:
          return render_template('mainpage.html', title='Main Page')
     else:
          return redirect(url_for('users.login'))

     
@main.route('/mainpage')
def mainpage():
     if current_user.is_authenticated:
          
          current_date = datetime.now()
          
          query_data = db.session.query(
                         Sporting_Event.SportingEvent_Name,
                         Sporting_Event.SportingEvent_Date,
                         Sporting_Event.SportingEvent_Time,
                         Venue.Venue_Location,
                         Venue.Venue_City,
                         Venue.Venue_State,
                         Venue.Venue_ZipCode,
                         Sport.Sport_Name,
                         Sport.Sport_Image,
                         SportingEvent_Detail.TransportationVan_Driver,
                         SportingEvent_Detail.SportEssential_Quantity,
                         Worker.Worker_FirstName,
                         Worker.Worker_LastName,
                         Transportation.Transportation_VanName,
                         Transportation.Transportation_PlateNumber,
                         Sport_Essential.SportEssential_Name,
                         Sport_Essential.SportEssential_Category)\
               .outerjoin(Venue, Sporting_Event.Venue_ID == Venue.Venue_ID) \
               .outerjoin(Sport, Sporting_Event.Sport_ID == Sport.Sport_ID) \
               .outerjoin(SportingEvent_Detail, Sporting_Event.SportingEvent_ID == SportingEvent_Detail.SportingEvent_ID) \
               .outerjoin(Worker, SportingEvent_Detail.Worker_ID == Worker.Worker_ID) \
               .outerjoin(Transportation, SportingEvent_Detail.Transportation_ID == Transportation.Transportation_ID) \
               .outerjoin(Sport_Essential, SportingEvent_Detail.SportEssential_ID == Sport_Essential.SportEssential_ID) \
               .filter(Sporting_Event.SportingEvent_Date >= current_date) \
               .order_by(Sporting_Event.SportingEvent_Date.asc())\
               .limit(3).all()
                    
          if current_user.role.Role_Name == 'Admin': 
               is_admin = True 
          else:
               is_admin = False
          
          print(f"Number of results: {len(query_data)}")
               
          print ('Here is Query')
          print (query_data)
          print ('End of Query')

          return render_template('mainpage.html', title='Main Page', query_data = query_data, is_admin = is_admin)

     else:
          return redirect(url_for('users.login'))

