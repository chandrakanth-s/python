from flask import Flask
from controllers.registration.registration import registration_api
from controllers.auth.login import login_api
from controllers.auth.activation import activation_api
from controllers.auth.password import password_api
from controllers.document_upload.upload import upload_api
from controllers.post.post_manager import post_api
from controllers.startup_error_handler import errors

app = Flask(__name__)
app.register_blueprint(registration_api)
app.register_blueprint(login_api)
app.register_blueprint(activation_api)
app.register_blueprint(password_api)
app.register_blueprint(upload_api)
app.register_blueprint(post_api)
app.register_blueprint(errors)

@app.route("/")
def hello():
    return "Welcome to startup API"

if __name__ == "__main__": 
    app.run(debug = True)
