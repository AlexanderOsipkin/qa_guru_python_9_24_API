import json

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions


def requests_api(method, url, **kwargs):
    base_url = 'https://petstore.swagger.io'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    new_url = base_url + url
    method = method.upper()
    with allure.step(f"{method} {url}"):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, headers=headers, **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode('utf8'), name='Curl',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            try:
                allure.attach(body=json.dumps(response.json(), indent=4).encode('utf8'), name='Response Json',
                              attachment_type=AttachmentType.JSON, extension='json')
            except:
                allure.attach(body=response.content, name='Response',
                              attachment_type=AttachmentType.TEXT, extension='txt')
        return response