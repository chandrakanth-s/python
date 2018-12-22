from flask import jsonify
from flask import Blueprint

errors = Blueprint('error', __name__)

@errors.app_errorhandler(Exception)
def handleError(error):
    message = [str(x) for x in error.args]
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }
    
    return jsonify(response), status_code