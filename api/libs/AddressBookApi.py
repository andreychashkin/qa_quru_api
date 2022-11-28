from uuid import uuid4
from .BaseApi import BaseApi


class AddressBookApi(BaseApi):

    def address_book_get_groups(self, **params):
        """Возвращает список групп адресной книги сервера"""
        return self.call_method('get', 'api/v2/addressBook/groups', params)

    def address_book_delete_groups(self, name):
        """Удаляет группу по ее uid"""
        return self.call_method('delete', f'api/v2/addressBook/groups/{self.address_book_get_uuid(name)}', data=None)

    def address_book_get_uuid(self, name):
        """Метод возвращает uuid группы адресной книги по ее имени"""
        groups_list = self.address_book_get_groups().json()['list']
        if not(groups_list == []):
            for i in groups_list:
                if type(i) == dict and name in i.values():
                    return i['identity']
        return None

    def address_book_get_contacts(self, **params):
        """Возвращает список адресов в адресной книге"""
        return self.call_method('get', 'api/v2/addressBook/contacts', params)

    def address_book_created_contacts(self, **param):
        """Метод создает контакт в адресной книге"""
        data = self.create_data({'identity': str(uuid4())}, param)
        return self.call_method('post', 'api/v2/addressBook/contacts', data=data)
    
    def address_book_get_contact_uuid(self, name):
        """Метод возвращает uuid группы адресной книги по ее имени"""
        contacts_list = self.address_book_get_contacts().json()['list']
        if not(contacts_list == []):
            for i in contacts_list:
                if type(i) == dict and name in i.values():
                    return i['identity']
        return None

    def address_book_delete_contacts(self, name):
        """Удаляет контакт по ее uid"""
        return self.call_method(
            'delete', f'api/v2/addressBook/contacts/{self.address_book_get_contact_uuid(name)}', data=None)

    def address_book_created_profile(self, **params):
        """Метод создает профиль адресной книги"""
        uuid_profile = str(uuid4())
        data = self.create_data({'uuid': uuid_profile}, params)
        return self.call_method('put', f'api/v2/addressBook/profiles/{uuid_profile}', data=data)

    def address_book_get_profile(self, **params):
        """Возвращает список профилей в адресной книге"""
        return self.call_method('get', 'api/v2/addressBook/profiles', params)
    
    def address_book_get_profile_uuid(self, name):
        profile_list = self.address_book_get_profile().json()
        if not(profile_list == []):
            for i in profile_list:
                if type(i) == dict and name in i.values():
                    return i['uuid']
        return None

    def address_book_delete_profile(self, name):
        """Удаляет профиль по его uid, на вход принимает название профиля"""
        try:
            return self.call_method(
                'delete', f'api/v2/addressBook/profiles/{self.address_book_get_profile_uuid(name)}', data=None)
        except:
            return

    def address_book_created_group(self, **data):
        """Создание группы контактов на вход принимается Имя группы, метод так же возвращает это имя и uuid"""
        uuid_group = str(uuid4())
        data = self.create_data(data, {'identity': uuid_group})
        response = self.call_method('post', 'api/v2/addressBook/groups', data)
        return {'uuid': uuid_group, 'response': response}

    def address_book_delete_contacts_list(self, contacts):
        """Метод удаляет массив контактов из книги контактов"""
        return self.call_method('post', 'api/v2/addressBook/batch/contacts/delete', data={'contacts': contacts})
