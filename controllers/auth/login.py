from flask import Blueprint
from flask import request
from utilities.utils import isValidMDN, isEmpty
from utilities import messages
from database import database_manager as manager
from database.schema_declarative import RegistrationStatus
from data.LoginResponse import LoginResponse
from flask.json import jsonify

login_api = Blueprint('login_api', __name__)

@login_api.route('/login',methods=['POST'])
def login():
    mdn = request.json['mdn']
    authKey = request.json['authKey'] 
    
    baseResponse = LoginResponse()
    baseResponse.status = False  
    baseResponse.message = messages.failure_login
    
    if (not isValidMDN(mdn)):
        baseResponse.message = messages.error_invalid_mdn_length    
    elif (isEmpty(authKey)):
        baseResponse.message = messages.error_field_empty % ("password")
    else:
        user = manager.isUserExists(mdn)
        if(user==None):
            baseResponse.message = messages.error_user_not_exits
        else:
            if(user.status == RegistrationStatus.ACTIVATION_PENDING):
                baseResponse.message = messages.error_not_activated
            elif(not manager.isPasswordCreated(user.actor_id)):
                baseResponse.message = messages.error_password_not_created
            elif(not manager.isValidPassword(user.actor_id,authKey)):
                baseResponse.message = messages.failure_password
            else:
                baseResponse.status = True   
                baseResponse.message = messages.success_login            
                baseResponse.user = user.serialize()
                       
    return jsonify(baseResponse.serialize())
