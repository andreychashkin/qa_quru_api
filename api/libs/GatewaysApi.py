from .BaseApi import BaseApi


class GatewaysApi(BaseApi):

    def create_gateways(self, **settings):
        """Создание шлюза на сервере на вход принимаются настройки {}"""
        return self.call_method('post', 'api/v1/gateways', settings)

    def delete_gateways(self, number):
        """Удаление шлюза на сервере"""
        return self.call_method('delete', f'api/v1/gateway/{number}', data=None)

    def update_gateways(self, number, **data):
        """Изменение настроек шлюза на сервере"""
        return self.call_method('patch', f'api/v1/gateways/{number}', data)
