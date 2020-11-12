import os
import ruleEngine
import constant
import yaml_parser
import pandas as pd


#source = "/Users/shamim/Downloads/K8s_inspection/GITHUB_REPOS"
#source = "/Users/shamim/Downloads/k8s_data/"
source = "/Users/shamim/Downloads/K8s_inspection/GITLAB_REPOS/" #justin@kubernetes/"
subdirs = os.listdir(source)

def aggregate_all_functions(source):
    csv_list_per_file = []
    csv_list_per_repo = []
    namespace_count,namespace_count_old = 0,0
    rbac_miss_count,rbac_miss_count_old = 0,0
    network_policy_miss_count,network_policy_miss_count_old = 0,0
    network_egress_policy_miss_count,network_egress_policy_miss_count_old = 0,0

    no_TLS_count,no_TLS_count_old = 0,0
    no_limit_resource_count,no_limit_resource_count_old =0,0
    count = 0

    username_count,username_count_old = 0,0
    password_count,password_count_old = 0,0
    key_count,key_count_old =0,0

    missing_security_context_count,missing_security_context_count_old= 0,0
    unspecified_privilege_escalation_count,unspecified_privileged_container_count_old = 0,0
    privilege_escalation_count,privilege_escalation_count_old = 0,0

    count_root_privilege,count_root_privilege_old = 0,0

    no_rolling_update_count,no_rolling_update_count_old = 0,0
    replica_count = 0

    for dir in subdirs:
        print("\n\n========",dir,"--->",count,"===========\n\n")
#        print(dir)
        # INCOSISTENCY MAKE IT CONSISTENT
        # Assume RBAC flag missing
        rbac_flag = False
        # Assume Network flag present
        network_flag = False
        # missing egress
        network_egress_flag = False
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
                    namespace = ruleEngine.check_default_namespace(y)
                    namespace_count = namespace + namespace_count

                    #### CHECK RBAC EXISTENCE
                    rbac = ruleEngine.check_rbac(y)
                    if(rbac is True):
                        rbac_flag = True

                    #### CHECK NO TLS
                    no_TLS = ruleEngine.check_no_TLS(y)
                    no_TLS_count = no_TLS + no_TLS_count

                    #### CHECK RESOURCE LIMIT
                    no_limit = ruleEngine.check_resource_limit(y)
                    if(no_limit is True):
                        no_limit_resource = no_limit_resource + 1

                    #### CHECK POD POLICY

                    count_msc, count_pe, count_upe = ruleEngine.check_pod_policy(y)
                    #print("MISSING SECURITY CONTEXT-->",count_msc,"PRIVILEGE ESCALATION-->",count_pe,"PREVILEGE ESCALATION UNDEFINED", count_upe)
                    privilege_escalation_count = privilege_escalation_count + count_pe
                    unspecified_privilege_escalation_count = unspecified_privilege_escalation_count + count_upe
                    missing_security_context_count = missing_security_context_count + count_msc

                    ### PRIVILEGE COUNT

                    count_root = ruleEngine.check_root_privilege(y)
                    count_root_privilege = count_root + count_root_privilege
                    #print("ROOT PRIVILEGE -->", count_root)

                    ##### Rolling Update

                    no_rolling_update, replica = ruleEngine.check_update_strategy(y)
                    no_rolling_update_count = no_rolling_update_count + no_rolling_update
                    replica_count = replica_count + replica

                    #### NETWORK POLICY

                    flag = ruleEngine.check_network_policy(y)
                    if(flag is True):
                        network_flag = True

                    #### NETWORK EGRESS POLICY
                    e_flag = ruleEngine.check_network_egress_policy(y)
                    if(e_flag is True):
                        network_egress_flag = True


                    #### Hard Coded Secrets

                    u_count, p_count, k_count = ruleEngine.check_hardcoded_secrets(y)
                    #print("USERNAME --->", u_count, "PASSWORD--->", p_count, "KEY---->", k_count)

                    #### Update Hard coded count
                    username_count = username_count + u_count
                    password_count = password_count + p_count
                    key_count = key_count + k_count

                    #### Write Results to CSV file
                    if(namespace+no_TLS+count_msc+count_upe+count_pe+count_root+no_rolling_update+u_count+p_count+k_count>0):
                        tuple_per_file = (dir, name, namespace,no_TLS,count_msc,count_pe,count_upe,count_root,no_rolling_update,u_count,p_count,k_count,True)
                    else:
                        tuple_per_file = (dir, name, namespace, no_TLS, count_msc, count_pe, count_upe, count_root, no_rolling_update,u_count, p_count, k_count,False)
                    csv_list_per_file.append(tuple_per_file)
                    data_frame_file = pd.DataFrame(csv_list_per_file)
                    data_frame_file.to_csv('/Users/shamim/Fall-20/CSC-6903/KubeSec/GITHUB_all_per_file.csv',header=['REPO NAME','FILE NAME','DEFAULT NAMESPACE','HTTP WITHOUT TLS', 'MISSING SECURITY CONTEXT','PRIVILEGE ESCALATION','USPECIFIED PRIVILEGE ESCALATION','ROOT PRIVILEGE','NO ROLLING UPDATE','USERNAME','PASSWORD','KEY','SECURE FLAG'],index=False, encoding='utf-8')



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

        if(network_flag is False):
            network_policy_miss_count = network_policy_miss_count + 1

        if(network_egress_flag is False):
            network_egress_policy_miss_count = network_egress_policy_miss_count + 1

        ##### WRITE IN A CSV FILE FOR EACH REPO

        tuple_per_repo = (dir, rbac_flag, network_flag, network_egress_flag, namespace_count - namespace_count_old,no_TLS_count - no_TLS_count_old,missing_security_context_count-missing_security_context_count_old,
                          privilege_escalation_count-privilege_escalation_count_old, unspecified_privilege_escalation_count-unspecified_privileged_container_count_old,
                          count_root_privilege - count_root_privilege_old, no_rolling_update_count- no_rolling_update_count_old,
                          username_count - username_count_old, password_count -password_count_old, key_count - key_count_old)

        namespace_count_old = namespace_count
        no_TLS_count_old = no_TLS_count
        missing_security_context_count_old = missing_security_context_count
        privilege_escalation_count_old = privilege_escalation_count
        unspecified_privileged_container_count_old = unspecified_privilege_escalation_count
        count_root_privilege_old = count_root_privilege
        no_rolling_update_count_old = no_rolling_update_count
        username_count_old = username_count
        password_count_old = password_count
        key_count_old = key_count

        csv_list_per_repo.append(tuple_per_repo)
        data_frame_repo = pd.DataFrame(csv_list_per_repo)
        data_frame_repo.to_csv('/Users/shamim/Fall-20/CSC-6903/KubeSec/GITLAB_all_per_repo.csv',
                               header=['REPO NAME','RBAC FLAG','NETWORK POLICY FLAG', 'NETWORK EGRESS FLAG', 'DEFAULT NAMESPACE', 'HTTP WITHOUT TLS', 'MISSING SECURITY CONTEXT',
                                                                                                         'PRIVILEGE ESCALATION', 'USPECIFIED PRIVILEGE ESCALATION',
                                  'ROOT PRIVILEGE', 'NO ROLLING UPDATE', 'USERNAME', 'PASSWORD', 'KEY'],index=False, encoding='utf-8')


    print("NO RBAC in ",rbac_miss_count,"repositories out of ",len(subdirs))
    print("DEFAULT NAMESPACE COUNT---> ",namespace_count)
    print("NO TLS -->", no_TLS_count)
    print("NO RESOURCE LIMIT --->", no_limit_resource_count)
    print("USERNAME --->",username_count, "PASSWORD--->",password_count,"KEY---->",key_count)
    print("PRIVILEGE ESCALATION-->", privilege_escalation_count ,"MISSING SECURITY CONTEXT",missing_security_context_count, "PRIVILEGED CONTAINER-->", unspecified_privilege_escalation_count)
    print("ROOT PRIVILEGE -->", count_root_privilege)
    print("NO ROLLING UPDATE -->", no_rolling_update_count, "out of ",replica_count,"instances")
    print("NETWORK POLICY MISSING in ", network_policy_miss_count, "repositories out of ", len(subdirs))
    print("NETWORK EGRESS POLICY MISSING in ", network_egress_policy_miss_count, "repositories out of ", len(subdirs))


if __name__ == "__main__":
    aggregate_all_functions(source)
#     parse_yaml_file(source)
#source
