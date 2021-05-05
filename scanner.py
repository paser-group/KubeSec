'''
Akond Rahman 
May 03, 2021 
Code to detect security anti-patterns 
'''
import parser 
import constants 


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
    
    return dict_secret 



if __name__ == '__main__':
    # test_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml'
    # scanSingleManifest(test_yaml) 
    another_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/sni/values.yaml'
    scanSingleManifest( another_yaml ) 