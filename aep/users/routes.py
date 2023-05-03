from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
from aep import bcrypt
from aep import current_worker
from aep.models import Worker
from aep.users.forms import LoginForm
 
 
 
users = Blueprint('users', __name__)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))



@users.route('/login', methods=['GET', 'POST'])
def login():
    not_logged_in = False
    if current_user.is_authenticated:
        return redirect(url_for('main.mainpage'))
    else:
        not_logged_in = True

    form = LoginForm()
    
    if form.validate_on_submit():
        user = Worker.query.filter_by(Worker_Email=form.Worker_Email.data).first()
        if user and (user.Worker_Password == form.Worker_Password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.mainpage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form, not_logged_in=not_logged_in)



