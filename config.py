import os
from dotenv import load_dotenv
import dotenv 

dotenv_file =os.path.join(os.path.dirname(__file__),'.env')
if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    ENV="development"    
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://emqu:avion01.@localhost/emqudb"
    SECRET_KEY="camion350."
    
class ProductionConfig(Config):
    pass