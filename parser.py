'''
Akond Rahman 
April 30, 2021 
Parser to file YAML files
'''

import yaml
import constants 


def loadYAML( script_ ):
    dict2ret = {}
    with open(script_, constants.file_read_flag  ) as yml_content :
        try:
            dict2ret =   yaml.safe_load(yml_content) 
        except yaml.YAMLError as exc:
            print(exc)    
    return dict2ret 