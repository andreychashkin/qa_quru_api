from .BaseApi import BaseApi


class AccountGroupApi(BaseApi):

    def account_group_list_group(self, **param):
        """Получить список групп"""
        return self.call_method('get', 'api/v2/accounts/groups', param)
    
    def account_group_created(self, **data):
        """Создание группы на сервере"""
        return self.call_method('post', 'api/v2/accounts/groups', data)

    def account_group_delete(self, name):
        """Удаление группы по ее имени"""
        id_group = self.get_id_group(name)
        return self.call_method('delete', f'api/v2/accounts/groups/{id_group}', data=None)

    def account_group_add_contacts(self, name_group, **data):
        """Добавляет контакты в группу контактов сервера"""
        return self.call_method('post', f'api/v2/accounts/groups/{self.get_id_group(name_group)}/addAccounts', data)

    def get_id_group(self, name):
        """Получение id группы по ее имени"""
        list_group = self.account_group_list_group().json()
        for i in list_group:
            if name in i.values():
                return i['id']
        return 
