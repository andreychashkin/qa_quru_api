from .BaseApi import BaseApi
from .PlayersApi import PlayersApi

import requests
import json
import allure
import time
import os


class ConferencesApi(BaseApi):

    def create_conference(self, **data):
        """Метод создает конференцию, на вход принимаются настройки конференции"""
        return self.call_method('post', 'api/v1/conferences', data)

    def delete_conference(self, number):
        """Метод удаляет конференцию с сервера по ее номеру"""
        return self.call_method('delete', f'api/v1/conference/{number}', data=None)

    def delete_conferences(self, **numbers):
        """"Метод удаляет список конференций с сервера по номерам"""
        return self.call_method('post', 'api/v1/delete_conferences', numbers)

    def get_conferences_list(self, **params):
        """Метод возвращается все конференции с параметрами предусмотренными api сервера"""
        return self.call_method('get', 'api/v1/conferences', params)

    def start_conference(self, conference):
        """Метод включает конференцию"""
        return self.call_method('post', 'api/v1/start_conference', data={'conference': conference})

    def stop_conference(self, conference):
        """Останавливаем конференцию"""
        return self.call_method('post', 'api/v1/stop_conference', data={'conference': conference})

    def reboot_conference(self, conference):
        """Метод завершает конференцию и включает ее повторно"""
        self.stop_conference(conference)
        self.start_conference(conference)

    def get_participants_list(self, conf, **params):
        """Метод получает список участников конференции"""
        return self.call_method('get', f'api/v1/participants/{conf}', params)

    def update_conference(self, conference, **data):
        """Метод изменяет настройки конференции """
        return self.call_method('patch', f'api/v1/conference/{conference}', data)

    def add_players(self, conference, players, loop=True):
        """Метод добавляет ролики в конференцию по их id, на вход title плеера"""
        with allure.step(f"Добавляем плеер с id -- {players} в конференцию {conference}"):
            url = f'https://{self.server_ip}/api/v1/players'
            if type(players) == int or type(players) == str:
                players = str(players).split()
            for player in players:
                response = requests.post(
                    url,
                    data=json.dumps({"conference": conference,
                                     "video": str(PlayersApi().get_id_player(player)),
                                     "loop": loop}),
                    headers=self.headers,
                    verify=False
                    )
            return response

    def add_participants(self, conference, account, **settings):
        """Метод добавляет в конференцию участника"""
        if type(account) == int or type(account) == str:
            account = str(account).split()
        for acc in account:
            participant = self.create_data({'number': acc}, settings)
            data = self.create_data({'conference': conference, 'participants': [participant]})
            return self.call_method('post', 'api/v1/participants', data)

    def fast_call(self, **data):  # H323
        """Метод выполняет быстрый вызов в конференцию"""
        return self.call_method('post', 'api/v1/fast_call', data)

    def remove_participant(self, conf, number):
        """Метод удаляет участника конференции по номеру участника"""
        return self.call_method('delete', f'api/v1/participant/{conf}/{number}', data=None)

    def call_in_conference(self, conf, users, delay=9, check_delay=6, check=False):
        """Метод вызывает участника в конференцию"""
        with allure.step(f"Вызываем {users} в конференцию {conf}"):
            url = f'https://{self.server_ip}/api/v1/call'
            if type(users) == int or type(users) == str:
                users = str(users).split()
            for i in range(0, 10):
                for user in users:
                    response = requests.post(
                        url,
                        data=json.dumps({"conference": int(conf),
                                         "participants": [str(user)]}),
                        headers=self.headers,
                        verify=False
                    )
                if check:
                    time.sleep(check_delay)
                    if len(users) == len(
                            self.get_participants_list(conf).json()["data"]["participants"]) - self.current_connections:
                        self.current_connections += len(users)
                        break
                else:
                    break
            time.sleep(delay)
            return response

    def disconnect_from_conference(self, conference, part, delay=0):
        """Метод отключает участника от конференции, на вход номер конференции и номер участника или ролика"""
        if type(part) == int or type(part) == str:
            part = str(part).split()
        url = f'https://{self.server_ip}/api/v1/disconnect'
        response = requests.post(
            url,
            data=json.dumps({"conference": conference,
                            "participants": part}),
            headers=self.headers,
            verify=False
        )
        self.current_connections -= 1
        time.sleep(delay)
        return response

    def start_recording(self, conference):
        """Метод начинает запись конференции"""
        return self.call_method('post', 'api/v1/start_recording', data={'conference': conference})

    def stop_recording(self, conference):
        """Метод останавливает запись конференции на сервере по ее номеру"""
        return self.call_method('post', 'api/v1/stop_recording', data={'conference': conference})

    def enable_lecturer_mode(self, conference):
        """Метод включат режим лектора в конференции (лектор на весь экран)"""
        return self.call_method('post', 'api/v1/enable_lecturer_mode', data={'conference': conference})

    def disable_lecturer_mode(self, **data):
        """Метод включат режим лектора в конференции (лектор на весь экран)"""
        return self.call_method('post', 'api/v1/disable_lecturer_mode', data)

    def enable_webcast(self, conference):
        """Метод включает трансляцию конференции, нужен для получения скриншотов"""
        self.call_method('patch', f'api/v1/webcast/{conference}', data={'resolution': 'FULLHD', 'hls': True})
        return self.call_method('post', 'api/v1/enable_webcast', data={'conference': conference})

    def disable_webcast(self, conference):
        """Метод отключения трансляции конференции"""
        return self.call_method('post', 'api/v1/disable_webcast', data={'conference': conference})

    def change_mosaic(self, **data):
        """Смена мозаики конференции список мозаик смотреть в readme проекта"""
        return self.call_method('post', 'api/v1/mosaic', data)

    def get_layout_position(self, conference):
        """Получение словаря с {'position': позиция в мозаике, 'nowScreen': сейчас на экране,
        'mosaic': текущая мозаика}"""
        url = f'https://{self.server_ip}/api/v1/layout/{conference}'
        response = requests.get(
            url,
            headers=self.headers,
            verify=False
        )
        try:
            positions = response.json()['data']['layout']['positions']
            now_screen = response.json()['data']['layout']['nowOnScreen']['positions']
            mosaic = response.json()['data']['layout']['mosaic']
            return {'position': positions, 'nowScreen': now_screen, 'mosaic': mosaic}
        except KeyError:
            return response.status_code

    def get_screen(self, conference, test_name, test_number=''):
        """Получение скриншота конференции через превью трансляции"""
        url = f'https://{self.server_ip}/api/v1/stream/preview/{conference}'
        response = requests.get(
            url,
            headers=self.headers,
            verify=False
        )
        # записываем полученный скриншот в файл по указанному пути
        current_way = os.path.join(os.getcwd())
        current_way = os.path.join(f"{current_way}/screenshots/{test_name}/current/")
        try:
            os.makedirs(current_way)
        except FileExistsError:
            print("Папка уже создана")
        finally:
            way = os.path.abspath(os.path.join(current_way, f'{test_name}{test_number}.png'))
            out = open(way, "wb")
            out.write(response.content)
            out.close()
            return response.status_code

    def change_position_on_layout(self, conference, positions, mosaic=None, delay=0):
        """Метод изменяет позиции абонентов на раскладке, на вход принимает словарь {Номер позиции(int): участник}"""
        with allure.step(f"Меняем позиции в раскладке на {positions}, мозаику на {mosaic}"):
            if mosaic is None:
                mosaic = self.get_layout_position(conference)['mosaic']
            prepare_array = self.get_layout_position(conference)['position']
            url = f'https://{self.server_ip}/api/v1/layout/{conference}'
            for pos, value in positions.items():
                prepare_array[pos - 1] = value
            response = requests.post(
                url,
                data=json.dumps({"mosaic": str(mosaic),
                                 "positions": prepare_array}),
                headers=self.headers,
                verify=False
            )
            time.sleep(delay)
            return response.status_code

    def change_all_position_auto(self, conference, mosaic=None):
        """Назначение на все позиции мозаики Авто"""
        with allure.step(f"Устанавливаем все позиции общей раскладки в auto"):
            if mosaic is None:
                mosaic = self.get_layout_position(conference)['mosaic']
            url = f'https://{self.server_ip}/api/v1/layout/{conference}'
            all_auto_array = []
            for _ in range(0, 100):
                all_auto_array.append('')
            response = requests.post(
                url,
                data=json.dumps({"mosaic": str(mosaic),
                                 "positions": all_auto_array}),
                headers=self.headers,
                verify=False
            )
            return response.status_code

    def send_message_in_conference(self, **data):
        """Отправляем сообщение в конференцию"""
        return self.call_method('post', 'api/v1/message', data)

    def get_settings_conference(self, conference):
        """Получение настроек конференции"""
        return self.call_method('get', f'api/v1/conference/{conference}', data=None)

    def move_participants(self, conf, participant, to_conf):
        """Перемещение участника из конференции в конференцию"""
        return self.call_method('post', 'api/v1/move', data={'conference': conf,
                                                             'participant': [
                                                                 {'from': to_conf,
                                                                  'participants': participant}
                                                             ]})

    def get_participants_in_conf(self, conf, filters='online'):
        """Метод возвращает количество участников из конференции total-все, online(по-умолчанию) - онлайн участники"""
        val = self.get_conferences_list().json()
        for i in val:
            try:
                if i['number'] == conf:
                    return i['participants'][filters]
            except KeyError:
                continue
        return None

    def get_webcast_settings(self, conf, **data):
        return self.call_method('get', f'api/v1/webcast/{conf}', data)
    def get_audio_channel_settings_conference(self, conference):
        """Получение настроек аудио каналов конференции"""
        return self.call_method('get', f'api/v2/conference/{conference}/audioChannels', data=None)

    def save_audio_channel_settings_conference(self, conference, **data):
        """Сохранение настроек аудио каналов конференции"""
        return self.call_method('patch', f'api/v2/conference/{conference}/audioChannels', data)

