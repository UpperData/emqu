from src import dbConn
from datetime import datetime
    
   
class Devices(dbConn.Model):
    id=dbConn.Column( dbConn.Integer,primary_key=True,autoincrement=True)
    typeId=dbConn.Column(dbConn.Integer, nullable=False)
    makerId=dbConn.Column(dbConn.Integer, unique=True,nullable=False)    
    ipv4=dbConn.Column(dbConn.String(255),nullable=False )
    departament=dbConn.Column(dbConn.String(255),nullable=False )
    domainName=dbConn.Column(dbConn.String(255),nullable=False)
    personName=dbConn.Column(dbConn.String(255),nullable=False)
    isOperative=dbConn.Column(dbConn.Boolean,default=True )
    osId=dbConn.Column(dbConn.Integer )
    created=dbConn.Column(dbConn.DateTime,default=datetime.utcnow,nullable=False )
    updated=dbConn.Column(dbConn.DateTime, onupdate=datetime.utcnow)
    
    def transform_jsonb_devices(self):
        return{
            'id':self.id,
            'typeId':self.typeId,
            'makerId':self.makerId,
            'ipv4':self.ipv4,	
            'departament':self.departament,
            'domainName':self.domainName,
            'personName':self.personName,
            'isOperative':self.isOperative,
            'osId':self.osId,
            'created':self.created,
            'updated':self.updated
        }        
