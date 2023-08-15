import logging
from functools import lru_cache
from jsonget import json_get

from general_utls.src.io.file_helpers import Files


class Config:
    def __init__(self, file_path: str):
        self.file_path = file_path

    @lru_cache(maxsize=128)
    def __read(self, file_path: str):
        address = ""
        try:
            return Files.read_json_relative(file_path)
        except FileNotFoundError as ex:
            logging.error("file %s not found", address)
            logging.error(ex)
            raise ex

    def read(self, key: str, obj_path: str = None):
        try:
            if not key:
                raise KeyError("key is not provided to read args")
            config = self.__read(self.file_path)
            if not obj_path:
                if key not in config:
                    return None
                return config[key]
            else:
                return json_get(config, self.__get_obj_path(key, obj_path))
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def read_int(self, key: str, obj_path: str = None) -> int:
        try:
            if not key:
                raise KeyError("key is not provided to read_int args")
            str_val = self.read(key, obj_path)
            return int(str_val)
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def read_bool(self, key: str, obj_path: str = None) -> bool:
        try:
            if not key:
                raise KeyError("key is not provided to read_bool args")
            str_val = self.read(key, obj_path)
            return bool(str_val)
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def read_float(self, key: str, obj_path: str = None) -> float:
        try:
            if not key:
                raise ValueError("key is not provided to read_float args")
            str_val = self.read(key, obj_path)
            return float(str_val)
        except Exception as ex:
            logging.exception(ex)
            raise ex

    @staticmethod
    def __get_obj_path(key: str, obj_path: str):
        if not obj_path.startswith("/"):
            return "/" + obj_path + "/" + key
        return obj_path + "/" + key


