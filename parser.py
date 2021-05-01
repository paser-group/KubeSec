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
    with open(script_, constants.file_read_flag  ) as yml_content :
        try:
            dict2ret =   yaml.safe_load(yml_content) 
        except yaml.YAMLError as exc:
            print(exc)    
    return dict2ret 

def keyMiner(dic_, value):
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

'''
def getKeyRecursively(  dict_, depth_ = 0 , parent = 'ROOT' ) :
    if  isinstance(dict_, dict) :
        # for key_, val_ in dict_.items():       
        for key_, val_ in sorted(dict_.items(), key=lambda x: x[0]):              
            if isinstance(val_, dict):
                print(key_, depth_, parent)
                depth_ += 1 
                parent  = key_     
                getKeyRecursively( val_, depth_, parent ) 
                print('*'*50)
            elif isinstance(val_, list):
                for listItem in val_:
                        if( isinstance( listItem, dict ) ):
                            print(key_, depth_, parent )  
                            depth_ += 1 
                            getKeyRecursively( listItem, depth_, parent )     
                print('='*50)
            else: 
                print( key_, depth_, parent )
'''

            

if __name__=='__main__':
    dic = loadYAML('TEST_ARTIFACTS/dataimage.airflowimage.manifests.deployment.yaml')
    # getKeyRecursively( dic )
    # print('-'*100)
    # print( keyMiner(dic, '/usr/local/airflow/analytics' ) )

