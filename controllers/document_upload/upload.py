from flask import Blueprint, jsonify
from flask import request
import os
from database import database_manager as manager
from utilities import messages
from utilities.utils import isValidMDN, isEmpty
from data.DocumentUploadResponse import DocumentUploadResponse

upload_api = Blueprint('upload_api', __name__)


@upload_api.route('/upload', methods=['POST'])
def uploadFile():
    response = DocumentUploadResponse()
    response.status = False
    response.message = messages.failure_file_upload
    documentId = None
    if 'file' not in request.files:
        response.message = messages.error_no_file_found
    else:
        fileToSave = request.files['file']
        #fileToSave.save(os.path.join(dbManager.config.get('database-configuration','file_upload_path'),fileToSave.filename))
        fileToSave.save(os.path.join('/home/chandra/Workspace/MyProjects/Python/uploads',fileToSave.filename))
        imageURL = fileToSave.filename
        documentId = manager.addDocument(imageURL,fileToSave.content_type)
        response.documentId = documentId
        if (documentId == None):
            response.message = messages.failure_file_upload  
        else:
            response.status = True
            response.message = messages.success_file_upload 
           
    return jsonify(response.serialize())

@upload_api.route('/updateProfilePicture', methods=['POST'])
def updateProfilePicture():
    response = DocumentUploadResponse()
    response.status = True
    response.message = messages.failure_profile_picture_update 
     
    documentId = request.json['documentId']
    mdn = request.json['mdn']
     
    if(not isValidMDN(mdn)):
        response.message = messages.error_invalid_mdn_length
    elif (isEmpty(documentId)):
        response.message = messages.error_field_empty % ("documentId")
    elif(not manager.isUserExists(mdn)):
        response.message = messages.error_user_not_exits
    else:
        response.status = manager.updateProfilePicture(documentId,mdn) 
        if(not response.status):
            response.message = messages.failure_profile_picture_update
        else:
            response.status = True
            response.message = messages.success_profile_picture_update 
            
    return jsonify(response.serialize())

