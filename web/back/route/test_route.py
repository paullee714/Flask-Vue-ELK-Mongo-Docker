from flask import Blueprint

# logging lib
from util.my_log import back_logger_info

my_test = Blueprint('test',__name__)

@my_test.route('/',methods=['GET'])
def test_router():
    back_logger_info('hello world api!')
    return "hello world!"