from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b884d70f6360e929e626e2deb34dd58e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager1 = LoginManager(app)
login_manager2 = LoginManager(app)
login_manager1.login_view = 'Login_student'
login_manager2.login_view = 'Login_instructor'
# login_manager.login_message_category = 'info'


from hello import routes