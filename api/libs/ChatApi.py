from .BaseApi import BaseApi


class ChatApi(BaseApi):
    def display_name_in_chat(self, **value):
        """Ввод имени в чате"""
        return self.call_method('post', 'api/v1/messages/display_name', value)

    def send_message_in_chat(self, **data):
        """Отправление сообщения в чате на ввод нужен номер конференции и тело сообщения"""
        return self.call_method('post', 'api/v1/messages', data)

    def delete_message_in_chat(self, **data):
        """Удаление сообщение в чате на ввод методу нужен номер конференции и id сообщения"""
        return self.call_method('delete', 'api/v1/messages', data)

    def enable_chat(self, number):
        """Метод включает чат в указоной по номеру конференции"""
        return self.api_test('patch', f'api/v1/webcast/{number}', chat=True)