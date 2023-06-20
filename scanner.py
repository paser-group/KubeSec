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
import json
from sarif_om import *
from jschema_to_python.to_json import to_json

'''Global SarifLog Object definition and Rule definition for SLI-KUBE. Rule IDs are ordered by the sequence as it appears in the TOSEM paper'''

sarif_log = SarifLog(version='2.1.0',schema_uri='https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json', runs =[])
run = Run(tool=Tool(driver=ToolComponent(name = 'SLI-KUBE', version = '2.0.0',information_uri ='https://github.com/paser-group/KubeSec',organization = 'PASER',rules=[])))
sarif_log.runs.append(run)
run.results = []
slikube_01 =  ReportingDescriptor(id='SLIKUBE_01',name=" Absent Resource Limit",short_description=Message(text="Specify resource limits for containers within a pod"),full_description= Message( text= "Specify resource limits for containers within a pod"),help= Message(text= "Specify resource limits for containers within a pod"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_01)
slikube_02 =  ReportingDescriptor(id='SLIKUBE_02',name=" Absent securityContext",short_description=Message(text=" Use securityContext while provisioning containers"),full_description= Message( text= " Use securityContext while provisioning containers"),help= Message(text= " Use securityContext while provisioning containers"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_02)
slikube_03 =  ReportingDescriptor(id='SLIKUBE_03',name=" Activation of hostIPC",short_description=Message(text=" Deactivate hostIPC while specifying configurations in Kubernetes manifests"),full_description= Message( text= " Deactivate hostIPC while specifying configurations in Kubernetes manifests"),help= Message(text= "Deactivate hostIPC while specifying configurations in Kubernetes manifests"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_03)
slikube_04 =  ReportingDescriptor(id='SLIKUBE_04',name=" Activation of hostNetwork",short_description=Message(text=" Deactivate hostNetwork while specifying configurations in Kubernetes manifests"),full_description= Message( text= " Deactivate hostNetwork while specifying configurations in Kubernetes manifests"),help= Message(text= " Deactivate hostNetwork while specifying configurations in Kubernetes manifests"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_04)
slikube_05 =  ReportingDescriptor(id='SLIKUBE_05',name=" Activation of hostPID",short_description=Message(text=" Deactivate hostPID while specifying configurations in Kubernetes manifests"),full_description= Message( text= " Deactivate hostPID while specifying configurations in Kubernetes manifests"),help= Message(text=  "Deactivate hostPID while specifying configurations in Kubernetes manifests"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_05)
slikube_06 =  ReportingDescriptor(id='SLIKUBE_06',name=" Capability Misuse",short_description=Message(text=" Avoid misuse with CAP_SYS_ADMIN, and misuse with CAP_SYS_MODULE configurations"),full_description= Message( text= "Avoid misuse with CAP_SYS_ADMIN, and misuse with CAP_SYS_MODULE configurations"),help= Message(text= "Avoid misuse with CAP_SYS_ADMIN, and misuse with CAP_SYS_MODULE configurations"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_06)
slikube_07 =  ReportingDescriptor(id='SLIKUBE_07',name=" Docker Socket Mounting",short_description=Message(text=" Avoid mounting of the Docker socket path by using the /var/run/docker.sock configuration"),full_description= Message( text= "Avoid mounting of the Docker socket path by using the /var/run/docker.sock configuration"),help= Message(text= "Avoid mounting of the Docker socket path by using the /var/run/docker.sock configuration"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_07)
slikube_08 =  ReportingDescriptor(id='SLIKUBE_08',name=" Escalated Privileges for Child Container Processes",short_description=Message(text=" Avoid allocating privileges for child processes within a container that are higher than that of the parent processes with allowPrivilegeEscaltion : true"),full_description= Message( text= " Avoid allocating privileges for child processes within a container that are higher than that of the parent processes with allowPrivilegeEscaltion : true"),help= Message(text= " Avoid allocating privileges for child processes within a container that are higher than that of the parent processes with allowPrivilegeEscaltion : true"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_08)
slikube_09 =  ReportingDescriptor(id='SLIKUBE_09',name=" Hard-coded Secret",short_description=Message(text=" Avoid providing hard-coded secrets. Do not provide (i) hard-coded usernames, (ii) hard-coded passwords, and (iii) hard-coded private tokens in Kubernetes manifests."),full_description= Message( text= " Avoid providing hard-coded secrets. Do not provide (i) hard-coded usernames, (ii) hard-coded passwords, and (iii) hard-coded private tokens in Kubernetes manifests."),help= Message(text= " Avoid providing hard-coded secrets. Do not provide (i) hard-coded usernames, (ii) hard-coded passwords, and (iii) hard-coded private tokens in Kubernetes manifests."), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_09)
slikube_10 =  ReportingDescriptor(id='SLIKUBE_10',name=" Use of HTTP without TLS",short_description=Message(text=" Avoid using HTTP without SSL/TLS certificates to setup URLs or transmit traffic inside and outside the Kubernetes clusters"),full_description= Message( text= " Avoid using HTTP without SSL/TLS certificates to setup URLs or transmit traffic inside and outside the Kubernetes clusters"),help= Message(text= "Avoid using HTTP without SSL/TLS certificates to setup URLs or transmit traffic inside and outside the Kubernetes clusters"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_10)
slikube_11 =  ReportingDescriptor(id='SLIKUBE_11',name=" Privileged securityContext",short_description=Message(text="Avoid using privileged securityContext in Kubernetes manifests"),full_description= Message( text= "Avoid using privileged securityContext in Kubernetes manifests"),help= Message(text= "Avoid using privileged securityContext in Kubernetes manifests"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_11)
slikube_UNLISTED_01 =  ReportingDescriptor(id='SLIKUBE_UNLISTED_01',name=" Use of Default Namespace",short_description=Message(text=" Avoid using the default namespace"),full_description= Message( text= "  Avoid using the default namespace"),help= Message(text= " Avoid using the default namespace"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_UNLISTED_01)
slikube_UNLISTED_02 =  ReportingDescriptor(id='SLIKUBE_UNLISTED_02',name=" No Use of Rolling Update",short_description=Message(text="  Use rolling update for deployment"),full_description= Message( text= " Use rolling update for deployment"),help= Message(text= "Use rolling update for deployment"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_UNLISTED_02)
slikube_UNLISTED_03 =  ReportingDescriptor(id='SLIKUBE_UNLISTED_03',name=" No Network Policy",short_description=Message(text=" Use network policy in pod specification"),full_description= Message( text= " Use network policy in pod specification"),help= Message(text= "Use network policy in pod specification"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_UNLISTED_03)
slikube_UNLISTED_04 =  ReportingDescriptor(id='SLIKUBE_UNLISTED_04',name=" Use of Host Aliases",short_description=Message(text="Avoid Using Host Aliases"),full_description= Message( text= "Avoid Using Host Aliases"),help= Message(text= "Avoid Using Host Aliases"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_UNLISTED_04)
slikube_UNLISTED_05 =  ReportingDescriptor(id='SLIKUBE_UNLISTED_05',name=" Use of unconfined seccomp profile",short_description=Message(text=" Use Seccomp security profiles"),full_description= Message( text= "  Use Seccomp security profiles"),help= Message(text= " Use Seccomp security profiles"), default_configuration= ReportingConfiguration(level="error"))
run.tool.driver.rules.append(slikube_UNLISTED_05)


'''Following lists are used to check the statistics of analyzed files such as invalid, weird and valid k8s and helm charts'''

invalid_yaml = []
weird_yaml = []
helm_chart = []
k8s_yaml =[]

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
        # print('KEY LIST ALL-------------------------------------')
        # print(key_lis)
        '''
        if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
        as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
        '''
        just_keys = [x_[0] for x_ in key_lis] 
        # print('JUST KEYS ALL -----------------------------------------------------')
        # print(just_keys)
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
                            line_number = parser.show_line_for_paths(script_path, constants.PRIVI_KW)
                            for line in line_number:
                                result= Result(rule_id='SLIKUBE_11',rule_index= 10, level='error',attachments = [] ,message=Message(text=" Privileged securityContext"))
                                location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=script_path),region = Region(start_line =line)))
                                result.locations = [location]
                                run.results.append(result)
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
    
    # for each key in dict_secret we extract the key, return the line number and extracted valid taints for the secret

    for key in dict_secret:
        line_number = parser.show_line_for_paths(path_to_script, key)
        for line in line_number:
            print(line)
            secret, template_secret, valid_taint = graphtaint.mineSecretGraph(path_to_script, yaml_dict, dict_secret)
            '''Included valid taints in attachments []'''
            result= Result(rule_id='SLIKUBE_09',rule_index= 8, level='error',attachments = [valid_taint] ,message=Message(text=" Hard-coded Secret"))
            location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_to_script),region = Region(start_line =line)))
            result.locations = [location]
            run.results.append(result)

    _, templ_secret_, valid_taint_secr  = graphtaint.mineSecretGraph(path_to_script, yaml_dict, dict_secret) 
    # print(within_secret_) 
    # print(templ_secret_) 
    # print(valid_taint_secr) 
    '''
    taint tracking for over privileges 
    '''
    #valid_taint_privi  = scanForOverPrivileges( path_to_script )
    # print(valid_taint_privi) 

    return within_secret_, templ_secret_, valid_taint_secr 


 

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

                        # As absent securityContext, we assume that it should be in pod specification so line number will be the line number of the spec.
                        line_number = parser.show_line_for_paths(path_scrpt,constants.SPEC_KW)
                        for line in line_number:
                            result= Result(rule_id='SLIKUBE_02',rule_index=1, level='error',attachments = [] ,message=Message(text=" Absent securityContext"))
                            location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_scrpt),region = Region(start_line =line)))
                            result.locations = [location]
                            run.results.append(result)
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
                    
                    # Lines for SARIF output
                    line_number = parser.show_line_for_paths(path_scrpt,constants.NAMESPACE_KW)
                    for line in line_number:
                        result= Result(rule_id='SLIKUBE_UNLISTED_01',rule_index= 11, level='error',attachments = [] ,message=Message(text=" Use of Default Namespace"))
                        location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_scrpt),region = Region(start_line =line)))
                        result.locations = [location]
                        run.results.append(result)
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
                # the line number for SARIF output should be the line number of the container spec 
                line_number = parser.show_line_for_paths(path_scrpt, constants.SPEC_KW)
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_01',rule_index= 0, level='error',attachments = [] ,message=Message(text="  Absent Resource Limit"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_scrpt),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)

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
                        # the line number for SARIF output should be the line number of the container spec for rolling update
                        line_number = parser.show_line_for_paths(path_script,constants.SPEC_KW)
                        for line in line_number:
                            result= Result(rule_id='SLIKUBE_UNLISTED_02',rule_index= 12, level='error',attachments = [] ,message=Message(text=" No Use of Rolling Update"))
                            location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                            result.locations = [location]
                            run.results.append(result)
                        dic[ cnt ] = [ constants.DEPLOYMENT_KW ]
    return dic     


def scanForMissingNetworkPolicy(path_script ):
    dic, lis   = {}, []
    if ( parser.checkIfValidK8SYaml( path_script )  ): 
        cnt = 0 
        dict_as_list = parser.loadMultiYAML( path_script )
        yaml_di      = parser.getSingleDict4MultiDocs( dict_as_list )        
        all_values = list( parser.getValuesRecursively(yaml_di)  )
        #print(all_values)
        #print(all_values)
        if ( constants.NET_POLICY_KW not in all_values ):
            cnt += 1 
            temp_ls = [] 
            parser.getKeyRecursively(yaml_di, temp_ls) 
            '''
            if you are using `parser.getKeyRecursively` to get all keys , you need to do some trnasformation to get the key names 
            as the output is a list of tuples so, `[(k1, v1), (k2, v2), (k3, v3)]`
            '''
            #print (temp_ls)
            key_list = [ x_[0] for x_ in temp_ls  ]
            #print(key_list)
            
            # specification is present the line number of the SARIF output should be the line number of the container spec 
            if (constants.SPEC_KW in key_list ):
                line_number = parser.show_line_for_paths(path_script,constants.SPEC_KW)
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_UNLISTED_03',rule_index= 13, level='error',attachments = [] ,message=Message(text=" No Use of Network Policy"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
            # if specification is not present the line number of the SARIF output is be the first line number
            else:
                line = 1
                result= Result(rule_id='SLIKUBE_UNLISTED_03',rule_index= 13, level='error',attachments = [] ,message=Message(text=" No Use of Network Policy"))
                location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                result.locations = [location]
                run.results.append(result)
            
            dic[ cnt ] = [ constants.NET_POLICY_KW ]
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
                # For Sarif output 
                line_number = parser.show_line_for_paths(path_script,constants.HOST_PID_KW)
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_05',rule_index= 4, level='error',attachments = [] ,message=Message(text=" Activation of hostPID"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
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
                # For Sarif output 
                line_number = parser.show_line_for_paths(path_script,constants.HOST_IPC_KW)
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_03',rule_index= 2, level='error',attachments = [] ,message=Message(text=" Activation of hostIPC"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
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
                docker_sock_path = parser.keyMiner(yaml_di, constants.DOCKERSOCK_PATH_KW)
                # The last element of the http_in_spec is the value so the second last element is a . so third last element of the docker_sock_path is the key

                line_number = parser.show_line_for_paths(path_script,docker_sock_path[-2])
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_07',rule_index= 6, level='error',attachments = [] ,message=Message(text=" Docker Socket Mounting"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
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
            print ("\n\n--------------- FILE --------------\n\t-->",yml_)
            if( ( parser.checkIfValidK8SYaml( yml_ ) ) or (  parser.checkIfValidHelm( yml_ ) ) ) and parser.checkParseError( yml_) :
                # print (" \n\n--------------- FILE RUNNING NOW---------------")
                # print (yml_)
                # print("---------------############################### ------\n\n\n")
                helm_flag             = parser.checkIfValidHelm(yml_)
                k8s_flag              = parser.checkIfValidK8SYaml(yml_)
                if (helm_flag):
                    helm_chart.append(yml_)
                    print("HELM Chart")

                if (k8s_flag):
                    k8s_yaml.append(yml_)
                    print("Kubernetes YAML")
                
                val_cnt = val_cnt + 1 
                print(constants.ANLYZING_KW + yml_ + constants.COUNT_PRINT_KW + yml_ +str(val_cnt) )
               
                print("get valid taint secrets")
                within_secret_, templ_secret_, valid_taint_secr  = scanSingleManifest( yml_ )


                print("get privileged security contexts")
                valid_taint_privi  = scanForOverPrivileges( yml_ )
               
                print("get insecure HTTP")            
                http_dict             = scanForHTTP( yml_ )
               
                print("get missing security context") 
                absentSecuContextDict = scanForMissingSecurityContext( yml_ )
               
                print("get use of default namespace") 
                defaultNameSpaceDict  = scanForDefaultNamespace( yml_ )
               
                print("get missing resource limit")
                absentResourceDict    = scanForResourceLimits( yml_ )

                print("get absent rolling update count") 
                rollingUpdateDict     = scanForRollingUpdates( yml_ )

                print("get absent network policy count") 
                absentNetPolicyDic    = scanForMissingNetworkPolicy( yml_ )

                print(" get hostPIDs where True is assigned ")
                pid_dic               = scanForTruePID( yml_ )

                print("get hostIPCs where True is assigned") 
                ipc_dic               = scanForTrueIPC( yml_ )
                
                print("scan for docker sock paths: /var.run/docker.sock") 
                dockersock_dic        = scanDockerSock( yml_ )

                print("scan for hostNetwork where True is assigned ")
                host_net_dic          = scanForHostNetwork( yml_ )
                
                print("scan for CAP SYS") 
                cap_sys_dic           = scanForCAPSYS( yml_ )
                
                print("scan for Host Aliases") 
                host_alias_dic        = scanForHostAliases( yml_ )
                
                print("scan for allowPrivilegeEscalation") 
                allow_privi_dic       = scanForAllowPrivileges( yml_ )
                
                print("scan for unconfied seccomp ")
                unconfied_seccomp_dict= scanForUnconfinedSeccomp( yml_ )
                
                print(" scan for cap sys module ")
                cap_module_dic        = scanForCAPMODULE( yml_ )
                # need the flags to differentiate legitimate HELM and K8S flags 
                
                print (" \n\n---------------END FILE RUNNING--------------")
                print(constants.SIMPLE_DASH_CHAR )
                
                #print(yml_)
                
                                      
                # sarif_json = to_json(sarif_log)
                # print(sarif_json)
                # #Write the JSON string to a file
                # sarif_file = yml_.split('\\')[-1].split('.')[0]+'.sarif'
                # with open(sarif_file, "w") as f:
                #     f.write(sarif_json)

                all_content.append( ( dir2scan, yml_, within_secret_, templ_secret_, valid_taint_secr, valid_taint_privi, http_dict, absentSecuContextDict, defaultNameSpaceDict, absentResourceDict, rollingUpdateDict, absentNetPolicyDic, pid_dic, ipc_dic, dockersock_dic, host_net_dic, cap_sys_dic, host_alias_dic, allow_privi_dic, unconfied_seccomp_dict, cap_module_dic, k8s_flag, helm_flag ) )
            else:
                print("Invalid YAML --> ",yml_)
                invalid_yaml.append(yml_)
        else:
            print(" Weird YAML --> ",yml_)
            weird_yaml.append(yml_)

        sarif_json = to_json(sarif_log)
        #print(sarif_json)       


    return all_content, sarif_json


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
                line_number = parser.show_line_for_paths(path_script,constants.HOST_NET_KW)
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_04',rule_index= 3, level='error',attachments = [] ,message=Message(text=" Activation of hostNetwork"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
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
                capsys_key = parser.keyMiner(yaml_di, constants.CAPSYS_ADMIN_STRING)
                #print(capsys_key)
                # ['spec.YAML.DOC.2', 'template', 'spec', 'containers', '0', 'securityContext', 'capabilities', 'add', '1', 'CAP_SYS_ADMIN'] --> [-3]
                # Line number of the line where the key was found for CAPSYS_ADMIN  to provide  SARIF output
                line_number = parser.show_line_for_paths(path_script,capsys_key[-3])
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_06',rule_index= 5, level='error',attachments = [] ,message=Message(text=" Capability Misuse"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
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
                capsys_key = parser.keyMiner(yaml_di, constants.CAPSYS_MODULE_STRING)
                #print(capsys_key)
                #['spec.YAML.DOC.2', 'template', 'spec', 'containers', '0', 'securityContext', 'capabilities', 'add', '2', 'CAP_SYS_MODULE']
                # Line number of the line where the key was found for CAPSYS_MODULE to provide  SARIF output
                line_number = parser.show_line_for_paths(path_script,capsys_key[-3])
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_06',rule_index= 5, level='error',attachments = [] ,message=Message(text=" Capability Misuse"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
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
                # Line number of the line where the key was found for CAPSYS_MODULE to provide  SARIF output
                line_number = parser.show_line_for_paths(path_script,constants.HOST_ALIAS_KW)
                for line in line_number:
                    result= Result(rule_id='SLIKUBE_UNLISTED_04',rule_index= 14, level='error',attachments = [] ,message=Message(text=" Use of Host Aliases"))
                    location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                    result.locations = [location]
                    run.results.append(result)
                relevant_values = [] 
                parser.getValsFromKey(yaml_di, constants.HOST_ALIAS_KW, relevant_values)
                dic[ cnt ] = relevant_values
    return dic  


def scanForAllowPrivileges(path_script ):
    dic, lis   = {}, []
    #print(path_script)
    # with open(path_script, "r") as f:
    #     for line in f.readlines():
    #         print(line)
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
        #print(key_list)
        if ( all( var in key_list for var in constants.ALLOW_PRIVI_KW_LIST ) ) :
                cnt += 1 
                relevant_values = [] 
                parser.getValsFromKey(yaml_di, constants.ALLOW_PRIVILEGE_KW, relevant_values)
                relevant_values = [str(x_) for x_ in relevant_values if isinstance(x_, bool)]
                relevant_values = [x_.lower() for x_ in relevant_values]
                if constants.TRUE_LOWER_KW in relevant_values:
                    dic[cnt] = []
                    line_number = parser.show_line_for_paths(path_script, constants.ALLOW_PRIVILEGE_KW)
                    for line in line_number:
                        #print(line7
                        result= Result(rule_id='SLIKUBE_08',rule_index= 7, message=Message(text="Escalated Privileges for Child Container Processes"),level='error')
                        location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))                       
                        result.locations = [location]
                        #print(result)
                        #result.locations.append(location)
                        #run.results = [result]   
                        #print(result) 
                        run.results.append(result)
    return dic  

def scanForHTTP( path2script ):
    sh_files_configmaps = {} 
    http_count = 0 
    if parser.checkIfValidK8SYaml( path2script ) or parser.checkIfValidHelm( path2script ) or True:
        dict_as_list = parser.loadMultiYAML( path2script )
        yaml_d       = parser.getSingleDict4MultiDocs( dict_as_list )
        all_vals     = list (parser.getValuesRecursively( yaml_d )  )
        all_vals     = [x_ for x_ in all_vals if isinstance(x_, str) ] 
        #print(all_vals)
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
                http_in_spec = parser.keyMiner(yaml_d,val_)
                # The last element of the http_in_spec is the value so the second last element of the http_in_spec is the key
                http_key = http_in_spec[-2]
                print(" THIS IS HTTP KEY ----> ", http_key)

                if ( constants.SPEC_KW in just_keys ):
                    '''
                    this branch is for HTTP values coming from Deplyoment manifests  
                    '''                    
                    http_count += 1 
                    sh_files_configmaps[http_count] =  val_ 

                    line_number = parser.show_line_for_paths(path2script, http_key)
                    for line in line_number:
                            # print(line)
                            result= Result(rule_id='SLIKUBE_10',rule_index= 9,level='error', attachments= [], message=Message(text="Use of HTTP without TLS"),)
                            location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path2script),region = Region(start_line =line)))
                            result.locations = [location] 
                            run.results.append(result)
                            
                elif( parser.checkIfValidHelm( path2script ) ):
                    '''
                    this branch is for HTTP values coming from Values.yaml in HELM charts  
                    '''
                    http_count += 1 
                    matching_keys = parser.keyMiner(yaml_d, val_)
                    key_ = matching_keys[-1]  
                    infected_list = graphtaint.mineViolationGraph(path2script, yaml_d, val_, key_) 
                    sh_files_configmaps[http_count] = infected_list
                    line_number = parser.show_line_for_paths(path2script, http_key)
                    for line in line_number:
                            #print(line)
                            result= Result(rule_id='SLIKUBE_10',rule_index= 9,level='error', attachments= [], message=Message(text="Use of HTTP without TLS"),)
                            location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path2script),region = Region(start_line =line)))
                            result.locations = [location] 
                            run.results.append(result)
                    
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
                        line_number = parser.show_line_for_paths(path2script, http_key)
                        for line in line_number:
                            #print(line)
                            result= Result(rule_id='SLIKUBE_10',rule_index= 9,level='error', attachments= [], message=Message(text="Use of HTTP without TLS"),)
                            location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path2script),region = Region(start_line =line)))
                            result.locations = [location] 
                            run.results.append(result)
                         
    
    # print(sh_files_configmaps) 
    return sh_files_configmaps

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
                    line_number = parser.show_line_for_paths(path_script,constants.UNCONFIED_KW)
                    for line in line_number:
                        result= Result(rule_id='SLIKUBE_UNLISTED_05',rule_index= 4, level='error',attachments = [] ,message=Message(text=" Use of unconfined seccomp profile"))
                        location = Location(physical_location=PhysicalLocation(artifact_location=ArtifactLocation(uri=path_script),region = Region(start_line =line)))
                        result.locations = [location]
                        run.results.append(result)
                    dic[cnt] = [] 
    return dic  

if __name__ == '__main__':
    #provide directory to scan
    dir2scan = r'C:\Users\..'
    a,b = runScanner(dir2scan)
    with open("test-scanner.sarif", "w") as f:
        f.write(b)