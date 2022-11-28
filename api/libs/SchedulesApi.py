from .BaseApi import BaseApi


class SchedulesApi(BaseApi):

    def delete_conf_in_schedules(self, **data):
        """Удаление планировки в расписании на сервере"""
        return self.call_method('post', 'api/v1/delete_schedules', data)

