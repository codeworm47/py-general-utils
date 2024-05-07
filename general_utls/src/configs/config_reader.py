import logging
from functools import lru_cache

from general_utls.src.io.file_helpers import Files
from general_utls.src.types.dicts import Dicts


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

    def read(self, key: str, obj_path: str = None, default=None, throw_if_not_found=False):
        try:
            if not key:
                raise KeyError("key is not provided to read args")
            config = self.__read(self.file_path)
            _key = f"{obj_path}.{key}" if obj_path else key
            if throw_if_not_found:
                value = Dicts.safe_read(config, _key)
                if not value:
                    raise KeyError(f"key {_key} not found in config {self.file_path}")
            return Dicts.safe_read(config, _key, default)
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def read_int(self, key: str, obj_path: str = None, default=None, throw_if_not_found=False) -> int:
        try:
            value = self.read(key, obj_path, default, throw_if_not_found)
            if value:
                return int(value)
            return default
        except Exception as ex:
            logging.error(ex)
            raise ex

    def read_bool(self, key: str, obj_path: str = None, default=None, throw_if_not_found=False) -> bool:
        try:
            value = self.read(key, obj_path, default, throw_if_not_found)
            if value:
                return bool(value)
            return default
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def read_float(self, key: str, obj_path: str = None, default=None, throw_if_not_found=False) -> float:
        try:
            value = self.read(key, obj_path, default, throw_if_not_found)
            if value:
                return float(value)
            return default
        except Exception as ex:
            logging.exception(ex)
            raise ex


