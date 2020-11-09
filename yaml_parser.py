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
source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/" #OpenStack-on-Kubernetes" #justin@kubernetes/"

#source = "/Users/shamim/Downloads/k8s_data/"

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
                return value
            elif(type(yaml) is dict):
                for key,value in yaml.items():
                    if(type(value) is dict):
                         return find_value_for_keys(value,key_)

 def find_all_value_for_keys(yaml,key_):
    if (type(yaml) is dict):
        for key, value in yaml.items():
            if key_ == key:
                 print("match found")
                 yield value
            else:
                 for values in find_all_value_for_keys(value,key_):
                     yield values
    elif(type(yaml) is list):
        for item in yaml:
            for values in find_all_value_for_keys(item,key_):
                yield values



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


def check_root_privilege(yaml_file):
    count_privileged =0
    keys = yaml_parser.get_key_values(yaml_file, constant.return_key)
    if(constant.container_privilege_given in keys):
        values = yaml_parser.find_value_for_keys(yaml_file,constant.container_privilege_given)
        print("WHAT HAPPENED--->",values)

        if(values):
            count_privileged = count_privileged + 1
    print("ROOT PRIVILEGE -->", count_privileged)
    return count_privileged

def parse_yaml_file_test(source):
    # count_pod = 0
    # count_namespace = 0
    # count_namespace_instance = 0
    count_privileged =0
    count_container_privilege_escalation = 0
    count_no_container_privilege_escalation = 0
    count_privileged_containers = 0


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
                # ----------NameSpace -------------#
                #value = find_value_for_keys(yaml_file,constant.kind)
                #namespace = find_value_for_keys(yaml_file,constant.namespace_key)

                # print(file_path)
                # print(name)
                # if(value is not None):
                #     print(value)
                #     if value==constant.pod:
                #         count_pod = count_pod + 1
                # #CHECK namespace with dictionary
                # if(namespace is not None):
                #     count_namespace_instance = count_namespace_instance +1
                #     print(namespace)
                #     if (type(namespace) is list):
                #         for item in namespace:
                #             if (item == constant.namespace_value_default):
                #                 count_namespace = count_namespace + 1
                #     else:
                #         if (namespace == constant.namespace_value_default):
                #             count_namespace = count_namespace + 1
                #-----------------------------------------------#

#---------------------ROOT PRIVILEGE ----------------#
                # keys = get_key_values(yaml_file, constant.return_key)
                # if (constant.container_privilege_given in keys):
                #     #values = str()
                #     print(file_path)
                #     print(yaml_file)
                #     a = list(find_all_value_for_keys(yaml_file,constant.container_privilege_given))
                #     print("\n-------",a,"-----------\n")
                #     #print("WHAT --->", type(check_boolean_for_keys(yaml_file, constant.container_privilege_given)))
                #     for instance in a:
                #         print (instance)
                #         if (instance):
                #             count_privileged = count_privileged + 1
                # #print("ROOT PRIVILEGE -->", count_privileged)
                # #return count_privileged

#---------------------POD POLICY ----------------------#
                #     keys = get_key_values(yaml_file, constant.return_key)
                # #if (constant.pod_spec in keys):
                #     print(yaml_file)
                #     if (constant.pod_policy_security_context in keys):
                #         #absent_security_context = False
                #         #if (constant.pod_container in keys):
                #         print("Container exists!------->")
                #         if (constant.container_privilege_escalation in keys):
                #             values = list(find_all_value_for_keys(yaml_file,constant.container_privilege_escalation))
                #             print("es value escalationnnnn-->", type(values), "VALUE-->", values)
                #                 # print("\n\n", value, "\n\n")
                #             for value in values:
                #                 if (value):
                #                     count_container_privilege_escalation = count_container_privilege_escalation + 1
                #         else:
                #             count_no_container_privilege_escalation = count_no_container_privilege_escalation + 1
                #     else:
                #         count_privileged_containers = count_privileged_containers + 1

                    # elif(constant.container_privilege_given in keys):
                    #     value_privileged_containers = list(find_all_value_for_keys(yaml_file,constant.container_privilege_given))
                    #         # print("\n\n",value_privileged_containers,"\n\n")
                    #     print("ROOT privilegedddd-->", type(value_privileged_containers), "VALUE-->",
                    #               value_privileged_containers)
                    #
                    #     for value in value_privileged_containers:
                    #         if (value):
                    #              count_privileged_containers = count_container_privilege_escalation + 19092

    print("CPE-->", count_container_privilege_escalation,"CNPE-->",count_no_container_privilege_escalation,"CPC--->",count_privileged_containers)

    # print("POD----->",count_pod)
    # print("DEFAULT NAMESPACE ------>",count_namespace)
    # print("COUNT NAMESPACE ------>",count_namespace_instance)



# comment out when DONE
if __name__ == "__main__":

    # Test each functions working properly
    parse_yaml_file_test(source)