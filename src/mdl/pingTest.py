from src import dbConn
from datetime import datetime   
   
class test(dbConn.Model):
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
