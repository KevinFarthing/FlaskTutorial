# could be stored under app.config in __init__.py but SEPARATION OF CONCERNS PRINCIPLE
# using a class format and importing them is easily extensible
# flask uses SECRET_KEY as a cryptographic key. Protects against CSRF (cross site request forgery pronounced seasurf)
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # value of secret_key looks for environment variable, or hardcoded version if the environment var isn't found
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') # using DATABASE_URL as a db variable, currently undefined
    SQLALCHEMY_TRACK_MODIFICATIONS = False # feature of alchemy that signalsthe app every time a change is made. don't need it right now
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['farthing.kw@gmail.com']
    POSTS_PER_PAGE = 20
    LANGUAGES = ['en', 'es']