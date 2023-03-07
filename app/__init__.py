from flask import Flask
from config import Config

#Creates application object as an instance of class Flask
# __name__ is a python predefined variable which is the name of module used
app = Flask(__name__)
app.config.from_object(Config)

#import routes once created, bottom import instead of top to workaround circular imports
from app import routes