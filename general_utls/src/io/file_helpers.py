import json
import os


class Files:
    @classmethod
    def get_absolute_path(cls, file_path):
        base_path = os.getcwd()  # os.path.abspath(os.curdir)
        return f'{base_path}/{file_path}'

    @classmethod
    def read_json_relative(cls, file_path: str):
        with open(cls.get_absolute_path(file_path), 'r') as f:
            return json.load(f)

    @classmethod
    def read_raw_relative(cls, file_path: str):
        with open(cls.get_absolute_path(file_path), 'r') as f:
            return f.read()
