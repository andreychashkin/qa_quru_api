import os

version = {'chrome': '100.0', 'firefox': '98.0'}

if os.environ.get('SERVER_IP') is None:
    ip_server = 'demo.vinteo.com'
else:
    ip_server = os.environ.get('SERVER_IP')
if os.environ.get('LOGIN') is None:
    login = 'admin'
else:
    login = os.environ.get('LOGIN')
if os.environ.get('PASSWORD') is None:
    password = '654321'
else:
    password = os.environ.get('PASSWORD')
if os.environ.get('SECOND_IP') is None:
    second_ip = '10.23.9.55'
else:
    second_ip = os.environ.get('SECOND_IP')

# -----------------

if os.environ.get('CALL_IP') is None:
    call_ip = '10.23.9.59:4567'
else:
    call_ip = os.environ.get('CALL_IP')
if os.environ.get('IP_CALL_NUMBER') is None:
    ip_call_number = '10.23.9.59'
else:
    ip_call_number = os.environ.get('IP_CALL_NUMBER')

# ----------------

if os.environ.get('BROWSER') == 'chrome':
    selene_browser = 'chrome'
    selene_browser_version = '100.0'
elif os.environ.get('BROWSER') == 'firefox':
    selene_browser = 'firefox'
    selene_browser_version = '98.0'
else:
    selene_browser = 'chrome'
    selene_browser_version = '100.0'

# ---------------

if os.environ.get('SELENOID_LOGIN') is None:
    selenoid_login = 'user1'
else:
    selenoid_login = os.environ.get('SELENOID_LOGIN')
if os.environ.get('SELENOID_PASSWORD') is None:
    selenoid_password = '1234'
else:
    selenoid_password = os.environ.get('SELENOID_PASSWORD')
