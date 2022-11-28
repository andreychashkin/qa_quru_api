from .BaseApi import BaseApi

import requests
import json
import allure
import time
import os


class ParticipantsApi(BaseApi):

    def enable_mic(self, conference, participants):
        """Метод включает микрофон участникам в конференции на вход или одиночный участник.ролик или массив"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/enable_mic', data={'conference': conference,
                                                                   'participants': [participants]})

    def disconnect_participant(self, conference, participants):
        """Метод отключает участника конференции"""
        return self.call_method('post', 'api/v1/disconnect', data={'conference': conference,
                                                                   'participants': [participants]})

    def disable_mic(self, conference, participants):
        """Метод отключает микрофон участникам в конференции на вход или одиночный участник.ролик или массив"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/disable_mic', data={'conference': conference,
                                                                    'participants': [participants]})

    def appoint_lecture(self, conference, participant):
        """Назначает лектором выбранного участника/ролик конференции"""
        return self.call_method('post', 'api/v1/appoint_lecturer', data={'conference': conference,
                                                                         'participant': participant})

    def disappoint_lecture(self, conference, participant):
        """Снимает роль лектора с выбранного участника/ролик конференции"""
        return self.call_method('post', 'api/v1/disappoint_lecturer', data={'conference': conference,
                                                                            'participant': participant})

    def show_participant_as_presentation(self, conference, participant):
        """Метод показывает выбранного участника как презентацию"""
        return self.call_method('post', 'api/v1/enable_pvp', data={'conference': conference,
                                                                   'participant': participant})

    def disable_show_participant_as_presentation(self, conference, participant):
        """Метод отключает выбранного участника как презентацию"""
        return self.call_method('post', 'api/v1/disable_pvp', data={'conference': conference,
                                                                    'participant': participant})

    def disable_video_participants(self, conference, participants):
        """Метод отключает видео идущее к участнику конференции"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/disable_video', data={'conference': conference,
                                                                      'participants': [participants]})

    def enable_video_participants(self, conference, participants):
        """Метод включает видео идущее к участнику конференции"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/enable_video', data={'conference': conference,
                                                                     'participants': [participants]})

    def enable_audio_participants(self, conference, participants):
        """Метод включает звука идущее к участнику конференции"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/enable_audio', data={'conference': conference,
                                                                     'participants': [participants]})

    def disable_audio_participants(self, conference, participants):
        """Метод включает звука идущее к участнику конференции"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/disable_audio', data={'conference': conference,
                                                                      'participants': [participants]})

    def disable_cam_participants(self, conference, participants):
        """Метод отключает камеру участнику"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/disable_camera', data={'conference': conference,
                                                                       'participants': participants})

    def enable_cam_participants(self, conference, participants):
        """Метод включает камеру участнику"""
        if type(participants) == int or type(participants) == str:
            participants = str(participants).split()
        return self.call_method('post', 'api/v1/enable_camera', data={'conference': conference,
                                                                      'participants': participants})

    def get_personal_screen(self, conference, user, test_name, test_number=''):
        """Получение скриншота персональной раскладки"""
        url = f'https://{self.server_ip}/api/v1/take_screenshot/{conference}/{str(user)}/out'
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
            # print(response.json())
        return response

    def get_personal_layout_position(self, conference, participant):
        """Получение словаря с {'position': позиция в мозаике, 'nowScreen': сейчас на экране,
        'mosaic': текущая мозаика, 'nowMosaic': мозаика на экране} на персональной мозаике абонента"""
        url = f'https://{self.server_ip}/api/v1/layout/{conference}/{participant}'
        response = requests.get(
            url,
            headers=self.headers,
            verify=False
        )
        try:
            positions_in_conference = response.json()['data']['layout']['positions']
            positions_on_screen = (response.json()['data']['layout']['nowOnScreen'])['positions']
            current_mosaic = response.json()['data']['layout']['mosaic']
            on_screen_mosaic = (response.json()['data']['layout']['nowOnScreen'])['mosaic']
            with allure.step(f'Запрашиваем расположение участников на персональной раскладке абонента {participant}'):
                return {'position': positions_in_conference, 'nowScreen': positions_on_screen,
                        'mosaic': current_mosaic, 'nowMosaic': on_screen_mosaic}
        except KeyError:
            return response

    def change_personal_position_on_layout_auto(self, conference, participant, mosaic=1, yourself=False):
        """Меняем все позиции персональной раскладки на Авто"""
        with allure.step(f"Меняем все позиции на раскладке абонента {participant} на авто"):
            if mosaic is None:
                mosaic = self.get_personal_layout_position(conference, participant)['mosaic']
            prepare_array = []
            url = f'https://{self.server_ip}/api/v1/layout/{conference}/{participant}'
            for _ in range(0, 100):
                prepare_array.append('')
            response = requests.post(
                url,
                data=json.dumps({'mosaic': str(mosaic),
                                 'positions': prepare_array,
                                 'dontShowYourself': yourself}),
                headers=self.headers,
                verify=False)
            return response

    def change_personal_mosaic(self, conference, participant, mosaic=None, yourself=False):
        """Смена персональной раскладки абоненту на вход конференция, пользователь, мозаика"""
        with allure.step(f"Меняем персональную мозаику участнику {participant} на "
                         f"{mosaic}, не показывать себя - {yourself}"):
            prepare_array = self.get_personal_layout_position(conference, participant)['position']
            data = {'mosaic': str(mosaic), 'positions': prepare_array, 'dontShowYourself': yourself}
            if mosaic is None:
                data = {'positions': prepare_array, 'dontShowYourself': yourself}
            url = f'https://{self.server_ip}/api/v1/layout/{conference}/{participant}'
            response = requests.post(
                url,
                data=json.dumps(data),
                headers=self.headers,
                verify=False)
            time.sleep(2.5)
            return response

    def change_personal_position_on_layout(self, conference, participant, positions, mosaic=None, yourself=False):
        """Изменение позиции на персональной раскладке абонента"""
        with allure.step(f"Меняем расположение участников на раскладке абонента {participant} на {positions}"):
            if mosaic is None:
                mosaic = self.get_personal_layout_position(conference, participant)['mosaic']
            prepare_array = self.get_personal_layout_position(conference, participant)['position']
            url = f'https://{self.server_ip}/api/v1/layout/{conference}/{participant}'
            for pos, value in positions.items():
                prepare_array[pos - 1] = value
            response = requests.post(
                url,
                data=json.dumps({"mosaic": str(mosaic),
                                 "positions": prepare_array,
                                 "dontShowYourself": yourself}),
                headers=self.headers,
                verify=False)
            time.sleep(2)
            return response

    def show_participant_titer(self, **data):
        """Показать титр участника на вход конференция и номер участника"""
        return self.call_method('post', 'api/v1/show_titer', data)

    def get_in_screenshots_participants(self, test_name, users, delay=9):
        """Получаем маленькие скриншоты участников конференции"""
        with allure.step(f'получаем маленькие скриншоты участников {users}'):
            name_arr = ['', '_2']

            for j in range(len(name_arr)):
                for i in range(0, len(users)):
                    user = users[i][0]
                    url = users[i][1]
                    response = requests.get(
                        url,
                        headers=self.headers,
                        verify=False
                    )
                    current_way = os.path.join(os.getcwd())
                    current_way = os.path.join(f"{current_way}/screenshots/{test_name}/current/")
                    try:
                        os.makedirs(current_way)
                    except FileExistsError:
                        print("Папка уже создана")
                    finally:
                        way = os.path.abspath(
                            os.path.join(current_way, str(test_name) + str(name_arr[j]) + '.png'))
                        out = open(way, "wb")
                        out.write(response.content)
                        out.close()
                time.sleep(delay)
            return

    def update_watermark(self, conference, participant, watermark):
        """Изменение watermark участника конференции"""
        return self.call_method('patch', f'api/v1/watermark/{conference}/{participant}', data={'watermark': watermark})

    def get_audio_chanel(self, conference, participant, **params):
        """Получение настроек аудио канала участника конференции"""
        return self.call_method('get', f'api/v1/audio_channels/{conference}/{participant}', params)

    def change_audio_chanel(self, conference, participant, **data):
        """Изменение аудио канала участника конференции"""
        return self.call_method('patch', f'api/v1/audio_channels/{conference}/{participant}', data)

    def get_settings(self, conference, participant, **params):
        """Получение настроек участника конференции"""
        return self.call_method('get', f'api/v1/participant/{conference}/{participant}/settings', params)

    def change_settings(self, conference, participant, **data):
        """Изменение настроек участника конференции"""
        return self.call_method('patch', f'api/v1/participant/{conference}/{participant}/settings', data)

    def get_param(self, conference, participant):
        """Получение параметров участника конференции"""
        return self.call_method('get', f'api/v1/participant/{conference}/{participant}', data=None)

    def delete(self, conference, participant):
        """Удаление участника из конференции"""
        return self.call_method('delete', f'api/v1/participant/{conference}/{participant}', data=None)

    def simple_parser_for_link(self, arr):
        """Преобразовывает список контактов в массив словарей вида {номер абонента: ссылка на скриншот}"""
        link_in = []
        for i in range(1, len(arr), 2):
            pre_number = arr[i].get("number")
            pre_number = pre_number[pre_number.find('-') + 1:]
            prepare_link_in = [pre_number, f'https://{self.server_ip}{arr[i].get("shots")[0]}']
            link_in.append(prepare_link_in)
        return link_in

    def save_participants_audio_channel(self, conference, participant, **params):
        """Сохранение настроек аудио каналов участника конференции"""
        return self.call_method('get', f'api/v2/conference/{conference}/participant/{participant}', params)


