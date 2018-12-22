from sqlalchemy.inspection import inspect
from utilities.utils import getFormattedKey

class Serializer(object):

    def serialize(self):
        output = {getFormattedKey(c): getattr(self, c) for c in inspect(self).attrs.keys()}
        return output

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
        