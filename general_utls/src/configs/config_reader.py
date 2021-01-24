import logging
import json
import os
from functools import lru_cache


class Config:
    def __init__(self, file_path: str):
        self.file_path = file_path

    @lru_cache(maxsize=128)
    def __read(self, file_path: str):
        try:
            base_path = os.getcwd()  # os.path.abspath(os.curdir)
            address = f'{base_path}/{file_path}'
            with open(address, 'r') as f:
                return json.load(f)
        except FileNotFoundError as ex:
            logging.error(ex)
            raise ex

    def read(self, key: str, section: str = None):
        try:
            config = self.__read(self.file_path)
            if not section:
                return config[key]
            else:
                return config[section][key]
        except KeyError as ex:
            logging.exception(ex)
            raise ex

    def read_int(self, key: str, section: str = None) -> int:
        try:
            if not key:
                return 0
            str_val = self.read(key, section)
            return int(str_val)
        except ValueError as ex:
            logging.exception(ex)
            raise ex

    def read_bool(self, key: str, section: str = None) -> bool:
        try:
            if not key:
                return False
            str_val = self.read(key, section)
            return bool(str_val)
        except ValueError as ex:
            logging.exception(ex)
            raise ex

    def read_float(self, key: str, section: str = None) -> float:
        try:
            if not key:
                return 0
            str_val = self.read(key, section)
            return float(str_val)
        except ValueError as ex:
            logging.exception(ex)
            raise ex
