class BaseResponse():
    status = False
    message = None
    
    def serialize(self):
        return self.__dict__
    
    
    
