from flask import Blueprint,jsonify

# logging lib
from util.my_log import back_logger_info
from back_lib import connect_db

my_test = Blueprint('test',__name__)

@my_test.route('/',methods=['GET'])
def test_router():
    back_logger_info('hello world api!')

    client = connect_db.connect_mongo()
    back_logger_info(client)

    return jsonify("hello world!")