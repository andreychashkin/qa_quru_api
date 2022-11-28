import time

import requests
import json
from . import TestData


class BaseApi:
    token = refresher_token = ''
    current_connections = 0
    headers = ''
    second_ip_server = ''
    server_ip = ''
    fake_token = fake_refresher_token = ''

    def __init__(self, server_ip=TestData.ip_server, logins=TestData.login, passwords=TestData.password,
                 fake_token=False):
        self.server_ip = server_ip
        self.second_ip_server = TestData.second_ip
        self.auth_jwt(server_ip, logins, passwords, fake_token)

    def api_test(self, method: str, url: str, **data):
        response = None
        if 'get' in method:
            response = requests.get(url=f'https://{self.server_ip}/{url}', params=data, verify=False,
                                    headers=self.headers)
        if 'post' in method:
            response = requests.post(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                     headers=self.headers)
        if 'patch' in method:
            response = requests.patch(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                      headers=self.headers)
        if 'delete' in method:
            response = requests.delete(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                       headers=self.headers)
        if 'put' in method:
            response = requests.put(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                    headers=self.headers)
        return response

    def call_method(self, method: str, url: str, data):
        response = None
        if 'get' in method:
            response = requests.get(url=f'https://{self.server_ip}/{url}', params=data, verify=False,
                                    headers=self.headers)
        if 'post' in method:
            response = requests.post(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                     headers=self.headers)
        if 'patch' in method:
            response = requests.patch(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                      headers=self.headers)
        if 'delete' in method:
            response = requests.delete(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                       headers=self.headers)
        if 'put' in method:
            response = requests.put(url=f'https://{self.server_ip}/{url}', data=json.dumps(data), verify=False,
                                    headers=self.headers)
        return response

    def auth_jwt(self, server_ip, logins='admin', passwords='123456', fake_token=False):
        url = f'https://{server_ip}/api/v1/auth/jwt'
        response = requests.post(
            url,
            data=json.dumps({"username": logins,
                             "password": passwords}),
            verify=False
        )
        if fake_token:
            self.token = response.json()
            self.refresher_token = response.json()
            self.server_ip = server_ip
            self.headers = {"Authorization": f"Bearer "}
        else:
            try:
                self.token = response.json()["data"]["token"]
                self.refresher_token = response.json()["data"]["refreshToken"]
                self.server_ip = server_ip
                self.headers = {"Authorization": "Bearer" + self.token}
                return response
            except KeyError:
                return response

    @staticmethod
    def create_data(dict_2, dict_1=None):
        """Метод принимает на вход два словаря с параметрами запросов и формирует из двух словарей один
         Метод работает как склейка в случае если нужно к уже полученным настройкам или данным добавить недостающие"""
        if dict_1 is None:
            dict_1 = {}
        data = dict_1
        for setting, value in dict_2.items():
            data = {**data, **{setting: value}}
        return data
