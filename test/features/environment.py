import yaml

global config_data
config_data = yaml.load(
    open('test/configurations/config.yml'))


def before_all(context):
    print("******* BEFORE ALL *******")
    context.rm_host = config_data['rm_host']
    context.rm_port = config_data['rm_port']
    context.rm_db_port = config_data['rm_db_port']
    context.root_path = config_data['root_path']
    context.version = config_data['version']

    context.base_url = 'http://{}{}{}{}{}'.format(context.rm_host, ':', context.rm_port, context.root_path,
                                                  context.version)
