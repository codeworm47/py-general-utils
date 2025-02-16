from typing import Dict, Any

import httpx
import logging


def grab_headers_and_log(verb: str, url: str, auth_token: str = None, custom_headers: Dict = None) -> Dict[str, str]:
    headers = {}

    msg = f"executing {verb} call to {url}"
    if auth_token:
        msg += f", auth token: {auth_token}"
        headers['Authorization'] = f'Bearer {auth_token}'
    if custom_headers:
        msg += f", custom headers: {custom_headers}"
        headers.update(custom_headers)
    logging.debug(msg)

    return headers


class RestClientAsync:

    @staticmethod
    async def get(url: str, url_params: Dict = None, auth_token: str = None, custom_headers: Dict = None):
        headers = grab_headers_and_log("GET", url, auth_token, custom_headers)
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=url_params, headers=headers)
            logging.debug("response status code : %s", response.status_code)
            response.raise_for_status()
            return response.json()

    @staticmethod
    async def post(url: str, body: Any, auth_token: str = None, custom_headers: Dict = None):
        headers = grab_headers_and_log("POST", url, auth_token, custom_headers)
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=body, headers=headers)
            logging.debug("response status code : %s", response.status_code)
            response.raise_for_status()
            return response.json()


class RestClient:
    @staticmethod
    def get(url: str, url_params: Dict = None, auth_token: str = None, custom_headers: Dict = None):
        headers = grab_headers_and_log("GET", url, auth_token, custom_headers)
        with httpx.Client() as client:
            response = client.get(url, params=url_params, headers=headers)
            logging.debug("response status code : %s", response.status_code)
            response.raise_for_status()
            return response.json()

    @staticmethod
    def post(url: str, body: Any, auth_token: str = None, custom_headers: Dict = None):
        headers = grab_headers_and_log("POST", url, auth_token, custom_headers)
        with httpx.Client() as client:
            response = client.post(url, json=body, headers=headers)
            logging.debug("response status code : %s", response.status_code)
            response.raise_for_status()
            return response.json()

