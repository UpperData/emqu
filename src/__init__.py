import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dbConn=SQLAlchemy()

def conf_app():
    app= Flask(__name__)    
    app.config.from_object(os.environ['CONFIG_ENV']) #Define varaibles de entorno (Desarrollo)    
    dbConn.init_app(app) # Iniciamos DB    
    with app.app_context(): 
        #Inicializamos endpoint
        from .routes import api_routes        
        app.register_blueprint(api_routes)
        return app 