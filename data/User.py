import json
class User:
    name = None
    mdn = None
    status = None
    password = None
    pictureUrl = None
    actorId = None
    
    def default(self):
        return json.dumps(self.__dict__)
    
    def toJSON(self):
        return json.dumps(self.__dict__)
