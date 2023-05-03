from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from aep.config import Config


current_worker = False

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()



def create_app(config_clas=Config):
    app = Flask(__name__)
 
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'
    
    
    
    from .main.routes import main
    from .admin.routes  import admin
    from .users.routes import users
    
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(users)
    
    return app