from flask import Blueprint
api_routes=Blueprint('routes',__name__)
from . import routes
