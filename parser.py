'''
Akond Rahman 
April 30, 2021 
Parser to file YAML files
'''

import yaml
import constants 
key_lis = []


def loadYAML( script_ ):
    dict2ret = {}
    with open(script_, constants.FILE_READ_FLAG  ) as yml_content :
        try:
            dict2ret =   yaml.safe_load(yml_content) 
        except yaml.YAMLError as exc:
            print(exc)    
    return dict2ret 

def keyMiner(dic_, value):
  '''
  If you give a value, then this function gets the corresponding key, and the keys that call the key 
  i.e. the whoel hierarchy 
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

if __name__=='__main__':
    dic = loadYAML('TEST_ARTIFACTS/dataimage.airflowimage.manifests.deployment.yaml')
    # getKeyRecursively( dic )
    # print('-'*100)
    # print( keyMiner(dic, '/usr/local/airflow/analytics' ) )

    temp_ = list (getValuesRecursively( dic  ) )
    print( len(temp_) )
