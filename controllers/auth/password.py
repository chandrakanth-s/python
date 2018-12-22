from database import database_manager as manager
from flask import Blueprint
from flask import request
import utilities.messages as messages
from utilities.utils import isValidMDN, isEmpty
from flask import jsonify
from database.schema_declarative import RegistrationStatus
from data.BaseResponse import BaseResponse

password_api = Blueprint('password_api', __name__)

@password_api.route('/password/create',methods=['POST'])
def createPassword(): 
    actorId = request.json['actorId']
    mdn = request.json['mdn']
    authKey = request.json['authKey']   
    response = BaseResponse()
    response.status = False
    response.message = messages.error_server
        
    if (isEmpty(actorId)):
        response.message = messages.error_field_empty %("actorId")
    elif(not isValidMDN(mdn)):
        response.message = messages.error_invalid_mdn_length
    else:
        userStatus = manager.isUserExists(mdn)   
        if(userStatus == None):
            response.message = messages.error_user_not_exits
        elif (userStatus.status!=RegistrationStatus.ACTIVE):
            response.message = messages.error_not_activated
        elif (userStatus.actor_id!=actorId):
            response.message = messages.error_not_match_mdn_actorid
        else:
            if(not manager.createPassword(actorId, authKey)):
                response.message = messages.error_server  
            else:
                response.status = True
                response.message = messages.success_create_password  
      
    return jsonify(response.serialize())
