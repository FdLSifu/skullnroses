from flask import Flask
import os

temp_dir = os.path.abspath('./templates/')
app = Flask(__name__, template_folder=temp_dir)

from server import routes
