import json


class Request:
    def to_json(self):
        return json.dumps(self.__dict__)
