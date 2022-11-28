import requests
from bs4 import BeautifulSoup as b
from pyzabbix.api import ZabbixAPI


data = {"name": "maykop",
        "password": "vinteo",
        'autologin': '1',
        'enter': 'Sign in'}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                 ' Chrome/106.0.0.0 Safari/537.36'
ZABBIXURL = 'http://10.1.0.112'
ZABBIXAPIUSER = 'maykop'
ZABBIXAPIPASSWORD = 'vinteo'


def get_stats_zabbix(server_ip="10.1.0.11", free_memory=False, cpu_system=False, cpu_user=False, load_cpu=False):
    """Функция возвращает значение одной из переменных: Свободная память ОЗУ, CPU system time, CPU user time,
    загрузка CPU, данные берутся с zabbix 10.1.0.112, по-умолчанию мониторится 10.1.0.11 сервер"""
    zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)
    result = zapi.host.get(monitored_hosts=1, output='extend')
    hostnames = [host['host'] for host in result]
    hostid = [host['hostid'] for host in result]
    server_id = dict(zip(hostnames, hostid))
    url = f'http://10.1.0.112/zabbix.php?action=latest.view.refresh&filter_hostids[0]={server_id[server_ip]}&filter_application=&filter_select=&sort=host&sortorder=ASC'

    session = requests.Session()
    session.post('http://10.1.0.112/index.php', data=data, headers={
        'user-Agent': user_agent})
    stats = session.get(url)

    soup = b(stats.text, 'html.parser')
    headers = []
    if free_memory:
        for i in soup.find_all('tr')[18].find('div').find('span').find('td'):
            title = i.text
            headers.append(title)
        print(headers[1][0:5])
        return float(headers[1][0:5])
    elif cpu_system:
        for i in soup.find_all('tr')[8].find('div').find('span').find('td'):
            title = i.text
            headers.append(title)
        print(headers[1][0:7])
        return float(headers[1][0:7])
    elif cpu_user:
        for i in soup.find_all('tr')[9].find('div').find('span').find('td'):
            title = i.text
            headers.append(title)
        print(headers[1][0:7])
        return float(headers[1][0:7])


# def test_stat():
#     mem = get_stats_zabbix(free_memory=True)
#     assert float(mem) > 12
#
#
# def main():
#     get_stats_zabbix(free_memory=True)
#
#
# if __name__ == '__main__':
#     main()
