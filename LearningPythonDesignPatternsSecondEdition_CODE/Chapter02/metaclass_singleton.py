__author__ = 'Chetan'

class MetaSingleton(type):
    
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

## python 3
# class Logger(metaclass=MetaSingleton):
#     pass

## python 2.7
class Logger():
	__metaclass__=MetaSingleton

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
