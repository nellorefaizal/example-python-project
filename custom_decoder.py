
import json
from json import JSONEncoder

class Animal:
    def __init__(self,name):
        self.name=name
pye={'a':Animal('avakado'),'b':Animal('bear'),'c':Animal('Cat')}
class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o)==Animal:
            return o.name
        else:
            super().default(o)


print(json.dumps(pye,cls=AnimalEncoder))