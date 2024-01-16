from src import conf_app,dbConn
from src import models
from src.mdl import accounts, pingTest,devices,bitPackege
from decouple import config as conf
from flask_migrate import Migrate
app=conf_app() #configura valores inicales de API
#Migra base de datos
buildDB=Migrate(app,dbConn)
if __name__=='__main__':
    app.run(host=conf('API_HOST'),port=conf('API_PORT'))

