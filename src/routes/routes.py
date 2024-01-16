from . import api_routes
from .. import dbConn
from ..mdl.accounts import Accounts
from ..mdl.bitPackege import bitPackage
from flask import jsonify, request
from subprocess import Popen, PIPE
import jwt
from decouple import config as conf
import socket
import platform
import subprocess
from numpy import size, array 
## Cuentas de usuario ###############################################################
@api_routes.route('/AccOUnt/list',methods=['GET']) #Listar usuario del sistema
def List():
    try:
        list=[]
        for row  in Accounts.query.all():
            list.append(row.transform_jsonb_accounts())
        #response=jsonify({'rs':list})    
        response={"success":True,"message":'Busqueda satisfactoria',"data":list},200
        return response
    except Exception as ex:
        response={"success":False,"message":'Algo salió mal, intente nuevamente',"data":ex},401
        return response

@api_routes.route('/AccOunt/signin',methods=['POST']) #Inicio de seion
def signin():    
    try:
        data=request.get_json()    
        
        email=data['email']
        passw=data['passw']
        print("invocando login "+ passw +" "+ email)
        account=Accounts.login(Accounts,email,passw)        
        print("Login -> " + str(account))
        if account is not None:
            token=jwt.encode(
                    {"accountId":account.id,
                     "email": account.email,
                     "personName":account.fullName, 
                     "roleId":account.roleId},
                    conf('SECRET_KEY'),
                    algorithm="HS256")
            response={"Success":True,"message":'Usuario autenticado como '+email,"accessToken":token},200            
            return response
        response={"Success":False,"message":'Email o password no validos'},401
        return response
    except Exception as ex:
        print("Algo salió mal en login "+ex)
        
@api_routes.route('/ACcOUnt/ADD',methods=['POST']) #Agregar usuarios al sistema
def newAccount():
    try:        
        data=request.get_json()    
        fullName=data['fullName']
        email=data['email']
        roleId=data['roleId']
        isActived=data['isActived']
        passw=data['passw']
        account=Accounts()
        account.fullName=fullName
        account.email=email
        account.roleId=roleId
        account.isActived=isActived        
        account.passw=Accounts.encrypt_password(Accounts,passw)        
        dbConn.session.add(account)
        dbConn.session.commit()
        response={"success":True,"message":'Cuenta agregada satisfactoriamente',"data":""},200
        return response
    except Exception as ex:
        dbConn.session.rollback()
        response={"success":False,"message":'Algo saliio mal',"data":ex},401
        return response
## FIN CUENTAS DE USUARIO ###################################################################

### Ping Testing ############################################################################
@api_routes.route('/Testing/prossesing',methods=['POST']) #Hace PING
def ping ():
    print("iniciando")
    data=request.get_json()    
    testId=data['testId']    
    hostList=data['deviceId']        
    tries=data['tries']    
    origin=socket.gethostbyname(socket.gethostname())    
    print("IP Origen: "+origin)
    print("IP Destino: "+hostList[0])        
    parameter = "-n" if platform.system().lower() == "windows" else "-c"    
    try:
        print("intentando")
        print("tamaño arreglo: "+ str(size(hostList)))
        for i in range(size(hostList)):
            print (hostList[i])
            for c in range(tries):                    
                isSended=True
                cmd = ["ping", parameter, "1", hostList[i]]
                response = subprocess.call(cmd)
                print (response)
                if response == 0:
                    isRecived=True                
                else:
                    isRecived=False                                            
                print('registrar ping')
                bitPackage.register(bitPackage, testId,hostList[i],origin,isRecived,isSended)                    
        response={"success":True,"message":'Pureba finalizada con exito',"data":""},200
        return response
    except Exception as ex:
        dbConn.session.rollback()
        response={"success":False,"message":'Algo salio mal, intente nuevamente',"data":ex},402
        return response

@api_routes.route('/Testing/report/devide',methods=['POST']) #Resultados por equipo
def getHistory ():
    try:
        data=request.get_json()    
        deviceId=data['deviceId']
        #print("IP: "+ deviceId)
        rs=bitPackage.get_by_deviceId(bitPackage,deviceId)        
        print(rs)
        response={"success":True,"message":'Consulta satisfactoria',"data":bitPackage},200
        return response
    except Exception as ex:
        response={"success":False,"message":'Algo salió mal, intente nuevamente',"data":ex},402
        return response
    

