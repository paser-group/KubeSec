import yaml_parser
import os
import constant
import pandas as pd

#source = "/Users/shamim/Downloads/K8s_inspection/GITHUB_REPOS"
#source = "/Users/shamim/Downloads/k8s_data/"
source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/" #justin@kubernetes/"
subdirs = os.listdir(source)


def check_rbac(yaml_file):
    values = yaml_parser.get_key_values(yaml_file, constant.return_value)
    if constant.rbac_api_version in values:
        return True
    elif constant.rbac_object_role in values:
        return True
    elif constant.rbac_cluster_role_binding in values:
        return True
    elif constant.rbac_object_cluster_role in values:
        return True
    elif constant.rbac_role_binding in values:
        return True
    else:
        return False

def check_default_namespace(yaml_file):
    counts = 0
    try:
        if(type(yaml_file) is dict):
            name_space = yaml_file.get("metadata",{}).get("namespace")
            if(name_space == constant.namespace_value_default):
                counts=counts+1
            else:
                pass
    except KeyError:
        pass
    return counts

#https://kubernetes.io/docs/concepts/policy/pod-security-policy/

def check_root_privilege(yaml_file):
    count_privileged =0
    keys = yaml_parser.get_key_values(yaml_file, constant.return_key)
    if(constant.container_privilege_given in keys):
        values = list(yaml_parser.find_all_value_for_keys(yaml_file,constant.container_privilege_given))
        for value in values:
            print ("ROOT PRIVILEGE value type-->",type(value),"VALUE-->",value)
            if(type(value) is bool):
                #"IT IS OK-->"
                if(value is True):
                    count_privileged = count_privileged + 1
            elif(type(value is str)):
                if (value =='true'):
                    count_privileged = count_privileged + 1
    print("ROOT PRIVILEGE check-->", count_privileged)
    return count_privileged


def check_pod_policy(yaml_file):
    count_missing_security_context = 0
    count_container_privilege_escalation = 0
    count_no_container_privilege_escalation = 0
    #count_privileged_containers = 0

    kind = yaml_parser.find_value_for_keys(yaml_file, constant.kind)
    if (kind == constant.pod):
        keys = yaml_parser.get_key_values(yaml_file, constant.return_key)
        if (constant.pod_policy_security_context in keys):
            # absent_security_context = False
            # if (constant.pod_container in keys):
            print("Container exists!------->")
            if (constant.container_privilege_escalation in keys):
                values = list(yaml_parser.find_all_value_for_keys(yaml_file, constant.container_privilege_escalation))
                #print("es value-->", type(values), "VALUE-->", values)
                # print("\n\n", value, "\n\n")
                for value in values:
                    if (value):
                        count_container_privilege_escalation = count_container_privilege_escalation + 1
            else:
                count_no_container_privilege_escalation = count_no_container_privilege_escalation + 1
        else:
            count_missing_security_context = count_missing_security_context + 1

    return count_missing_security_context,count_container_privilege_escalation,count_no_container_privilege_escalation
#
def check_linux_capability_pod(yaml_file):
    pass

def check_network_policy(yaml_file):
    pass

def check_update_strategy(yaml_file):
    pass

def check_network_egress_policy():
    pass

def check_resource_limit(yaml_file):
    absent_flag = True
    kind = yaml_parser.find_value_for_keys(yaml_file,constant.kind)
    if(kind == constant.pod):
        keys = yaml_parser.get_key_values(yaml_file,constant.return_key)
        if(constant.pod_spec in keys and constant.pod_container in keys):
            if(constant.limit_resources in keys):
                if(constant.limit_resources in keys) and (constant.limit_requests in keys):
                    absent_flag = False
            #   else:
            #     return absent_flag
        else:
            return absent_flag
    #return absent_flag


def check_no_TLS(yaml_file):
    count =0
    #https://stackabuse.com/python-check-if-string-contains-substring/
    values = yaml_parser.get_key_values(yaml_file,constant.return_value)
    for value in values:
        value_string =str(value)
        if(value_string.find(constant.http_no_tls)!=-1):
            count = count + 1
    return count

def check_hardcoded_secrets(yaml_file):
    password_count = 0
    username_count = 0
    key_count = 0
    keys = yaml_parser.get_key_values(yaml_file,constant.return_key)
    for key in keys:
        if(key==constant.user_name or key == constant.user_only):
            value = yaml_parser.find_value_for_keys(yaml_file,constant.user_name)
            value =str(value)
            #print("-----USERNAME------")
            if(value):
                #print("-----USERNAME------")
                username_count = username_count + 1
        elif(key==constant.password):
            p_value = yaml_parser.find_value_for_keys(yaml_file,constant.password)
            p_value = str(p_value)
            if(p_value):
                #print("-----PASSWORD------")
                password_count = password_count +1
        elif(key==constant.password_key):
            k_value = yaml_parser.find_value_for_keys(yaml_file,constant.password_key)
            k_value = str(k_value)
            if(k_value):
                #print("-----KEY------")
                key_count = key_count + 1

    #print("USERNAME --->", username_count, "PASSWORD--->", password_count, "KEY---->", key_count)

    return username_count,password_count,key_count

def check_yaml_load(source):
    namespace_count = 0
    rbac_miss_count = 0
    no_TLS_count = 0
    no_limit_resource_count =0
    count = 0

    username_count = 0
    password_count = 0
    key_count =0
    missing_security_context_count = 0
    privileged_container_count = 0
    privilege_escalation_count = 0

    count_root_privilege = 0
    for dir in subdirs:
        print("\n\n========",dir,"--->",count,"===========\n\n")
#        print(dir)
        rbac_flag = False
        no_limit_resource =0
        u_count, p_count, k_count = 0, 0, 0
        source_dir = source + "/" + dir + "/"
        for (root, directory, files) in os.walk(source_dir, topdown=True):

            for name in files:
                file_path = root + "/" + name
                #print(name)
                if name.endswith((".yaml", ".yml")) and not name.endswith(("docker-compose.yml", "bootstrap.yml", "application,yml")):
                    #print (file_path)
                    y = yaml_parser.parse_yaml_file(file_path)

                    #### CHECK DEFAULT NAMESPACE
                    namespace = check_default_namespace(y)
                    namespace_count = namespace + namespace_count

                    #### CHECK RBAC EXISTENCE
                    rbac = check_rbac(y)
                    if(rbac is True):
                        rbac_flag = True

                    #### CHECK NO TLS
                    no_TLS = check_no_TLS(y)
                    no_TLS_count = no_TLS + no_TLS_count

                    #### CHECK RESOURCE LIMIT
                    no_limit = check_resource_limit(y)
                    if(no_limit is True):
                        no_limit_resource = no_limit_resource + 1

                    #### CHECK POD POLICY

                    count_msc, count_pe, count_upe = check_pod_policy(y)
                    print("PRIVILEGE ESCALATION-->",count_pe,"MISSING SECURITY CONTEXT-->",count_msc, "PREVILEGE ESCALATION UNDEFINED", count_upe)
                    privilege_escalation_count = privilege_escalation_count + count_pe
                    privileged_container_count = privileged_container_count + count_upe
                    missing_security_context_count = missing_security_context_count + count_msc

                    ### PRIVILEGE COUNT

                    count_root = check_root_privilege(y)
                    count_root_privilege = count_root + count_root_privilege
                    #print("ROOT PRIVILEGE -->", count_root)


                    #### NETWORK POLICY

                    #### Hard Coded Secrets

                    u_count, p_count, k_count = check_hardcoded_secrets(y)
                   # print("USERNAME --->", u_count, "PASSWORD--->", p_count, "KEY---->", k_count)

                    #### Update Hard coded count
                    username_count = username_count + u_count
                    password_count = password_count + p_count
                    key_count = key_count + k_count

        ##### UPDATE RESOURCE LIMIT COUNT
        no_limit_resource_count = no_limit_resource_count + no_limit_resource

        #print("USERNAME --->", username_count, "PASSWORD--->", password_count, "KEY---->", key_count)

        #print(y)
        count = count + 1

        if(rbac_flag is False):
            #print("\n Dirname-->",dir,"\n")
            rbac_miss_count = rbac_miss_count + 1
        if(rbac_flag is True):
            print("\n RBAC Dirname-->", dir, "\n")

        ##### WRITE IN A CSV FILE



    print(rbac_miss_count,"out of ",len(subdirs))
    print(namespace_count)
    print(" NO TLS -->", no_TLS_count)
    print(" NO LIMIT --->", no_limit_resource_count)
    print("USERNAME --->",username_count, "PASSWORD--->",password_count,"KEY---->",key_count)
    print("PRIVILEGE ESCALATION-->", privilege_escalation_count ,"MISSING SECURITY CONTEXT",missing_security_context_count, "PRIVILEGED CONTAINER-->", privileged_container_count)
    print("ROOT PRIVILEGE -->", count_root_privilege)


if __name__ == "__main__":
    check_yaml_load(source)
#     parse_yaml_file(source)
#source