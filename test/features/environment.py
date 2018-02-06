import yaml

global config_data
config_data = yaml.load(
    open('test/configurations/config.yml'))


def before_all(context):
    """This method executes actions before regression"""
    print("******* BEFORE ALL *******")
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
    context.params = None
    context.credentials = None
    context.item_id = None

    context.__exchange_server = config_data['__exchange_server']
    context.__hostname = config_data['__hostname']
    context.__name_server = config_data['__name_server']
    context.__type_server = config_data['__type_server']
    context.__version_server = config_data['__version_server']
