import time

import requests
import json
import allure
from . import TestData


class CallsApi():

    @staticmethod
    def polycom_open():
        """Открываем приложение polycom desktop"""
        with allure.step('Открываем приложение polycom'):
            request = requests.get(url=f'http://{TestData.call_ip}/polycom_open')
        return request

    @staticmethod
    def polycom_close():
        """Закрываем приложение polycom desktop"""
        with allure.step('Закрываем приложение polycom'):
            request = requests.get(url=f'http://{TestData.call_ip}/polycom_close')
        return request

    @staticmethod
    def polycom_update_settings(**data):
        """Выполняем запрос на изменение настроек удаленного polycom"""
        with allure.step('Изменяем настройки polycom'):
            request = requests.post(url=f'http://{TestData.call_ip}/polycom_update_settings', data=json.dumps(data))
        return request

    @staticmethod
    def polycom_get_settings():
        """Выполняем запрос настроек удаленного polycom"""
        with allure.step('Запрашиваем настройки приложение polycom'):
            request = requests.get(url=f'http://{TestData.call_ip}/polycom_get_settings')
        return request

    @staticmethod
    def polycom_call(number, protocol):
        """Вызываем с удаленного поликома number protocol (SIP или H323)"""
        with allure.step('Выполняем вызов через приложение polycom'):
            request = requests.post(url=f'http://{TestData.call_ip}/polycom_call',
                                    data=json.dumps({'number': number, 'protocol': protocol}))
        return request

    @staticmethod
    def desktop_call(number):
        """Выполняем вызов с vinteo desktop на number, открывает приложение и выполняет вызов"""
        with allure.step('Выполняем вызов через приложение VinteoDesktop'):
            request = requests.post(url=f'http://{TestData.call_ip}/desktop_call',
                                    data=json.dumps({'number': number}))
            time.sleep(15)
        return request

    @staticmethod
    def desktop_open():
        """Открываем приложение vinteo desktop"""
        with allure.step('Открываем приложение VinteoDesktop'):
            request = requests.get(url=f'http://{TestData.call_ip}/desktop_open')
        return request

    @staticmethod
    def desktop_close():
        """Закрываем приложение vinteo desktop"""
        with allure.step('Закрываем приложение VinteoDesktop'):
            request = requests.get(url=f'http://{TestData.call_ip}/desktop_close')
        return request
