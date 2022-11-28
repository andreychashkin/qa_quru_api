from .AccountsApi import AccountsApi
from .AccountGroupApi import AccountGroupApi
from .AddressBookApi import AddressBookApi
from .ApiKeys import ApiKeysApi
from .ChatApi import ChatApi
from .ConferencesApi import ConferencesApi
from .GatewaysApi import GatewaysApi
from .MailApi import MailApi
from .OauthApi import OauthApi
from .ParticipantsApi import ParticipantsApi
from .PlayersApi import PlayersApi
from .TenantApi import TenantApi
from .UsersApi import UserApi
from .WebhooksApi import WebhooksApi


class Api(AccountGroupApi,
          AccountsApi,
          AddressBookApi,
          ApiKeysApi,
          ChatApi,
          ConferencesApi,
          GatewaysApi,
          MailApi,
          OauthApi,
          ParticipantsApi,
          PlayersApi,
          TenantApi,
          UserApi,
          WebhooksApi):
    pass
