import json

from pandas import Timestamp


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Timestamp):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
