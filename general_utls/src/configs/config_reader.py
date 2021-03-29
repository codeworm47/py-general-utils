import logging
import json
import os
import abc
from functools import lru_cache
from jsonget import json_get


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

    def read(self, key: str, obj_path: str = None):
        try:
            if not key:
                raise ValueError("key is not provided to read args")
            config = self.__read(self.file_path)
            if not obj_path:
                return config[key]
            else:
                return json_get(config, self.__get_obj_path(key, obj_path))
        except KeyError as ex:
            logging.exception(ex)
            raise ex

    def read_int(self, key: str, obj_path: str = None) -> int:
        try:
            if not key:
                raise ValueError("key is not provided to read_int args")
            str_val = self.read(key, obj_path)
            return int(str_val)
        except ValueError as ex:
            logging.exception(ex)
            raise ex

    def read_bool(self, key: str, obj_path: str = None) -> bool:
        try:
            if not key:
                raise ValueError("key is not provided to read_bool args")
            str_val = self.read(key, obj_path)
            return bool(str_val)
        except ValueError as ex:
            logging.exception(ex)
            raise ex

    def read_float(self, key: str, obj_path: str = None) -> float:
        try:
            if not key:
                raise ValueError("key is not provided to read_float args")
            str_val = self.read(key, obj_path)
            return float(str_val)
        except ValueError as ex:
            logging.exception(ex)
            raise ex

    @staticmethod
    def __get_obj_path(key: str, obj_path: str):
        if not obj_path.startswith("/"):
            return "/" + obj_path + "/" + key
        return obj_path + "/" + key


class Env:
    @classmethod
    def read(cls, key: str):
        try:
            if not key:
                raise ValueError("key is not provided to method args")
            value = os.environ[key]
            if not value:
                raise EnvironmentError(f"environment variable ${key} is not set.")
            return value
        except Exception as ex:
            logging.exception(ex)
            raise ex

    @classmethod
    def read_int(cls, key: str) -> int:
        return int(cls.read(key))

    @classmethod
    def read_float(cls, key: str) -> float:
        return float(cls.read(key))

    @classmethod
    def read_bool(cls, key: str) -> bool:
        return bool(cls.read(key))


