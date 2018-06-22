# could be stored under app.config in __init__.py but SEPARATION OF CONCERNS PRINCIPLE
# using a class format and importing them is easily extensible
# flask uses SECRET_KEY as a cryptographic key. Protects against CSRF (cross site request forgery pronounced seasurf)
import os

class Config(object):
    # value of secret_key looks for environment variable, or hardcoded version if the environment var isn't found
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    