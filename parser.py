'''
Akond Rahman 
April 30, 2021 
Parser to file YAML files
'''
import sys
import ruamel.yaml 
from ruamel.yaml.scanner import ScannerError
import json
#import jsonpath_rw as jp
# import yaml
import constants 
import pathlib as pl
import re
import subprocess
import os

#update basepath
base_path = r" "

key_jsonpath_mapping = {}

    
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
    #print(list2hold)               

def getValuesRecursively(  dict_   ) :
    '''
    gives you ALL values in a regular/nested dictionary 
    '''
    if  isinstance(dict_, dict) :
        for val_ in dict_.values():
            yield from getValuesRecursively(val_) 
            #print(val_)
    elif isinstance(dict_, list):
        for v_ in dict_:
            yield from getValuesRecursively(v_)
            #print(v_)
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

# This function checks whether our parser throws an exception for reading the YAML file. 
def checkParseError( path_script ):
    flag = True
    with open(path_script, constants.FILE_READ_FLAG) as yml:
        yaml = ruamel.yaml.YAML()
        try:
            for dictionary in yaml.load_all(yml):
                pass
        except ruamel.yaml.parser.ParserError as parse_error:
            flag = False
            print(constants.YAML_SKIPPING_TEXT)           
        except ruamel.yaml.error.YAMLError as exc:
            flag = False
            print( constants.YAML_SKIPPING_TEXT  )    
        except UnicodeDecodeError as err_: 
            flag = False
            print( constants.YAML_SKIPPING_TEXT  )
    return flag

def loadMultiYAML( script_ ):
    dicts2ret = []  
    with open(script_, constants.FILE_READ_FLAG  ) as yml_content :
        yaml = ruamel.yaml.YAML()
        yaml.default_flow_style = False      
        try:
            for d_ in yaml.load_all(yml_content) :                
                # print('='*25)
                # print(d_)
                dicts2ret.append( d_ )
        except ruamel.yaml.parser.ParserError as parse_error:
            print(constants.YAML_SKIPPING_TEXT)           
        except ruamel.yaml.error.YAMLError as exc:
            print( constants.YAML_SKIPPING_TEXT  )    
        except UnicodeDecodeError as err_: 
            print( constants.YAML_SKIPPING_TEXT  )
        
        path = find_json_path_keys(dicts2ret)
        #print(dicts2ret)
        no_exception = checkParseError(script_)
        if no_exception:
            # for debugging purposes

            path = find_json_path_keys(dicts2ret) #, key_jsonpath_mapping
            # print(path)
            updated_path = update_json_paths(path)
            # print(updated_path)
            # print("-------------------HERE IS THE MAPPING---------------")
            # for key in key_jsonpath_mapping:
            #     print(key, "-->", key_jsonpath_mapping[key],  "-->", print(type(key_jsonpath_mapping[key])) )
            # print("----LINE----")
            # line = show_line_for_paths(script_, 'serviceName') #imagePullSecrets
            # print(line)
            # print("----JSON Validated----")
            # print(type(dicts2ret))
            # for d in dicts2ret:
            #     print(type(d))
                
        #print(dicts2ret)
    return dicts2ret


def count_initial_comment_line (filepath):
    initial_comment_line = 0
    comment_found = False
    # calculates initial line before the comments begin in the file such as empty lines, '---'
    with open(filepath, constants.FILE_READ_FLAG  ) as yamlfile :       
        textfile = yamlfile.read()
        for line in textfile.split('\n'):
            if line.startswith('#'):
                comment_found = True
                #print(line)
                initial_comment_line+=1
            elif not line:
                #print(line)
                if(comment_found is False):
                    initial_comment_line +=1
            elif line.startswith('---'):
                if(comment_found is False):
                    initial_comment_line +=1
            else:
                break
        if comment_found is False:
            initial_comment_line = 0
    return initial_comment_line


"""This function takes input as ruamel yaml ordered dictionary (commentedKeyMap), 
the parent_path (root jsonpath), paths(additional paths) parameters are optional 

This function returns jsonpath for each key in the yaml file and also populates key_jsonpath_mapping dictionary"""

def find_json_path_keys(json_file, parent_path='', paths=None):
    #key_jsonpath_mapping = {}
    # print(type(json_file))

    """The following regular expressions are used to remove elements to construct a VALID json path"""

    # app.kubernetes.io/release --> "app.kubernetes.io/release"
    regex_key_dot = re.compile("([^\s\.]+[.][\S]+)")
    # app.kubernetes.io/release --> "app*kubernetes*io*release"
    regex_special_character_removal = re.compile("[^A-Za-z0-9]+")
    #[3].metadata.name --> .metadata.name
    regex_remove_initial_index = re.compile("^/?(\[)([0-9])+(\])")
    
    if paths is None:
        paths = []   
    if isinstance(json_file, dict):
        for key, value in json_file.items():
        
            """The following condition is used if there is any key: value mapping like jinja format sych as key: {{value}}. 
               This is a temporary fix to handle the case"""
            if (isinstance(key,ruamel.yaml.comments.CommentedKeyMap) and value is None) or isinstance(key,int):
                pass
            else:
                if regex_key_dot.match(key):              
                    str = regex_special_character_removal.sub("*",key)
                    path_withindex = f"{parent_path}.{str}"
                    path = regex_remove_initial_index.sub('',path_withindex)
                    #print("NOW IN DOT, the path--->",path)
                    #key_jsonpath_mapping[key] =path
                    if key_jsonpath_mapping.get(key) is None:
                        key_jsonpath_mapping[key] = []
                        key_jsonpath_mapping[key].append(path)
                        #print(key_jsonpath_mapping)
                    else:
                        '''Exckude the path if it is already present in the key_jsonpath_mapping dictionary. '''
                        if path not in key_jsonpath_mapping[key]:
                            key_jsonpath_mapping[key].append(path)
                        # print("DOT Keys -->",key_jsonpath_mapping[key])
                                    
                    paths.append(path)
                    find_json_path_keys(value, parent_path=path, paths=paths)
                else:
                    path_withindex = f"{parent_path}.{key}"
                    path = regex_remove_initial_index.sub('',path_withindex)
                    #print("NOW IN REGULAR, the path--->",path)
                    if key_jsonpath_mapping.get(key) is None:
                        key_jsonpath_mapping[key] = []
                        key_jsonpath_mapping[key].append(path)
                        #print(key_jsonpath_mapping)
                    else:
                        key_jsonpath_mapping[key] = path
                        #print(key_jsonpath_mapping) 
                    #key_jsonpath_mapping[key] =path
                    #print(key_jsonpath_mapping)
                    paths.append(path)          
                    find_json_path_keys(value, parent_path=path, paths=paths)
    elif isinstance(json_file, list):
        for index, value in enumerate(json_file):
            path_withindex = f"{parent_path}[{index}]"
            path = regex_remove_initial_index.sub('',path_withindex)
            paths.append(path)
            find_json_path_keys(value, parent_path=path, paths=paths)
    return paths 
    

""""The following function is used to update the json path in the key_jsonpath_mapping dictionary.
Useful in MultiYaml file format but redundant in single yaml Need to merge with the above function """

def update_json_paths (paths):
    #[3].metadata.name --> .metadata.name
    regex_remove_initial_index = re.compile("^/?(\[)([0-9])+(\])")
    json_path =[]
    updated_paths =[]
    remove = ''    
    for path in paths:            
        path_remove_initial_index = regex_remove_initial_index.sub('',path)
        if(path_remove_initial_index != remove):
            json_path.append(path_remove_initial_index)
            updated_paths.append(path_remove_initial_index)        
    return json_path
    

def show_line_for_paths(  filepath, key): #key_jsonpath_mapping is a global dictionary
    line_number = count_initial_comment_line(filepath)
    """
    input: provide  JSON_PATH dictionary and the key
    output:  line of appearance of the key in the file
    """
    env_PATH = r"C:\ProgramData\Chocolatey\bin"
    lines = []
    adjusted_lines = []
    print("This is the mapping for the Key",key,"--->",key_jsonpath_mapping[key]) 
    # for k in key_jsonpath_mapping:
    #     print("Key--->",k, "Value--->",key_jsonpath_mapping[k])
    if key_jsonpath_mapping.get(key) is not None:
        if isinstance(key_jsonpath_mapping[key], list):
            for i in key_jsonpath_mapping[key]:
                #print(i)
                yq_parameter = i + " | key | line "
                #print(yq_parameter)
                result = subprocess.check_output(["yq", yq_parameter , filepath], universal_newlines=True)
                #result = subprocess.run(["C:/ProgramData/Chocolatey/bin/yq ",yq_parameter, filepath], shell = True, text= True, capture_output= True,cwd= env_PATH ) #env= {'PATH' : env_PATH}
                #env= {'PATH': 'C:\ProgramData\Chocolatey\bin'}
                #print(result)
                output = result.split("---")
                for line in output:
                    line.replace("\n","")
                    line_convert = int(line)
                    print(type(line_convert))
                    if(line_convert >0):
                        line_number = line_convert + count_initial_comment_line(filepath)
                        lines.append(line_number)
                #print(lines)
        else:
            yq_parameter = key_jsonpath_mapping[key]+ " | key | line "
            result = subprocess.check_output(["yq", yq_parameter , filepath], universal_newlines=True)
                #result = subprocess.run(["C:/ProgramData/Chocolatey/bin/yq ",yq_parameter, filepath], shell = True, text= True, capture_output= True,cwd= env_PATH ) #env= {'PATH' : env_PATH}
                #env= {'PATH': 'C:\ProgramData\Chocolatey\bin'}
                
            output = result.split("---")
            for line in output:
                line.replace("\n","")
                line_convert = int(line)
                #print(type(line_convert))
                if(line_convert >0):
                    line_number = line_convert + count_initial_comment_line(filepath)
                    lines.append(line_number)
                #print(lines)
                   
    return lines



def getSingleDict4MultiDocs( lis_dic ):
    dict2ret = {} 
    key_lis  = []
    counter  = 0 
    for dic in lis_dic:
        # print(dic)
        # print('='*100) dic = dic[0]
        # print("----DIC---")
        # print(dic)
        # print("----DIC---")
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

        """ the algorithm doesn't check the keys with suffix for misconfigurations"""

        # if (dic is not None) and isinstance(dic, dict):
        #     keys4dic = list(dic.keys())
        #     for k_ in keys4dic:
        #         dict2ret[k_] = dic[k_]

        if ( (dic is None) == False  ) and (isinstance(dic, dict ) ):
            keys4dic = list(dic.keys()) 
            for k_ in keys4dic: 
                if k_ in key_lis:
                    dict2ret[k_ + constants.DOT_SYMBOL + constants.YAML_DOC_KW + str(counter)] = dic[k_]
                else:
                    key_lis.append( k_ )
                    dict2ret[k_] = dic[k_] 
            counter += 1 
            #print(dict2ret) 
    # print("-----In Single Dict 4 multiple docs---")
    # yaml = ruamel.yaml.YAML()
    # yaml.dump(dict2ret, sys.stdout)
    # print("-----")
        
    return dict2ret


if __name__=='__main__':
    yaml_path = pl.Path(base_path,'test.yaml')
    dic_lis   = loadMultiYAML(yaml_path)