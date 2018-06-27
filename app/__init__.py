import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
# RotatingFileHandler is a class, consistently makes new log files when one grows too large and stores previous ones in a quantity you give it
import os
from flask import Flask
# Flask class from flask module-ish

# app = Flask(__name__) # refactored using config import lines
#app.config['SECRET_KEY'] = 'you-will-never-guess'
#more variables as needed
# from /../config import Config ? not quite just need from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' #named reference to the login view, like url_for()

# test with '(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025'
# creates testing server that prints to console :D
# use console to set/export MAIL_SERVER=localhost and MAIL_PORT=8025
# use the following in console to set actual account
# export MAIL_SERVER=smtp.googlemail.com
# export MAIL_PORT=587
# export MAIL_USE_TLS=1
# export MAIL_USERNAME=<your-gmail-username>
# export MAIL_PASSWORD=<your-gmail-password>
if not app.debug: 
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler=RotatingFileHandler('logs/microblog.log',maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s, [in %(pathname)s:%(lineno)d]'))
    # logging.Formatter structures log messages, here we have timestamp, level, message, and sourcefile with line number
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')




from app import routes, models, errors