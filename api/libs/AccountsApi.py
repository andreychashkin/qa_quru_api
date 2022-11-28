from .BaseApi import BaseApi


class AccountsApi(BaseApi):

    def create_account(self, **data):
        """Создание аккаунта на сервере"""
        return self.call_method('post', 'api/v1/accounts', data)

    def delete_account(self, number):
        """Метод удаляет аккаунт на сервере (абонента) по его номеру"""
        return self.call_method('delete', f'api/v1/account/{number}', data=None)

    def delete_accounts(self, **data):
        """Удаление списка абонентов - на вход массив номеров абонентов"""
        return self.call_method('post', f'api/v1/delete_accounts', data)

    def get_accounts_list(self, **params):
        """Метод возвращает список всех аккаунтов сервера"""
        return self.call_method('get', 'api/v1/accounts', params)

    def update_account_setting(self, number, **data):
        """Метод изменяет настройки аккаунта"""
        return self.call_method('patch', f'api/vi/account/{number}', data)

    def get_list_allowed_accounts_in_conf(self, conf, **params):
        """Метод возвращает список аккаунтов доступных для добавления в указанную конференцию"""
        return self.call_method('get', f'api/v1/allowed_accounts/{conf}', params)

    def get_data_account(self, number, **params):
        """Метод возвращает настройки аккаунта"""
        return self.call_method('get', f'api/v1/account/{number}', params)

    def get_list_allowed_accounts_moderators(self, conf, **params):
        """Метод возвращает список аккаунтов доступных для назначения модераторами в указанную конференцию"""
        return self.call_method('get', f'api/v1/allowed_moderators/{conf}', params)

