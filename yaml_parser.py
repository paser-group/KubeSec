'''
Parse and Identify the violation of RBAC in the repository
'''
from ruamel.yaml import YAML
from ruamel.yaml.scanner import ScannerError
import yaml
import os
import constant
counts = 0
#source = "/Users/shamim/Downloads/K8s_inspection/GITHUB_REPOS/"
source = "/Users/shamim/Downloads/k8s_data/"

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
        if yaml is not None:
            if key_ in yaml:
                value = yaml.get(key_)
                #if (type(value) is not None):
                return value
            elif(type(yaml) is dict):
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
    return yaml_file


def parse_yaml_file_test(source):
    count_pod = 0
    count_namespace = 0
    count_namespace_instance = 0

    for (root, directory, files) in os.walk(source,topdown=True):
        for name in files:
            if name.endswith((".yaml", ".yml")) and not name.endswith(("docker-compose.yml","bootstrap.yml","application.yml")):
                file_path = root + "/" +name
                #if(file_path=='/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/opendatahub-operator/roles/grafana/templates/grafana.yaml'):
                    #continue
                #print(file_path)
                #global counts
                yaml_file = {}
                with open(file_path,"r") as file:
                    try:
                        list_yaml =list(yaml.safe_load_all(file))
                        yaml_file = {}
                        if(len(list_yaml)>0):
                            yaml_file = list_yaml[0]
                    except yaml.YAMLError as exc:
                        print(exc)
                value = find_value_for_keys(yaml_file,constant.kind)
                namespace = find_value_for_keys(yaml_file,constant.namespace_key)
                #
                # print(file_path)
                # print(name)
                if(value is not None):
                    print(value)
                    if value==constant.pod:
                        count_pod = count_pod + 1
                #CHECK namespace with dictionary
                if(namespace is not None):
                    count_namespace_instance = count_namespace_instance +1
                    print(namespace)
                    if (type(namespace) is list):
                        for item in namespace:
                            if (item == constant.namespace_value_default):
                                count_namespace = count_namespace + 1
                    else:
                        if (namespace == constant.namespace_value_default):
                            count_namespace = count_namespace + 1



    print("POD----->",count_pod)
    print("DEFAULT NAMESPACE ------>",count_namespace)
    print("COUNT NAMESPACE ------>",count_namespace_instance)



# comment out when DONE
if __name__ == "__main__":

    # Test each functions working properly
    parse_yaml_file_test(source)