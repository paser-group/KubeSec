'''
Akond Rahman 
May 03, 2021 
Code to detect security anti-patterns 
'''
import parser 
import constants 
import graphtaint 


def isValidUserName(uName): 
    valid = True
    if( any(z_ in uName for z_ in constants.FORBIDDEN_USER_NAMES ) ): 
        valid = False   
    return valid

def isValidPasswordName(pName): 
    valid = True
    if( any(z_ in pName for z_ in constants.FORBIDDEN_PASS_NAMES) ): 
        valid = False  
    return valid

def isValidKey(keyName): 
    valid = False 
    if( any(z_ in keyName for z_ in constants.LEGIT_KEY_NAMES ) ): 
        valid = True   
    return valid    

def checkIfValidSecret(single_config_val):
    flag2Ret = False 
    # print(type( single_config_val ), single_config_val  )
    if ( isinstance( single_config_val, str ) ):
        single_config_val = single_config_val.lower()
        config_val = single_config_val.strip() 
        if ( any(x_ in config_val for x_ in constants.INVALID_SECRET_CONFIG_VALUES ) ):
            flag2Ret = False 
        else:
            if(  len(config_val) > 2 )  :
                flag2Ret = True 
    else: 
        flag2Ret = False 
    return flag2Ret

def scanUserName(k_ , val_lis ):
    hard_coded_unames = []
    k_ = k_.lower()    
    # print('INSPECTING:', k_) 
    if( isValidUserName( k_ )   and any(x_ in k_ for x_ in constants.SECRET_USER_LIST )  ):
        # print( val_lis ) 
        for val_ in val_lis:
            if (checkIfValidSecret( val_ ) ): 
                # print(val_) 
                hard_coded_unames.append( val_ )
    return hard_coded_unames

def scanPasswords(k_ , val_lis ):
    hard_coded_pwds = []
    k_ = k_.lower()
    if( isValidPasswordName( k_ )   and any(x_ in k_ for x_ in constants.SECRET_PASSWORD_LIST )  ):
        for val_ in val_lis:
            if (checkIfValidSecret( val_ ) ): 
                hard_coded_pwds.append( val_ )
    return hard_coded_pwds


def checkIfValidKeyValue(single_config_val):
    flag2Ret = False 
    if ( isinstance( single_config_val, str ) ):
        if ( any(x_ in single_config_val for x_ in constants.VALID_KEY_STRING ) ):
            flag2Ret = True 
    return flag2Ret

def scanKeys(k_, val_lis):
    hard_coded_keys = []
    k_ = k_.lower()
    if( isValidKey( k_ )    ):
        for val_ in val_lis:
            if (checkIfValidKeyValue( val_ ) ): 
                hard_coded_keys.append( val_ )
    return hard_coded_keys    


def scanForSecrets(yaml_d): 
    key_lis, dic2ret_secret   = [], {} 
    parser.getKeyRecursively( yaml_d, key_lis )
    for key_data  in key_lis:
        key_     = key_data[0]
        value_list = [] 
        parser.getValsFromKey( yaml_d, key_ , value_list )
        unameList = scanUserName( key_, value_list  )
        # print(unameList)
        passwList = scanPasswords( key_, value_list  )
        keyList   = scanKeys( key_, value_list )
        # print(keyList)
        if( len(unameList) > 0  )  or ( len(passwList) > 0  ) or ( len(keyList) > 0  ) :
            dic2ret_secret[key_] =  ( unameList, passwList, keyList ) 
    return dic2ret_secret


def scanForOverPrivileges(script_path):
    key_count , privi_dict_return = 0, {} 
    kind_values = [] 
    checkVal = parser.checkIfValidK8SYaml( script_path )
    if(checkVal): 
        yaml_dict = parser.loadYAML( script_path )
        key_lis   = []
        parser.getKeyRecursively(yaml_dict, key_lis) 
        just_keys = [x_[0] for x_ in key_lis] 
        if ( constants.KIND_KEY_NAME in just_keys ):
            parser.getValsFromKey( yaml_dict, constants.KIND_KEY_NAME, kind_values )
        '''
        For the tiem being Kind:DeamonSet is not a legit sink because they do not directly provision deplyoments 
        '''
        if ( constants.PRIVI_KW in just_keys ) and ( constants.DEAMON_KW not in kind_values  ) :
            privilege_values = []
            parser.getValsFromKey( yaml_dict, constants.PRIVI_KW , privilege_values )
            # print(privilege_values) 
            for value_ in privilege_values:
                    if value_ == True: 
                        key_lis_holder = parser.keyMiner(yaml_dict, value_ ) 
                        if(constants.SPEC_KW in key_lis_holder) and (constants.CONTAINER_KW in key_lis_holder) and (constants.SECU_CONT_KW in key_lis_holder) and (constants.PRIVI_KW in key_lis_holder):
                            key_count += 1
                            privi_dict_return[key_count] = value_, key_lis_holder 
    return privi_dict_return 


def scanSingleManifest( path_to_script ):
    checkVal = parser.checkIfValidK8SYaml( path_to_script )
    # print(checkVal) 
    # initializing 
    dict_secret = {} 
    yaml_dict = parser.loadYAML( path_to_script )
    if(checkVal): 
        dict_secret = scanForSecrets( yaml_dict )
    elif ( parser.checkIfValidHelm( path_to_script )) :
        dict_secret = scanForSecrets( yaml_dict )
    
    '''
    taint tracking zone for secret dictionary 
    '''
    # print(dict_secret)
    within_secret_, templ_secret_, valid_taint_secr  = graphtaint.mineSecretGraph(path_to_script, yaml_dict, dict_secret) 
    # print(within_match_) 
    # print(templ_match_) 
    # print(valid_taints) 
    '''
    taint tracking for over privileges 
    '''
    valid_taint_privi  = scanForOverPrivileges( path_to_script )
    # print(valid_taint_privi) 

    return within_secret_, templ_secret_, valid_taint_secr, valid_taint_privi 


def scanForHTTP( path2script ):
    if parser.checkIfValidK8SYaml( path2script ):
        yaml_d   = parser.loadYAML( path2script )
        all_vals = parser.getValuesRecursively( yaml_d ) 
        for val_ in all_vals:
            if constants.HTTP_KW in val_:
                key_lis   = []
                parser.getKeyRecursively(yaml_d, key_lis) 
                just_keys = [x_[0] for x_ in key_lis] 
                if ( constants.SPEC_KW in just_keys ):
                    print(val_)
                    print(just_keys) 
                    print('Non ConfigMap Branch')               
                else: 
                    val_holder = [] 
                    parser.getValsFromKey(yaml_d, constants.KIND_KEY_NAME, val_holder)
                    if ( constants.CONFIGMAP_KW in val_holder ):
                        sh_files_configmaps = graphtaint.getTaintsFromConfigMaps( path2script  )
                        # print(val_)
                        # print(just_keys)  
                        print(sh_files_configmaps) 




if __name__ == '__main__':
    # test_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml'
    # scanSingleManifest(test_yaml) 
    # another_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/values.yaml'
    # another_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/minecraft/values.yaml'

    tp_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-glance-setup.yaml'
    tp_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-horizon-setup.yaml'
    scanForHTTP( tp_yaml )