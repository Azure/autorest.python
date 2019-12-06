class CloudErrorPlugin:

    @staticmethod
    def remove_cloud_errors(yaml_data):
        for group in yaml_data['operationGroups']:
            for operation in group['operations']:
                if not operation.get('exceptions'):
                    continue
                i = 0
                while i < len(operation['exceptions']):
                    exception = operation['exceptions'][i]
                    if exception.get('schema') and exception['schema']['language']['default']['name'] == 'CloudError':
                        del operation['exceptions'][i]
                        i -= 1
                    i += 1
        if yaml_data.get('schemas') and yaml_data['schemas'].get('objects'):
            for i in range(len(yaml_data['schemas']['objects'])):
                obj_schema = yaml_data['schemas']['objects'][i]
                if obj_schema['language']['default']['name'] == 'CloudError':
                    del yaml_data['schemas']['objects'][i]
                    break
