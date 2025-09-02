import string
import uuid
from random import random


class StringUtils:
    @staticmethod
    def random_chars(length) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    @staticmethod
    def partial_uuid(length) -> str:
        return str(uuid.uuid4())[:length]
