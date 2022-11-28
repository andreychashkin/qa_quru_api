from .BaseApi import BaseApi


class MailApi(BaseApi):

    def get_mail_settings(self):
        """Получение настроек email"""
        return self.call_method('get', 'api/v2/system/mail/settings', None)

    def update_mail_settings(self, **settings):
        """Изменение настроек email"""
        return self.call_method('patch', 'api/v2/system/mail/settings', settings)

    def test_current_email(self, **settings):
        """Проверка отправки email"""
        return self.call_method('post', 'api/v2/system/mail/test', settings)

    def get_declared_email(self):
        """Получить шаблон email"""
        return self.call_method('get', 'api/v2/system/mail/templates', None)

    def get_specified_templates(self, templates):
        """Получить указанный шаблон email"""
        return self.call_method('get', f'api/v2/system/mail/templates/{templates}', None)

    def set_templates(self, templates, content):
        """Установить содержимое шаблона"""
        return self.call_method('get', f'api/v2/system/mail/templates/{templates}', data={'content': content})

    def preview_email(self, templates):
        """Предварительный просмотр"""
        return self.call_method('post', f'api/v2/system/mail/templates/{templates}/preview', None)

    def reset_email(self, templates):
        """Сбросить содержимое шаблона почты"""
        return self.call_method('post', f'api/v2/system/mail/templates/{templates}/reset', None)
    