import yaml_parser
import os
import constant

source = "/Users/shamim/Downloads/K8s_inspection/GITHUB_REPOS/" #justin@kubernetes/"

#source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/"
subdirs = os.listdir(source)


def check_rbac(yaml_file):
    values = yaml_parser.get_key_values(yaml_file, constant.return_value)
    if constant.rbac_object_role in values:
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

def check_pod_policy(yaml_file):
    pass

def check_network_policy(yaml_file):
    pass

def check_no_TLS(yaml_file):
    count =0
    #https://stackabuse.com/python-check-if-string-contains-substring/
    values = yaml_parser.get_key_values(yaml_file,constant.return_value)
    for value in values:
        value_string =str(value)
        if(value_string.find(constant.http_no_tls)!=-1):
            count = count + 1
    return count

def check_yaml_load(source):
    namespace_count = 0
    rbac_miss_count = 0
    no_TLS_count = 0
    for dir in subdirs:
        print(dir)
        rbac_flag = False
        source_dir = source + "/" + dir + "/"
        for (root, directory, files) in os.walk(source_dir, topdown=True):
            for name in files:
                file_path = root + "/" + name
                #print(name)
                if name.endswith((".yaml", ".yml")) and not name.endswith(("docker-compose.yml", "bootstrap.yml", "application,yml")):
                    #print (file_path)
                    y = yaml_parser.parse_yaml_file(file_path)
                    namespace = check_default_namespace(y)
                    namespace_count = namespace + namespace_count
                    rbac = check_rbac(y)
                    if(rbac is True):
                        rbac_flag = True
                    no_TLS = check_no_TLS(y)
                    no_TLS_count = no_TLS + no_TLS_count
                    #print(y)

        if(rbac_flag is False):
            #print("\n Dirname-->",dir,"\n")
            rbac_miss_count = rbac_miss_count + 1
        if(rbac_flag is True):
            print("\n RBAC Dirname-->", dir, "\n")

    print(rbac_miss_count,"out of ",len(subdirs))
    print(namespace_count)
    print(" NO TLS -->",no_TLS_count)

if __name__ == "__main__":
    check_yaml_load(source)
#     parse_yaml_file(source)
#source