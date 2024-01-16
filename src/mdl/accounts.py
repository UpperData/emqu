from src import dbConn
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
load_dotenv()
    
   
class Accounts(dbConn.Model):
    id=dbConn.Column( dbConn.Integer,primary_key=True,autoincrement=True)
    fullName=dbConn.Column(dbConn.String(255), nullable=False)
    email=dbConn.Column(dbConn.String(255), unique=True,nullable=False)
    roleId=dbConn.Column(dbConn.Integer,nullable=False )
    passw=dbConn.Column(dbConn.String(255), nullable=False)
    isActived=dbConn.Column(dbConn.Boolean,default=True )
    created=dbConn.Column(dbConn.DateTime,default=datetime.utcnow,nullable=False )
    updated=dbConn.Column(dbConn.DateTime, onupdate=datetime)
    
    def __init__(self):
        return
    
    def transform_jsonb_accounts(self):
        return{
            'id':self.id,
            'fullName':self.fullName,
            'email':self.email,
            'roleId':self.roleId,
            'isActived':self.isActived,
            'created':self.created,
            'updated':self.updated           
        }        

    def login(self, email, password): # Autehticación    
        print('Autenticando')
        try:
            account = self.get_by_email(Accounts,email)        
            if account is None or not check_password_hash(account.passw, password):
                print ("Usuario o clave no validos")
                return         
            return account
        except Exception as ex:
            print("Algo salio mal, "+ex)
            return False
        
    def get_by_email(self, mail):        
        try:
            print ('Buscando email: '+ mail +"-")
            account = Accounts.query.filter_by(email=mail).first()        
            print(account)
            if account is None:
                print ('email no existe')
                return            
            return account
        except Exception as ex:
            return None
    def encrypt_password(self, password):    
        print("encriptando: " + password)
        return generate_password_hash(password)
