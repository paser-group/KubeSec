'''
Akond Rahman 
May 03, 2021 
Code to detect security anti-patterns 
'''
import parser 
import constants 
import graphtaint 
import os 
import pandas as pd 
import numpy as np 

def getYAMLFiles(path_to_dir):
    valid_  = [] 
    for root_, dirs, files_ in os.walk( path_to_dir ):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if(os.path.exists(full_p_file)):
             if (full_p_file.endswith( constants.YML_EXTENSION  )  or full_p_file.endswith( constants.YAML_EXTENSION  )  ):
               valid_.append(full_p_file)
    return valid_ 

def isValidUserName(uName): 
    valid = True
    if (isinstance( uName , str)  ): 
        if( any(z_ in uName for z_ in constants.FORBIDDEN_USER_NAMES )   ): 
            valid = False   
        else: 
            valid = True    
    else: 
        valid = False   
    return valid

def isValidPasswordName(pName): 
    valid = True
    if (isinstance( pName , str)  ): 
        if( any(z_ in pName for z_ in constants.FORBIDDEN_PASS_NAMES) )  : 
            valid = False  
        else: 
            valid = True    
    else: 
        valid = False               
    return valid

def isValidKey(keyName): 
    valid = False 
    if ( isinstance( keyName, str )  ):
        if( any(z_ in keyName for z_ in constants.LEGIT_KEY_NAMES ) ) : 
            valid = True   
        else: 
            valid = False     
    else: 
        valid = False                      
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
    if isinstance(k_, str):
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
    if isinstance(k_, str):
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
    if isinstance(k_, str):
        k_ = k_.lower()    
    if( isValidKey( k_ )    ):
        for val_ in val_lis:
            if (checkIfValidKeyValue( val_ ) ): 
                hard_coded_keys.append( val_ )
    return hard_coded_keys    


def scanForSecrets(yaml_d): 
    key_lis, dic2ret_secret   = [], {} 
    parser.getKeyRecursively( yaml_d, key_lis )
    '''
    if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
    as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
    '''    
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
    # print(dic2ret_secret)
    return dic2ret_secret


def scanForOverPrivileges(script_path):
    key_count , privi_dict_return = 0, {} 
    kind_values = [] 
    checkVal = parser.checkIfValidK8SYaml( script_path )
    if(checkVal): 
        dict_as_list = parser.loadMultiYAML( script_path )
        yaml_dict    = parser.getSingleDict4MultiDocs( dict_as_list )
        # print(yaml_dict.keys())
        key_lis   = []
        parser.getKeyRecursively(yaml_dict, key_lis) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        just_keys = [x_[0] for x_ in key_lis] 
        # just_keys = list( np.unique( just_keys )  )
        if ( constants.KIND_KEY_NAME in just_keys ):
            parser.getValsFromKey( yaml_dict, constants.KIND_KEY_NAME, kind_values )
        '''
        For the time being Kind:DeamonSet is not a legit sink because they do not directly provision deplyoments 
        '''
        # print(just_keys) 
        if ( constants.PRIVI_KW in just_keys ) and ( constants.DEAMON_KW not in kind_values  ) :
            privilege_values = []
            parser.getValsFromKey( yaml_dict, constants.PRIVI_KW , privilege_values )
            # print(privilege_values) 
            for value_ in privilege_values:
                    if value_ == True: 
                        key_lis_holder = parser.keyMiner(yaml_dict, value_ ) 
                        # print( key_lis_holder )
                        if(constants.CONTAINER_KW in key_lis_holder) and (constants.SECU_CONT_KW in key_lis_holder) and (constants.PRIVI_KW in key_lis_holder):
                            key_count += 1
                            privi_dict_return[key_count] = value_, key_lis_holder 
    return privi_dict_return 

def getItemFromSecret( dict_sec, pos ): 
    dic2ret = {}
    cnt     = 0 
    for key_name , key_tup in dict_sec.items():
        secret_data_list = key_tup[pos]
        for data_ in secret_data_list: 
            dic2ret[cnt] = (key_name, data_)
            cnt          += 1
    return dic2ret


def scanSingleManifest( path_to_script ):
    '''
    While it is named as `scanSingleManifest` 
    it can only do taint tracking for secrets and over privileges 
    '''
    checkVal = parser.checkIfValidK8SYaml( path_to_script )
    # print(checkVal) 
    # initializing 
    within_secret_ = []
    dict_secret    = {} 
    dict_list      = parser.loadMultiYAML( path_to_script )
    yaml_dict      = parser.getSingleDict4MultiDocs( dict_list )
    if(checkVal):
        '''
        additional logic to handle secrets within a valid Kubernetes manifest 
        '''
        val_lis    = list( parser.getValuesRecursively  ( yaml_dict ) )
        if( constants.CONFIGMAP_KW in val_lis   ) or (constants.SECRET_KW in val_lis):  
            secret_key_list    = parser.keyMiner(yaml_dict, constants.SECRET_KW)  
            configmap_key_list = parser.keyMiner(yaml_dict, constants.CONFIGMAP_KW)  
            key_lis            = []
            if( isinstance(secret_key_list, list) ): 
                key_lis = key_lis + secret_key_list 
            if( isinstance(configmap_key_list, list) ): 
                key_lis = key_lis + configmap_key_list 
            if (len( key_lis ) > 0 ) :
                unique_keys = np.unique( key_lis )
                unique_keys = [x_ for x_ in unique_keys if constants.KIND_KEY_NAME in x_]
                if (len( unique_keys ) > 0 ):
                    dict_secret = scanForSecrets( yaml_dict )
                    within_secret_.append( getItemFromSecret( dict_secret, 0 )  ) # 0 for username 
                    within_secret_.append( getItemFromSecret( dict_secret, 1 )  ) # 1 for password 
                    within_secret_.append( getItemFromSecret( dict_secret, 2 )  ) # 2 for tokens  
                else: 
                    within_secret_.append({})
                    within_secret_.append({})
                    within_secret_.append({})                     
            else: 
                within_secret_.append({})
                within_secret_.append({})
                within_secret_.append({}) 
        else: 
            within_secret_.append({})
            within_secret_.append({})
            within_secret_.append({})            
    elif ( parser.checkIfValidHelm( path_to_script )) :
        dict_secret = scanForSecrets( yaml_dict )
        within_secret_.append({})
        within_secret_.append({})
        within_secret_.append({}) 
    else: 
        within_secret_.append({})
        within_secret_.append({})
        within_secret_.append({}) 
    
    '''
    taint tracking zone for secret dictionary 
    '''
    # print(dict_secret)
    _, templ_secret_, valid_taint_secr  = graphtaint.mineSecretGraph(path_to_script, yaml_dict, dict_secret) 
    # print(within_secret_) 
    # print(templ_secret_) 
    # print(valid_taint_secr) 
    '''
    taint tracking for over privileges 
    '''
    valid_taint_privi  = scanForOverPrivileges( path_to_script )
    # print(valid_taint_privi) 

    return within_secret_, templ_secret_, valid_taint_secr, valid_taint_privi 


def scanForHTTP( path2script ):
    sh_files_configmaps = {} 
    http_count = 0 
    if parser.checkIfValidK8SYaml( path2script ) or parser.checkIfValidHelm( path2script ):
        dict_as_list = parser.loadMultiYAML( path2script )
        yaml_d       = parser.getSingleDict4MultiDocs( dict_as_list )
        all_vals     = list (parser.getValuesRecursively( yaml_d )  )
        all_vals     = [x_ for x_ in all_vals if isinstance(x_, str) ] 
        for val_ in all_vals:
            # if (constants.HTTP_KW in val_ ) and ( (constants.WWW_KW in val_) and (constants.ORG_KW in val_) ):
            if (constants.HTTP_KW in val_ ) :
                key_lis   = []
                parser.getKeyRecursively(yaml_d, key_lis) 
                '''
                if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
                as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
                '''
                just_keys = [x_[0] for x_ in key_lis] 
                if ( constants.SPEC_KW in just_keys ):
                    '''
                    this branch is for HTTP values coming from Deplyoment manifests  
                    '''                    
                    http_count += 1 
                    sh_files_configmaps[http_count] =  val_ 
                elif( parser.checkIfValidHelm( path2script ) ):
                    '''
                    this branch is for HTTP values coming from Values.yaml in HELM charts  
                    '''
                    http_count += 1 
                    matching_keys = parser.keyMiner(yaml_d, val_)
                    key_ = matching_keys[-1]  
                    infected_list = graphtaint.mineViolationGraph(path2script, yaml_d, val_, key_) 
                    sh_files_configmaps[http_count] = infected_list
                else: 
                    '''
                    this branch is for HTTP values coming from ConfigMaps 
                    '''                    
                    val_holder = [] 
                    parser.getValsFromKey(yaml_d, constants.KIND_KEY_NAME, val_holder)
                    if ( constants.CONFIGMAP_KW in val_holder ):
                        http_count += 1 
                        infected_list = graphtaint.getTaintsFromConfigMaps( path2script  ) 
                        sh_files_configmaps[http_count] = infected_list
                        # print('ASI_MAMA:', sh_files_configmaps) 
                        # print( val_holder )
                        # print(val_)
                        # print(just_keys)  
    
    # print(sh_files_configmaps) 
    return sh_files_configmaps 

def scanForMissingSecurityContext(path_scrpt):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_scrpt )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_scrpt )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        key_lis = [] 
        parser.getKeyRecursively(yaml_di, key_lis)
        yaml_values = list( parser.getValuesRecursively(yaml_di) )
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        real_key_lis = [x_[0] for x_ in key_lis]
        # print(real_key_lis) 
        if (constants.SECU_CONT_KW  not in real_key_lis)  and ( constants.CONTAINER_KW in real_key_lis ): 
            occurrences = real_key_lis.count( constants.CONTAINER_KW )
            for _ in range( occurrences ):
                prop_value = constants.YAML_SKIPPING_TEXT
                # if ( constants.DEPLOYMENT_KW in yaml_values ) : 
                #     prop_value = constants.DEPLOYMENT_KW
                #     lis.append( prop_value )
                if ( constants.POD_KW in yaml_values ) :
                    pod_kw_lis = parser.keyMiner(  yaml_di, constants.POD_KW  )
                    if ( constants.KIND_KEY_NAME in pod_kw_lis ):
                        cnt += 1 
                        prop_value = constants.POD_KW 
                        lis.append( prop_value )
                        dic[ cnt ] = lis
    # print(dic) 
    return dic 


def scanForDefaultNamespace(path_scrpt):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_scrpt )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_scrpt )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        nspace_vals  = []
        parser.getValsFromKey( yaml_di, constants.NAMESPACE_KW, nspace_vals )
        # print(nspace_vals)
        '''
        we are not going to process list of dicts 
        '''
        nspace_vals        = [x_ for x_ in nspace_vals if isinstance( x_ , str ) ]
        unique_nspace_vals =  list( np.unique( nspace_vals  ) )
        if (len(unique_nspace_vals) == 1 ) and ( unique_nspace_vals[0] == constants.DEFAULT_KW  ): 
            key_lis = parser.keyMiner(yaml_di, constants.DEFAULT_KW)
            if (isinstance( key_lis, list ) ):
                if (len(key_lis) > 0 ) : 
                    all_values = list( parser.getValuesRecursively(yaml_di)  )
                    cnt += 1 
                    prop_value = constants.YAML_SKIPPING_TEXT 
                    if ( constants.DEPLOYMENT_KW in all_values ) : 
                        prop_value = constants.DEPLOYMENT_KW
                        lis.append( prop_value )
                    elif ( constants.POD_KW in all_values ) :
                        prop_value = constants.POD_KW 
                        lis.append( prop_value )
                    else: 
                        holder_ = [] 
                        parser.getValsFromKey(yaml_di, constants.KIND_KEY_NAME, holder_ )
                        if ( constants.K8S_SERVICE_KW in holder_ ): 
                            srv_val_li_ = [] 
                            parser.getValsFromKey( yaml_di, constants.K8S_APP_KW, srv_val_li_  ) 
                            for srv_val in srv_val_li_:
                                lis = graphtaint.mineServiceGraph( path_scrpt, yaml_di, srv_val )


                    dic[ cnt ] = lis
    # print(dic) 
    return dic 


def scanForResourceLimits(path_scrpt):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_scrpt )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_scrpt )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        '''
        get values for a key from the dict 
        then check if at least one unique entry is kind:Pod 
        '''
        val_lis = [] 
        parser.getValsFromKey(yaml_di, constants.KIND_KEY_NAME, val_lis) 
        kind_entries =  list( np.unique( val_lis ) )
        if ( constants.POD_KW in kind_entries ):
            if ( (constants.CONTAINER_KW in key_list) and (constants.LIMITS_KW not in key_list ) and ( (constants.CPU_KW not in key_list)  or (constants.MEMORY_KW not in key_list) ) ):
                cnt += 1 
                if( len(temp_ls) > 0 ):
                    all_values = list( parser.getValuesRecursively(yaml_di)  )
                    # print(all_values)
                    prop_value = constants.YAML_SKIPPING_TEXT 
                    if ( constants.POD_KW in all_values ) :
                        prop_value = constants.POD_KW 
                        lis.append( prop_value )
                dic[ cnt ] = lis
    # print(dic) 
    return dic 



def scanForRollingUpdates(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if ( (constants.STRATEGY_KW not in key_list ) and  (constants.ROLLING_UPDATE_KW not in key_list) and (constants.SPEC_KW in key_list)   ):
            if( len(temp_ls) > 0 ):
                all_values = list( parser.getValuesRecursively(yaml_di)  )
                # print(all_values)
                prop_value = constants.YAML_SKIPPING_TEXT 
                if ( constants.DEPLOYMENT_KW in all_values ) and ( constants.VAL_ROLLING_UPDATE_KW not in all_values ) : 
                    keyFromVal =  parser.keyMiner(yaml_di, constants.DEPLOYMENT_KW)
                    if( constants.KIND_KEY_NAME in keyFromVal ):
                        cnt += 1 
                        dic[ cnt ] = [ constants.DEPLOYMENT_KW ]
    return dic     


def scanForMissingNetworkPolicy(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        all_values = list( parser.getValuesRecursively(yaml_di)  )
        if ( constants.NET_POLICY_KW not in all_values ):
            cnt += 1 
            temp_ls = [] 
            parser.getKeyRecursively(yaml_di, temp_ls) 
            '''
            if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
            as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
            '''
            key_list = [ x_[0] for x_ in temp_ls  ]
            if ( (constants.SPEC_KW in key_list ) and  (constants.POD_SELECTOR_KW in key_list) and  (constants.MATCH_LABEL_KW in key_list) ):
                for src_val in all_values:
                    lis  = graphtaint.mineNetPolGraph(path_script, yaml_di, src_val, key_list )
            dic[ cnt ] = lis
    # print(dic) 
    return dic  

def scanForTruePID(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if (constants.SPEC_KW in key_list ) and ( constants.HOST_PID_KW in key_list ) :
            vals_for_pid = [] 
            parser.getValsFromKey(yaml_di, constants.HOST_PID_KW, vals_for_pid)
            # print(vals_for_pid)
            vals_for_pid = [str(z_) for z_ in vals_for_pid if isinstance( z_,  bool) ]
            vals_for_pid = [z_.lower() for z_ in vals_for_pid]
            if constants.TRUE_LOWER_KW in vals_for_pid: 
                cnt += 1 
                dic[ cnt ] = []
    return dic  


def scanForTrueIPC(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if (constants.SPEC_KW in key_list ) and ( constants.HOST_IPC_KW in key_list ) :
            vals_for_ipc = [] 
            parser.getValsFromKey(yaml_di, constants.HOST_IPC_KW, vals_for_ipc)
            vals_for_ipc = [str(z_) for z_ in vals_for_ipc if isinstance( z_,  bool) ]
            vals_for_ipc = [z_.lower() for z_ in vals_for_ipc]
            if constants.TRUE_LOWER_KW in vals_for_ipc: 
                cnt += 1 
                dic[ cnt ] = []
    return dic  

def scanDockerSock(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if ( all( z_ in key_list for z_ in constants.DOCKERSOCK_KW_LIST )  ) :
            all_values = list( parser.getValuesRecursively(yaml_di)  )
            if (constants.DOCKERSOCK_PATH_KW in all_values):
                cnt += 1 
                dic[ cnt ] = []
    return dic  

def runScanner(dir2scan):
    all_content   = [] 
    all_yml_files = getYAMLFiles(dir2scan)
    val_cnt       = 0 
    for yml_ in all_yml_files:
        '''
        Need to filter out `.github/workflows.yml files` first 
        '''
        if(parser.checkIfWeirdYAML ( yml_  )  == False): 
            if( parser.checkIfValidK8SYaml( yml_ ) ) or (  parser.checkIfValidHelm( yml_ ) ) :
                val_cnt = val_cnt + 1 
                print(constants.ANLYZING_KW + yml_ + constants.COUNT_PRINT_KW + str(val_cnt) )
                # get secrets and over privileges 
                within_secret_, templ_secret_, valid_taint_secr, valid_taint_privi  = scanSingleManifest( yml_ )
                # get insecure HTTP            
                http_dict             = scanForHTTP( yml_ )
                # get missing security context 
                absentSecuContextDict = scanForMissingSecurityContext( yml_ )
                # get use of default namespace 
                defaultNameSpaceDict  = scanForDefaultNamespace( yml_ )
                # get missing resource limit 
                absentResourceDict    = scanForResourceLimits( yml_ )
                # get absent rolling update count 
                rollingUpdateDict     = scanForRollingUpdates( yml_ )
                # get absent network policy count 
                absentNetPolicyDic    = scanForMissingNetworkPolicy( yml_ )
                # get hostPIDs where True is assigned 
                pid_dic               = scanForTruePID( yml_ )
                # get hostIPCs where True is assigned 
                ipc_dic               = scanForTrueIPC( yml_ )
                # scan for docker sock paths: /var.run/docker.sock 
                dockersock_dic        = scanDockerSock( yml_ )
                # scan for hostNetwork where True is assigned 
                host_net_dic          = scanForHostNetwork( yml_ )
                # scan for CAP SYS 
                cap_sys_dic           = scanForCAPSYS( yml_ )
                # scan for Host Aliases 
                host_alias_dic        = scanForHostAliases( yml_ )
                # scan for allowPrivilegeEscalation 
                allow_privi_dic       = scanAllowPrivileges( yml_ )
                # scan for unconfied seccomp 
                unconfied_seccomp_dict= scanForUnconfinedSeccomp( yml_ )
                # scan for cap sys module 
                cap_module_dic        = scanForCAPMODULE( yml_ )
                # need the flags to differentiate legitimate HELM and K8S flags 
                helm_flag             = parser.checkIfValidHelm(yml_)
                k8s_flag              = parser.checkIfValidK8SYaml(yml_)
                all_content.append( ( dir2scan, yml_, within_secret_, templ_secret_, valid_taint_secr, valid_taint_privi, http_dict, absentSecuContextDict, defaultNameSpaceDict, absentResourceDict, rollingUpdateDict, absentNetPolicyDic, pid_dic, ipc_dic, dockersock_dic, host_net_dic, cap_sys_dic, host_alias_dic, allow_privi_dic, unconfied_seccomp_dict, cap_module_dic, k8s_flag, helm_flag ) )
                print(constants.SIMPLE_DASH_CHAR ) 


    return all_content


def scanForHostNetwork(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if (constants.SPEC_KW in key_list ) and ( constants.HOST_NET_KW in key_list ) :
            vals_for_net = [] 
            parser.getValsFromKey(yaml_di, constants.HOST_NET_KW, vals_for_net)
            # print(vals_for_net)
            vals_for_net = [str(z_) for z_ in vals_for_net if isinstance( z_,  bool) ]
            vals_for_net = [z_.lower() for z_ in vals_for_net]
            if constants.TRUE_LOWER_KW in vals_for_net: 
                cnt += 1 
                dic[ cnt ] = []
    return dic  


def scanForCAPSYS(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if ( all( z_ in key_list for z_ in constants.CAPSYS_KW_LIST )  ) :
            relevant_values = parser.getValuesRecursively(yaml_di)
            if (constants.CAPSYS_ADMIN_STRING in relevant_values) :
                cnt += 1 
                dic[ cnt ] = []
    return dic  

def scanForCAPMODULE(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if ( all( z_ in key_list for z_ in constants.CAPSYS_KW_LIST )  ) :
            relevant_values = parser.getValuesRecursively(yaml_di)
            if (constants.CAPSYS_MODULE_STRING in relevant_values) :
                cnt += 1 
                dic[ cnt ] = []
    return dic      

def scanForHostAliases(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        if ( constants.HOST_ALIAS_KW in key_list ) :
                cnt += 1 
                relevant_values = [] 
                parser.getValsFromKey(yaml_di, constants.HOST_ALIAS_KW, relevant_values)
                dic[ cnt ] = relevant_values
    return dic  


def scanAllowPrivileges(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        # print(key_list)
        if ( all( var in key_list for var in constants.ALLOW_PRIVI_KW_LIST ) ) :
                cnt += 1 
                relevant_values = [] 
                parser.getValsFromKey(yaml_di, constants.ALLOW_PRIVILEGE_KW, relevant_values)
                relevant_values = [str(x_) for x_ in relevant_values if isinstance(x_, bool)]
                relevant_values = [x_.lower() for x_ in relevant_values]
                if constants.TRUE_LOWER_KW in relevant_values:
                    dic[cnt] = [] 
    return dic  


def scanForUnconfinedSeccomp(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_ls = [] 
        parser.getKeyRecursively(yaml_di, temp_ls) 
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        key_list = [ x_[0] for x_ in temp_ls  ]
        # print(key_list)
        if ( all( var in key_list for var in constants.SECCOMP_KW_LIST ) ) :
                cnt += 1 
                relevant_values = [] 
                parser.getValsFromKey(yaml_di, constants.TYPE_KW, relevant_values)
                # print( relevant_values )
                if constants.UNCONFIED_KW in relevant_values:
                    dic[cnt] = [] 
    return dic  

if __name__ == '__main__':
    # test_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml'
    # scanSingleManifest(test_yaml) 
    # another_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/values.yaml'
    # another_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/minecraft/values.yaml'

    # tp_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/turkce-kubernetes/kubernetes-playground/replication-yontemlerine-genel-bakis/replication/deployment.yaml'
    # fp_yaml = 'TEST_ARTIFACTS/no.secu.nfs.yaml' 
    # scanForMissingSecurityContext( fp_yaml ) 

    # tp_http = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-glance-setup.yaml'
    # scanForHTTP( tp_http )

    # tp_pid  = 'TEST_ARTIFACTS/tp.host.net2.yaml'
    # a_dict  = scanForHostNetwork( tp_pid )

    # tp_docker_sock   = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/gitlab-runner/gitlab-runner-docker-deployment.yml' 
    # a_dict           = scanDockerSock( tp_docker_sock )

    # cap_sys_yaml = 'TEST_ARTIFACTS/cap.sys.yaml'
    # a_dict       = scanForHostAliases( cap_sys_yaml )
    
    # allow_privi_yaml = 'TEST_ARTIFACTS/allow.privilege.yaml'
    # a_dict           = scanAllowPrivileges( allow_privi_yaml  )

    # missing_net_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/lb/nginx-dep.yaml'
    # a_dict           = scanForMissingNetworkPolicy( missing_net_yaml )

    # seccomp_unconfined_yaml = 'TEST_ARTIFACTS/fp.seccomp.unconfined.yaml'
    # a_dict                  = scanForUnconfinedSeccomp( seccomp_unconfined_yaml )

    # over_privilege  = 'TEST_ARTIFACTS/multi.doc.yaml'
    # scanForOverPrivileges( over_privilege )

    # no_http_file        = 'TEST_ARTIFACTS/fp.http.yaml'
    # sh_files_configmaps = scanForHTTP( no_http_file )

    # special_secret1     = 'TEST_ARTIFACTS/special.secret1.yaml'
    # within_secret_, templ_secret_, valid_taint_secr, valid_taint_privi  = scanSingleManifest( special_secret1 )

    # no_reso_yaml = '/Users/arahman/K8S_REPOS/GITHUB_REPOS/istio-handson/deployment/articles.yaml'
    # no_reso_dict = scanForHTTP(no_reso_yaml)

    # cap_sys_module_yaml = 'TEST_ARTIFACTS/cap-module-ostk.yaml'
    # cap_sys_module_dic  = scanForCAPMODULE ( cap_sys_module_yaml )   

    print(cap_sys_module_dic)  