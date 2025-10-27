from flask import Blueprint
from .. import app

courses = Blueprint('courses', __name__, template_folder='templates')

from . import views