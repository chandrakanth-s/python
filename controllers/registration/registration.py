# from database import databasemanager as dbManager
from database import database_manager as manager
from flask import request
from flask import jsonify
from utilities.utils import isEmpty, isValidMDN
import utilities.messages as messages
from flask import Blueprint

registration_api = Blueprint('registration_api', __name__)

@registration_api.route('/register',methods=['POST'])
def registerUser(): 
    name = request.json['name']
    mdn = request.json['mdn']
    global status
    status = True
    global message
    message = messages.success_registration
     
    if (isEmpty(name)):
        status = False
        message = messages.error_field_empty % ("Name")
    elif (not isValidMDN(mdn)):
        status = False
        message = messages.error_invalid_mdn_length
    else:
        resitrationStatus = manager.createUser(name, mdn, "web")
        if(isEmpty(resitrationStatus) == False):
            message = messages.pending_activation
            status = False
            #return json.dumps(resitrationStatus.serialize(), default = dateSerializer)
        
    dat = {
    'message':message,
    'status':status
    }
    
    return jsonify(dat) 

