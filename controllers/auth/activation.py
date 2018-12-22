from database import database_manager as manager
from flask import Blueprint
from flask import request
import utilities.messages as messages
from utilities.utils import isEmpty, isValidMDN
from flask import jsonify
from data.BaseResponse import BaseResponse

activation_api = Blueprint('activation_api', __name__)

@activation_api.route('/activate',methods=['POST'])
def activateUser(): 
    mdn = request.json['mdn']
    otp = request.json['otp']
    response = BaseResponse()
    response.status = True
    response.message = messages.success_activation
        
    if (not isValidMDN(mdn)):
        response.status = False
        response.message = messages.error_invalid_mdn_length
    else:
        activationStatus = manager.activateUser(mdn, otp)
        if(not isEmpty(activationStatus)):
            response.message = activationStatus
            response.status = False
      
    return jsonify(response.serialize()) 
