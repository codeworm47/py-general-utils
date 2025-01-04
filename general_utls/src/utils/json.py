import json
from datetime import datetime

from general_utls.src.types.dates import Dates


class DateAwareJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return Dates.to_string(o)
        return json.JSONEncoder.default(self, o)


class JSON:
    @staticmethod
    def stringify(obj):
        return json.dumps(obj, cls=DateAwareJSONEncoder)
