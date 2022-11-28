from .BaseApi import BaseApi


class TenantApi(BaseApi):

    def create_tenant(self, **settings):
        """Создание тенанта на сервере"""
        return self.call_method('post', 'api/v2/tenants', settings)

    def delete_tenant(self, tenant):
        """Удаление тенанта на сервере"""
        return self.call_method('delete', f'api/v2/tenants/{tenant}', data=None)

    def update_tenant(self, tenant, **data):
        """Изменение настроек тенанта на сервере"""
        return self.call_method('patch', f'api/v2/users/{tenant}', data)