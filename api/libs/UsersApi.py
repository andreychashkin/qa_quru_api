from .BaseApi import BaseApi

import requests
import json
import allure


class UserApi(BaseApi):

    def create_users(self, **settings):
        """Создание пользователя  на сервере"""
        return self.call_method('post', 'api/v2/users', settings)

    def delete_user(self, user):
        """Удаление пользователя на сервере"""
        return self.call_method('delete', f'api/v2/users/{user}', data=None)

    def update_user(self, user, **data):
        """Изменение настроек пользователя на сервере"""
        return self.call_method('patch', f'api/v2/users/{user}', data)


