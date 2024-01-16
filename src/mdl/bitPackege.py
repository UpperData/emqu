from src import dbConn
from datetime import datetime
    
   
class bitPackage(dbConn.Model):
    id=dbConn.Column( dbConn.Integer,primary_key=True,autoincrement=True)    
    testId=dbConn.Column( dbConn.Integer,primary_key=True)    
    deviceId=dbConn.Column(dbConn.String(255),nullable=False)    
    host=dbConn.Column(dbConn.String(255),nullable=False ) #IP del equipo de Origen       
    isRecived=dbConn.Column(dbConn.Boolean,default=True )
    isSended=dbConn.Column(dbConn.Boolean,default=True )    
    created=dbConn.Column(dbConn.DateTime,default=datetime.utcnow,nullable=False )
    updated=dbConn.Column(dbConn.DateTime, onupdate=datetime.utcnow)
    
    def __init__(self):
        return
    
    def transform_jsonb_bitPackage(self):
        return{
            'testId':self.testId,            
            'deviceId':self.deviceId,
            'host':self.host,            
            'isRecived':self.isRecived,
            'isSended':self.isSended,
            'created':self.created,
            'updated':self.updated            
        }
        
    def register(self, testId,deviceId,host,isRecived,isSended): # Registra envio de paquetes
        print('Registrando ping')
        try:
            print("intentando registrar")
            bitPack=self()            
            bitPack.testId=testId
            bitPack.deviceId=deviceId
            bitPack.host=host
            bitPack.isRecived=isRecived
            bitPack.isSended=isSended
            print("Host registrando: " + self.host)
            dbConn.session.add(bitPack)
            print ("Agregado")
            dbConn.session.commit()            
            print("Ping registrado")
            return True
        except Exception as ex:
            dbConn.session.rollback()
            print("Algo salio mal, "+ex)
            return False
        
    def get_by_deviceId(self, ip):        
        try:
            print ('Buscando IP: '+ ip +"/")
           # bitPack=self()
            bitPack = bitPackage.query.filter_by(deviceId=ip)
            bitPack=list(map(lambda x: x.serialize(), bitPack))    
            #print(bitPack)
            if len(bitPack) ==0:
                print ('ip sin tests')
                return            
            return bitPack
        except Exception as ex:
            return None