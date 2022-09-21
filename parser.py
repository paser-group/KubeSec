'''
Akond Rahman 
April 30, 2021 
Parser to file YAML files
'''

import yaml
import constants 

def checkIfWeirdYAML(yaml_script):
    '''
    to filter invalid YAMLs such as ./github/workflows/ 
    '''
    val = False
    if ( any(x_ in yaml_script for x_ in constants.WEIRD_PATHS  ) ):
        val = True 
    return val 



def keyMiner(dic_, value):
  '''
  If you give a value, then this function gets the corresponding key, and the keys that call the key 
  i.e. the whole hierarchy
  Returns None if no value is found  
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
        # for key_, val_ in sorted(dict_.items(), key=lambda x: x[0]):    
        for key_, val_ in sorted(dict_.items(), key = lambda x: x[0] if ( isinstance(x[0], str) ) else str(x[0])  ):    
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
    dict_as_list = loadMultiYAML( path2yaml )
    yaml_dict    = getSingleDict4MultiDocs( dict_as_list )        
    k_list       = []
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
            # print( key, len(key) , target, len( target ), value  )
            if key == target:
                list_holder.append( value )
            else: 
                if isinstance(value, dict):
                    getValsFromKey(value, target, list_holder)
                elif isinstance(value, list):
                    for ls in value:
                        getValsFromKey(ls, target, list_holder)

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

def loadMultiYAML( script_ ):
    dicts2ret = []
    with open(script_, constants.FILE_READ_FLAG  ) as yml_content :
        try:
            for d_ in yaml.safe_load_all(yml_content) :
                # print(d_)
                # print('='*25)
                dicts2ret.append( d_ )
        except yaml.YAMLError as exc:
            print( constants.YAML_SKIPPING_TEXT  )    
        except UnicodeDecodeError as err_: 
            print( constants.YAML_SKIPPING_TEXT  )    
    return dicts2ret 


def getSingleDict4MultiDocs( lis_dic ):
    dict2ret = {} 
    key_lis  = []
    counter  = 0 
    for dic in lis_dic:
        # print(dic)
        # print('='*100)
        if( isinstance(dic, list) ): 
            '''
            to tackle YAMLs that are Ansible YAMLs and not K8S YAMLS
            '''
            dic = dic[0]
        '''
        the algorithm is if there are keys with similar names 
        then add a suffix to differentiate between keys for 
        multiple docs in a single YAML 
        '''
        # print(dic) 
        '''
        to handle Nones 
        '''
        if ( (dic is None) == False  ) and (isinstance(dic, dict ) ):
            keys4dic = list(dic.keys()) 
            for k_ in keys4dic: 
                if k_ in key_lis:
                    dict2ret[k_ + constants.DOT_SYMBOL + constants.YAML_DOC_KW + str(counter)] = dic[k_]
                else:
                    key_lis.append( k_ )
                    dict2ret[k_] = dic[k_] 
            counter += 1 
            # print(dict2ret) 
    return dict2ret


if __name__=='__main__':
    yaml_path = 'TEST_ARTIFACTS/docker.sock.yaml'
    dic_lis   = loadMultiYAML(yaml_path)
    # multi_yaml= 'TEST_ARTIFACTS/multi.doc.yaml' ## 2 dicts 
    # multi_yaml= 'TEST_ARTIFACTS/empty.yml'  ## 6 dicts 
    # dics      = loadMultiYAML(multi_yaml)
    # dic       = getSingleDict4MultiDocs( dic_lis )
    # print( dic.keys() )

    # print(dic)

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
    
    # invalid_yaml = 'TEST_ARTIFACTS/bootstrap.debian.yaml'
    # print(checkIfValidK8SYaml( invalid_yaml )  )
    
    multi_yaml  = 'TEST_ARTIFACTS/multi.doc.yaml'
    dics        = loadMultiYAML(multi_yaml)
    getSingleDict4MultiDocs( dics )

    # print(a_dict)