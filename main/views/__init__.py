from flask import Blueprint

bp = Blueprint('views', __name__)

from . import routes
from . import drug_routes, hospital_routes
# from . import config_api