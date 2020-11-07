'''
Parse and Identify the violation of RBAC in the repository
'''
from ruamel.yaml import YAML
from ruamel.yaml.scanner import ScannerError
import yaml
import os
import constant
counts = 0
source = "/Users/shamim/Downloads/K8s_inspection/GITHUB_REPOS/" #justin@kubernetes/"

count =0

def get_key_values(dictionary_or_list,key_or_value):
    if(type(dictionary_or_list) is dict):
        for key,values in dictionary_or_list.items():
            if((type(values) is dict) or (type(values) is list)):
                if(key_or_value is constant.return_key):
                    yield key
                for value in get_key_values(values,key_or_value):
                    yield value
            else:
                if (key_or_value is constant.return_key):
                    yield key
                if (key_or_value is constant.return_value):
                    yield values

    elif(type(dictionary_or_list) is list):
        for item in dictionary_or_list:
            if((type(item) is list) or (type(item) is dict)):
                for value in get_key_values(item,key_or_value):
                    yield value

def find_value_for_keys(yaml,key_):
    #values = []
    if key_ in yaml:
        return yaml[key_]
    else:
        for key,value in yaml.items():
            if(type(value) is dict):
                return find_value_for_keys(value,key_)

def parse_yaml_file(file_path):
    yaml_file = {}
    with open(file_path,"r") as file:
        try:
            #yaml = YAML()
            list_yaml =list(yaml.safe_load_all(file))
            #generator = yaml.safe_load_all(file)
            yaml_file = {}
            if(len(list_yaml)>0):
                yaml_file = list_yaml[0]
        except yaml.YAMLError as exc:
            print(exc)
    #return yaml_file

# if __name__ == "__main__":
#     parse_yaml_file(source)