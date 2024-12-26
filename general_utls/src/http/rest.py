from typing import Dict

import aiohttp
import logging


class RestClientAsync:

    @staticmethod
    async def get(url: str, url_params: Dict = None, auth_token: str = None, custom_headers: Dict = None):
        headers = {}

        msg = f"executing GET call to {url}"
        if auth_token:
            msg += f", auth token: {auth_token}"
            headers['Authorization'] = f'Bearer {auth_token}'
        if custom_headers:
            msg += f", custom headers: {custom_headers}"
            headers.update(custom_headers)
        logging.debug(msg)

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, params=url_params) as response:
                logging.debug("response status code : %s", response.status)
                return response.json()
