'''
Parse and Identify the violation of RBAC in the repository
'''

import yaml
import os
import constant

source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/justin@kubernetes/"


def get_key_values(dictionary_or_list,key_or_value):
    if(type(dictionary_or_list) is dict):
        for key,values in dictionary_or_list.items():
            if((type(values) is dict) or (type(values) is list)):
                if(key_or_value is return_key):
                    yield key
                for value in get_key_values(values,key_or_value):
                    yield value
            else:
                if (key_or_value is return_key):
                    yield key
                if (key_or_value is return_value):
                    yield values

    elif(type(dictionary_or_list) is list):
        for item in dictionary_or_list:
            if((type(item) is list) or (type(item) is dict)):
                for value in get_key_values(item,key_or_value):
                    yield value


#source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/"
#subdirs = os.listdir(source)
#print(subdirs)

# def find_key(dictionary,keysearch="key"):
#     for key,value in dictionary.items():
#         if keysearch = "key":
#             return key



def parse_yaml_file(source):
    count = 0
    for (root, directory, files) in os.walk(source,topdown=True):
        for name in files:
            if name.endswith((".yaml", ".yml")) and not name.endswith(("docker-compose.yml","bootstrap.yml","application,yml")):
                #print(name)
                file_path = root + "/" +name
                #print(file_path)
                with open(file_path,"r") as file:
                    try:
                        generator = yaml.safe_load_all(file)
                        yaml_file = {}
                        yaml_file = generator.__next__()
                        print(yaml_file)
                        print("------"*10)
                        print("\n"*3)
                        v = get_key_values(yaml_file, constant.return_value)
                        for value in v:
                            print(value)
                        print("\n" * 3)
                        print("------"*10)

                    except yaml.YAMLError as exc:
                        print(exc)


    #return yaml_file


def parse(source):
    count = 0
    for (root, directory, files) in os.walk(source, topdown=True):
        for name in files:
            if name.endswith((".yaml", ".yml")) and not name.endswith(
                    ("docker-compose.yml", "bootstrap.yml", "application,yml")):
                # print(name)
                file_path = root + "/" + name
                # print(file_path)
                with open(file_path, "r") as file:
                    try:
                        generator = yaml.safe_load_all(file)
                        yaml_file = {}
                        yaml_file = generator.__next__()

                    except yaml.YAMLError as exc:
                        print(exc)

    return yaml_file

if __name__ == "__main__":
    parse_yaml_file(source)
        #print("Instance Found {}",count)