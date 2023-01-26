from flask import Flask 
from .db import update_db, init_db
from settings import ADMIN_SECRET_KEY

UPLOAD_FOLDER = './templates/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__,template_folder='./templates',static_folder='./static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = ADMIN_SECRET_KEY

init_db(app)
update_db(app)

import api.views
