from flask import Flask
from controllers.teetime_controller import teetime_controller

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(teetime_controller)

if __name__ == '__main__':
    app.run(debug=True)