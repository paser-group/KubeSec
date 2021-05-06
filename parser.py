'''
Akond Rahman 
April 30, 2021 
Parser to file YAML files
'''

import yaml
import constants 

def loadYAML( script_ ):
    dict2ret = {}
    with open(script_, constants.FILE_READ_FLAG  ) as yml_content :
        try:
            dict2ret =   yaml.safe_load(yml_content) 
        except yaml.YAMLError as exc:
            print( constants.YAML_SKIPPING_TEXT  )    
    return dict2ret 

def keyMiner(dic_, value):
  '''
  If you give a value, then this function gets the corresponding key, and the keys that call the key 
  i.e. the whole hierarchy 
  '''
  if dic_ == value:
    return [dic_]
  elif isinstance(dic_, dict):
    for k, v in dic_.items():
      p = keyMiner(v, value)
      if p:
        return [k] + p
  elif isinstance(dic_, list):
    lst = dic_
    for i in range(len(lst)):
      p = keyMiner(lst[i], value)
      if p:
        return [str(i)] + p



def getKeyRecursively(  dict_, list2hold,  depth_ = 0  ) :
    '''
    gives you ALL keys in a regular/nested dictionary 
    '''
    if  isinstance(dict_, dict) :
        for key_, val_ in sorted(dict_.items(), key=lambda x: x[0]):              
            if isinstance(val_, dict):
                list2hold.append( (key_, depth_) )
                depth_ += 1 
                getKeyRecursively( val_, list2hold,  depth_ ) 
            elif isinstance(val_, list):
                for listItem in val_:
                        if( isinstance( listItem, dict ) ):
                            list2hold.append( (key_, depth_) )
                            depth_ += 1 
                            getKeyRecursively( listItem, list2hold,  depth_ )     
            else: 
                list2hold.append( (key_, depth_) )                

def getValuesRecursively(  dict_   ) :
    '''
    gives you ALL values in a regular/nested dictionary 
    '''
    if  isinstance(dict_, dict) :
        for val_ in dict_.values():
            yield from getValuesRecursively(val_) 
    elif isinstance(dict_, list):
        for v_ in dict_:
            yield from getValuesRecursively(v_)
    else: 
        yield dict_


def checkIfValidK8SYaml(path2yaml):
    val2ret   = False 
    yaml_dict = loadYAML( path2yaml )
    k_list    = []
    getKeyRecursively( yaml_dict, k_list )
    temp_ = []
    for k_ in k_list:
        temp_.append( k_[0]  )
    key_lis      = list( getValuesRecursively  ( yaml_dict ) )
    if ( any(x_ in key_lis for x_ in constants.K8S_FORBIDDEN_KW_LIST ) ): 
        val2ret = False 
    else: 
        if ( constants.API_V_KEYNAME in temp_ ) and (constants.KIND_KEY_NAME in temp_):
            val2ret = True 
    return val2ret


def getValsFromKey(dict_, target, list_holder  ):
    '''
    If you give a key, then this function gets the corresponding values 
    Multiple values are returned if there are keys with the same name  
    '''    
    if ( isinstance( dict_, dict ) ):
        for key, value in dict_.items():
            if isinstance(value, dict):
                getValsFromKey(value, target, list_holder)
            elif isinstance(value, list):
                for ls in value:
                    getValsFromKey(ls, target, list_holder)
            elif key == target:
                list_holder.append( value )

def checkIfValidHelm(path_script):
    val_ret = False 
    if ( (constants.HELM_KW in path_script) or (constants.CHART_KW in path_script) or (constants.SERVICE_KW in path_script) or (constants.INGRESS_KW in path_script)  or(constants.HELM_DEPLOY_KW in path_script) or (constants.CONFIG_KW in path_script) )  and (constants.VALUE_KW in path_script) :
        val_ret = True 
    return val_ret


def readYAMLAsStr( path_script ):
    yaml_as_str = constants.YAML_SKIPPING_TEXT
    with open( path_script , constants.FILE_READ_FLAG) as file_:
        yaml_as_str = file_.read()
    return yaml_as_str


if __name__=='__main__':
    dic = loadYAML('/Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/templates/integrate-grafana-job.yaml')
    # getKeyRecursively( dic )
    # print('-'*100)
    # print( keyMiner(dic, '/usr/local/airflow/analytics' ) )

    # temp_ = []
    # getValsFromKey( dic,  'allowPrivilegeEscalation', temp_ )
    # temp_ = []
    # getValsFromKey( dic,  'name', temp_ )
    # temp_ = []
    # getValsFromKey( dic,  'mountPath', temp_ )
    # print(   temp_ ) 
    # print( next(  getValFromKey( dic,  'runAsUser' ) ) )
    # print( next(  getValFromKey( dic,  'mountPath' ) ) )
    # print( next(  getValFromKey( dic,  'name' ) ) )
    
    
