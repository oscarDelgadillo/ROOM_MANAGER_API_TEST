import yaml
import logging
from api_core.api_request.api_request_manager import get_delete_request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

global config_data
config_data = yaml.load(
    open('test/configurations/config.yml'))


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

    context.__exchange_server = config_data['__exchange_server']
    context.__hostname = config_data['__hostname']
    context.__name_server = config_data['__name_server']
    context.__type_server = config_data['__type_server']
    context.__version_server = config_data['__version_server']


def after_step(context, step):
    """This method executes actions after scenario"""

    logger.info("Starting After Step execution...")
    if 'I POST to /meetings' in step.name:
        context.after_endpoint = context.endpoint
        context.after_credentials = context.credentials


def after_scenario(context, scenario):
    """This method executes actions after scenario"""

    logger.info("Starting After Scenario execution...")

    if 'Verify that is possible to retrieve free rooms' or 'Verify that is possible to retrieve busy rooms' in scenario.name:
        print("After Meeting _id:", context.after_item_id)
        print("After Credentials:", context.after_credentials)
        print("Endpoint:", context.after_endpoint)
        print("DELETE Meeting Response Status Code:",
              get_delete_request(context.base_url, context.after_endpoint, 'DELETE', context.after_credentials,
                                 context.after_item_id,
                                 None).status_code)
