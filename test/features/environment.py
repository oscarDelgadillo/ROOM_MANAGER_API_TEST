import yaml
import logging
from api_core.api_request.api_request_manager import get_delete_request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

global config_data
config_data = yaml.load(
    open('test/configurations/config.yml'))

global config_data_accounts
config_data_accounts = yaml.load(open('test/configurations/accounts.yml'))

global config_data_services
config_data_services = yaml.load(open('test/configurations/services.yml'))


def before_all(context):
    """This method executes actions before regression"""

    logger.info("Starting Before All execution...")
    logger.info("Setting up initial configurations...")
    context.rm_host = config_data['rm_host']
    context.rm_port = config_data['rm_port']
    context.rm_db_port = config_data['rm_db_port']
    context.root_path = config_data['root_path']
    context.version = config_data['version']
    context.protocol = config_data['protocol']
    context.database = config_data['data_base_rm']

    context.base_url = '{}://{}{}{}{}{}'.format(context.protocol, context.rm_host, ':', context.rm_port,
                                                context.root_path,
                                                context.version)

    logger.info("Setting up initial common values")
    context.params = None
    context.credentials = None
    context.item_id = None
    context.return_data = None
    context.data = None

    context.after_item_id = None
    context.after_credentials = None
    context.after_endpoint = None
    context.after_method = None

    context.accounts = {}
    context.accounts['__USER_ADMINISTRATOR'] = config_data_accounts['__USER_ADMINISTRATOR']
    context.accounts['__CREDENTIALS_ADMINISTRATOR'] = config_data_accounts['__CREDENTIALS_ADMINISTRATOR']
    context.accounts['__USER_COMMON'] = config_data_accounts['__USER_COMMON']
    context.accounts['__CREDENTIALS_COMMON'] = config_data_accounts['__CREDENTIALS_COMMON']
    context.accounts['__USER_ROOM'] = config_data_accounts['__USER_ROOM']

    context.services = {}
    context.services['__TYPE_SERVER'] = config_data_services['__TYPE_SERVER']
    context.services['__HOSTNAME'] = config_data_services['__HOSTNAME']
    context.services['__USER_ADMINISTRATOR'] = config_data_services['__USER_ADMINISTRATOR']
    context.services['__PASSWORD_ADMINISTRATOR'] = config_data_services['__PASSWORD_ADMINISTRATOR']
    context.services['__DELETE_LOCK_TIME'] = config_data_services['__DELETE_LOCK_TIME']

    context.__exchange_server = config_data['__exchange_server']
    context.__hostname = config_data['__hostname']
    context.__name_server = config_data['__name_server']
    context.__type_server = config_data['__type_server']
    context.__version_server = config_data['__version_server']

    # context.__user_administrator = config_data['__user_administrator']
    # context.__password_administrator = config_data['__password_administrator']
    # context.__deleteLockTime = config_data['__deleteLockTime']

# def after_scenario(context, scenario):
#     """This method executes actions after scenario"""
#
#     logger.info("Starting After Scenario execution...")
#     if 'Verify that is possible to retrieve free rooms' or 'Verify that is possible to retrieve busy rooms' in scenario.name:
#         print("After Meeting _id:", context.after_item_id)
#         print("After Credentials:", context.after_credentials)
#         print("Endpoint:", context.after_endpoint)
#         # print("DELETE Meeting Response Status Code:",
#         #       # get_delete_request(context.base_url, context.after_endpoint, 'DELETE', context.after_credentials,
#         #       #                    context.after_item_id,
#         #       #                    None).status_code)


def after_scenario(context, scenario):
    """This method delete a meeting by ID """
    if 'after_delete_meeting' in scenario.tags:
        get_delete_request(context.base_url, context.endpoint, context.after_method, context.credentials,
                           context.id_meeting, None)
        print("Was deleted meeting id:", context.id_meeting)

    if 'remove_service_after' in scenario.tags:
        get_delete_request(context.base_url, context.endpoint, 'DELETE', None, context.id_service, None)
