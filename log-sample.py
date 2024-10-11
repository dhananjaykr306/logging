import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x,y):
    """ Add Function """
    return x + y

def subtract(x, y):
    """ Subtract Function """
    return x-y

def multiply(x,y):
    """ multuply function """    
    return x*y

def divide(x,y):
    """ Divide Function """
    try:
        result = x/y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        return result
logging.basicConfig(filename ='sample.log',level = logging.DEBUG,
                    format ='%(asctime)s:%(levelname)s:%(message)s')

num1 = 20
num2 = 0

"""add_result = add(num1 , num2)
print('Add: {} + {} = {}'.format(num1,num2,add_result))

sub_result = subtract(num1, num2)
print('Add: {} - {} = {}'.format(num1,num2,sub_result))

mul_result =multiply(num1, num2)
print('Add: {} * {} = {}'.format(num1,num2,mul_result))

div_result = divide(num1, num2)
print('Add: {} / {} = {}'.format(num1,num2,div_result))
"""

add_result = add(num1 , num2)
logger.debug('Add: {} + {} = {}'.format(num1,num2,add_result))

sub_result = subtract(num1, num2)
logger.debug('subtract: {} - {} = {}'.format(num1,num2,sub_result))

mul_result =multiply(num1, num2)
logger.debug('Multiply: {} * {} = {}'.format(num1,num2,mul_result))

div_result = divide(num1, num2)
logger.debug('Division: {} / {} = {}'.format(num1,num2,div_result))
