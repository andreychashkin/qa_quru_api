from .BaseApi import BaseApi

import requests
import json
import allure


class WebhooksApi(BaseApi):

    def create_subscribers(self, **settings):
        """Создание подписчика  на сервере"""
        return self.call_method('post', 'api/v2/webhooks/subscribers', settings)

    def delete_subscriber(self, subscriber):
        """Удаление подписчика на сервере"""
        return self.call_method('delete', f'api/v2/webhooks/subscribers/{subscriber}', data=None)

    def update_subscriber(self, subscriber, **data):
        """Изменение настроек подписчика на сервере"""
        return self.call_method('patch', f'api/v2/webhooks/subscribers/{subscriber}', data)
