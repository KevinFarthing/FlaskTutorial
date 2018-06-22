from flask import Flask
# Flask class from flask module-ish

# app = Flask(__name__) # refactored using config import lines
#app.config['SECRET_KEY'] = 'you-will-never-guess'
#more variables as needed
# from /../config import Config ? not quite just need from config import Config
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes