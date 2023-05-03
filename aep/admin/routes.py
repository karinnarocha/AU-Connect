from flask import Blueprint, url_for, render_template, flash
from flask_login import current_user
from aep import db, current_worker
from flask import request , redirect, abort
from aep.admin.forms import SportingEventForm
from aep.models import Sporting_Event, Venue, Sport
from wtforms_alchemy import QuerySelectField

admin = Blueprint('admin',__name__)

@admin.route('/admin/', methods = ['GET', 'POST'])
def admin_default():
    
    form1 = SportingEventForm()
    
    venue_data = db.session.query(Venue.Venue_ID, Venue.Venue_Location).all()
    sport_data = db.session.query(Sport.Sport_ID, Sport.Sport_Name).all()
    form1.venue_list.choices = venue_data
    form1.sport_list.choices = sport_data

    if form1.is_submitted():
        
        sporting_event = Sporting_Event(
             SportingEvent_Name=form1.event_name.data,
             SportingEvent_Date=form1.event_date.data,
             SportingEvent_Time=form1.event_time.data,
             Venue_ID=form1.venue_list.data,
             Sport_ID=form1.sport_list.data)
        
        print('Made it to the submit the data!')

        db.session.add(sporting_event)
        db.session.commit()
        flash('Sporting Event has been added', 'success')
        return redirect(url_for('main.mainpage'))
     
    if current_user.is_authenticated:

        if current_user.role.Role_Name == 'Admin':
            return render_template ('admin.html', title = 'Admin Page', form1 = form1, venue_data = venue_data, sport_data = sport_data)
        else:
            flash('You do not have access to this page.', 'danger')
            return redirect(url_for('main.mainpage'))
    else:
        return redirect(url_for('users.login'))

 
@admin.route('/api/tables')
def api_tables():
    if current_user.is_authenticated:
        return "<h1 style='color: blue'>API Table Listing</h1>"
    else:
          return redirect(url_for('users.login'))

@admin.route('/api/sql')
def api_sql():
    if current_user.is_authenticated:
        return "<h1 style='color: green'>API SQL VIEWS</h1>"
    else:
          return redirect(url_for('users.login'))      



