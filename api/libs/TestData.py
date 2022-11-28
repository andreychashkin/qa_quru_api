import os


if os.environ.get('SERVER_IP') is None:
    ip_server = ''
else:
    ip_server = os.environ.get('SERVER_IP')
if os.environ.get('LOGIN') is None:
    login = ''
else:
    login = os.environ.get('LOGIN')
if os.environ.get('PASSWORD') is None:
    password = ''
else:
    password = os.environ.get('PASSWORD')
if os.environ.get('SECOND_IP') is None:
    second_ip = '10.23.9.55'
else:
    second_ip = os.environ.get('SECOND_IP')


if os.environ.get('CALL_IP') is None:
    call_ip = '10.23.9.59:4567'
else:
    call_ip = os.environ.get('CALL_IP')
if os.environ.get('IP_CALL_NUMBER') is None:
    ip_call_number = '10.23.9.59'
else:
    ip_call_number = os.environ.get('IP_CALL_NUMBER')
