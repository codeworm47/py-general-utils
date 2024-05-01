import aiohttp
import logging


class RestClientAsync:

    @staticmethod
    async def call_get(url: str, auth_token: str = None, custom_headers: dict = None):
        logging.debug("executing GET call to %s, token %s, customer headers %s", url, auth_token, custom_headers)
        headers = {}
        try:
            if auth_token is not None:
                headers['Authorization'] = f'Bearer {auth_token}'
            if custom_headers:
                headers.update(custom_headers)
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as response:
                    logging.debug("response : %s", response)
                    return response.json()
        except Exception as ex:
            logging.exception(ex)
            raise ex
