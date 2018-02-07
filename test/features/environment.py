import yaml
import logging
from api_core.api_request.api_request_manager import get_delete_request, delete_request, request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

global config_data
config_data = yaml.load(
    open('test/configurations/config.yml'))

global config_data_accounts
config_data_accounts = yaml.load(open('test/configurations/accounts.yml'))


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
    context.item_ids = {}

    context.environment_variables = {}
    context.environment_variables['__EXCHANGE_SERVER'] = config_data['__EXCHANGE_SERVER']
    context.environment_variables['__HOSTNAME'] = config_data['__HOSTNAME']
    context.environment_variables['__NAME_SERVER'] = config_data['__NAME_SERVER']
    context.environment_variables['__TYPE_SERVER'] = config_data['__TYPE_SERVER']
    context.environment_variables['__VERSION_SERVER'] = config_data['__VERSION_SERVER']
    context.environment_variables['__DELETE_LOCK_TIME'] = config_data['__DELETE_LOCK_TIME']

    context.accounts = {}
    context.accounts['__USER_ADMINISTRATOR'] = config_data_accounts['__USER_ADMINISTRATOR']
    context.accounts['__CREDENTIALS_ADMINISTRATOR'] = config_data_accounts['__CREDENTIALS_ADMINISTRATOR']
    context.accounts['__USER_COMMON'] = config_data_accounts['__USER_COMMON']
    context.accounts['__CREDENTIALS_COMMON'] = config_data_accounts['__CREDENTIALS_COMMON']
    context.accounts['__USER_ROOM'] = config_data_accounts['__USER_ROOM']
    context.accounts['__CREDENTIALS_USER1'] = config_data_accounts['__CREDENTIALS_USER1']
    context.accounts['__USER1'] = config_data_accounts['__USER1']

    context.accounts['__USER_NAME1'] = config_data_accounts['__USER_NAME1']
    context.accounts['__USER_NAME2'] = config_data_accounts['__USER_NAME2']
    context.accounts['__COMMON_PASSWORD'] = config_data_accounts['__COMMON_PASSWORD']


def after_step(context, step):
    """This method executes actions after scenario"""
    logger.info("Starting After Step execution...")
    if 'I POST to /meetings' in step.name:
        context.after_endpoint = context.endpoint
        context.after_credentials = context.credentials


def after_scenario(context, scenario):
    """This method executes actions after scenario"""

    logger.info("Starting After Scenario execution...")

    if 'tag1' in scenario.tags:
        print("After Meeting _id:", context.after_item_id)
        print("After Credentials:", context.after_credentials)
        print("Endpoint:", context.after_endpoint)
        print("DELETE Meeting Response Status Code:",
              get_delete_request(context.base_url, context.after_endpoint, 'DELETE',
                                 context.after_credentials,
                                 context.after_item_id,
                                 None).status_code)

    # """This method delete a meeting by ID """
    if 'after_delete_meeting' in scenario.tags:
        get_delete_request(context.base_url, context.endpoint, context.after_method, context.credentials,
                           context.id_meeting, None)
        print("Was deleted meeting id:", context.id_meeting)

    if 'after_delete_service' in scenario.tags:
        print(request(context.base_url, context.endpoint, "DELETE", context.credentials,
                      context.item_id,
                      context.data, context.params).status_code)
