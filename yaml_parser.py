'''
Parse and Identify the violation of RBAC in the repository
'''

import yaml
import os

source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/justin@kubernetes/"

def parse_yaml_file (source_path):
    for (root, directory, files) in os.walk(source,topdown=True):
        for name in files:
            if name.endswith((".yaml", ".yml")) and not name.endswith(("docker-compose.yml","bootstrap.yml","application,yml")):
                #print(name)
                file_path = root + "/" +name
                #print(file_path)
                with open(file_path,"r") as file:
                    try:
                        yaml_file = list(yaml.safe_load_all(file))
#                       if(yaml_file['kind']=="RoleBinding"):
                        #print(yaml_file['kind'])
                        dictionary = {}
                        dictionary = yaml_file[0]
                        #print(dictionary)
                        name_space = dictionary.get('namespace')
                        if (name_space == "default"):
                            print("\nInstance found\n")
                            #print(dictionary)
                    except yaml.YAMLError as exc:
                        print(exc)



if __name__ == "__main__":
    parse_yaml_file(source)