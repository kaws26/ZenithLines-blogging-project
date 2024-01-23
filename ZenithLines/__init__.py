from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import email_validator 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = '170632579391ac903fa5a1402d826121'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from ZenithLines import routes