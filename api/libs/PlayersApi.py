from .BaseApi import BaseApi

import requests


class PlayersApi(BaseApi):

    def get_players_list(self):
        """Метод возвращается массив роликов загруженных на сервер"""
        url = f"https://{self.server_ip}/api/v1/players"
        response = requests.get(
            url,
            headers=self.headers,
            verify=False
        )
        try:
            return response.json()['data']['video']
        except KeyError:
            return response

    @staticmethod
    def get_id_player(title: str):
        """Метод возвращает id ролика по его title"""
        players_list = PlayersApi().get_players_list()
        if len(players_list) == 0:
            return
        else:
            for i in players_list:
                if title in i['title']:
                    return i['id']
        return
