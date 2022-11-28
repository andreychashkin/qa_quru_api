from .BaseApi import BaseApi

import requests
import json
import allure


class ApiKeysApi(BaseApi):

    def create_api_key(self, **settings):
        """Создание апи ключа на сервере"""
        return self.call_method('post', 'api/v2/apiKeys', settings)

    def delete_api_key(self, key):
        """Удаление апи ключа на сервере"""
        return self.call_method('delete', f'api/v2/apiKeys/{key}', data=None)

    def update_api_key(self, key, **data):
        """Изменение настроек апи ключа на сервере"""
        return self.call_method('patch', f'api/v2/apiKeys/{key}', data)
