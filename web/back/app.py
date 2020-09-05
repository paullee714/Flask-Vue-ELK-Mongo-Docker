from flask import Flask
from flask_cors import CORS

# route pacakge import
from route.test_route import my_test

app = Flask(__name__)
app.secret_key = 'laksdjfoiawjewfansldkfnzcvjlzskdf'

CORS(app)

# route 등록
app.register_blueprint(my_test)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)