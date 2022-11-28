from .BaseApi import BaseApi

import requests
import json
import allure


class OauthApi(BaseApi):

    def create_oauth(self, **settings):
        """Создание oauth провайдера на сервере"""
        return self.call_method('post', 'api/v2/system/oauth/providers', settings)

    def delete_oauth(self, provider):
        """Удаление oauth провайдера на сервере"""
        return self.call_method('delete', f'api/v2/system/oauth/provider/{provider}', data=None)

    def update_oauth(self, provider, **data):
        """Изменение настроек oauth провайдера на сервере"""
        return self.call_method('patch', f'api/v2/system/oauth/provider/{provider}', data)
