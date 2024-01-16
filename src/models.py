from src import dbConn
from datetime import datetime

class Roles(dbConn.Model):
    id=dbConn.Column( dbConn.Integer,primary_key=True,autoincrement=True)
    name=dbConn.Column( dbConn.String(255), nullable=False)
    description=dbConn.Column( dbConn.String(255))
    created=dbConn.Column( dbConn.DateTime,default=datetime,nullable=False )
    updated=dbConn.Column(dbConn.DateTime, onupdate=datetime)
    
    def transform_jsonb_roles(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'created':self.created,
            'updated':self.updated
            
        }        
from src import dbConn
from datetime import datetime   
   
class pingTest(dbConn.Model):
    id=dbConn.Column( dbConn.Integer,primary_key=True,autoincrement=True)    
    accountId=dbConn.Column(dbConn.Integer,nullable=False)
    description=dbConn.Column(dbConn.String(255),nullable=True)
    deviceId=dbConn.Column(dbConn.Integer,nullable=False)  
    origin=dbConn.Column(dbConn.Integer,nullable=False )    
    created=dbConn.Column(dbConn.DateTime,default=datetime.utcnow,nullable=False )
    updated=dbConn.Column(dbConn.DateTime, onupdate=datetime.utcnow)
    
    def transform_jsonb_package(self):
        return{
            'id':self.id,
            'accountId':self.accountId,
            'description':self.description,
            'deviceId':self.deviceId,
            'origin':self.origin,
            'created':self.created,
            'updated':self.updated            
        }        
