class WebClientAsync:
    @classmethod
    async def get_html(cls, url):
        async with httpx.AsyncClient(headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }) as client:
            response = await client.get(url)
            response.raise_for_status()
        return response.text
