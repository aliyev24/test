import requests

from fake_useragent import UserAgent
user_agent = UserAgent()

class BaseRequest:
    headers = {
        # 'host': 'www.summertour.az',
        "content-Type": "text/javascript; charset=utf-8",
        "user-agent": user_agent.random,
        "connection": "keep-alive",
        "accept-Language": "en-US,en;q=0.5",
        "accept-Encoding": "gzip, deflate",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9," +
                  "image/webp,image/apng,*/*;q=0.8," +
                  "application/signed-exchange;v=b3;q=0.9",
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'empty',
        'upgrade-insecure-requests': '1',
        'dnt': '1',
    }

    def __init__(self,
                 proxy: str = None,
                 headers: dict = None,
                 additional_headers: dict = None,
                 proxy_off=True,
                 ) -> None:

        self.request = requests.Session()

        if headers:
            self.request.headers = headers

        elif additional_headers:
            self.headers.update(additional_headers)
            self.request.headers = self.headers

        else:
            self.request.headers = self.headers

        if proxy_off is False:
            self.set_proxies(proxy=proxy)

    def set_proxies(self, proxy):
        self.request.proxies = {
            "http": proxy,
            "https": proxy,
        }
        self.request.headers['user-agent'] = user_agent.random