'''
Akond Rahman 
May 04, 2021 
Construct taint graphs based on weakness types 
'''
import constants
import parser 
import os 
from itertools import combinations

def getYAMLFiles(path_to_dir):
    valid_  = [] 
    for root_, dirs, files_ in os.walk( path_to_dir ):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if(os.path.exists(full_p_file)):
             if (full_p_file.endswith( constants.YAML_EXTENSION  ) or full_p_file.endswith( constants.YML_EXTENSION  )  ):
               valid_.append(full_p_file)
    return valid_ 

def constructHelmString(hiera_tuple): 
    str2ret  = constants.YAML_SKIPPING_TEXT 
    upper_key, key, _ = hiera_tuple 
    if ( upper_key != key  ):
        str2ret =   constants.DOT_SYMBOL +  constants.HELM_VALUE_KW + constants.DOT_SYMBOL + upper_key + constants.DOT_SYMBOL + key 
    return str2ret 

def getHelmTemplateContent( templ_dir ):
    template_content_dict = {}
    template_yaml_files =  getYAMLFiles( templ_dir )
    for template_yaml_file in template_yaml_files:
        value_as_str      = parser.readYAMLAsStr( template_yaml_file )
        template_content_dict[template_yaml_file] = value_as_str
    return template_content_dict 


def getMatchingTemplates(path2script, hierarchy_ls):
    templ_list = [] 
    template_content_dict, helm_string_list = {}, []
    templateDirOfHelmValues = os.path.dirname( path2script )  + constants.TEMPLATES_DIR_KW 
    if (os.path.exists( templateDirOfHelmValues )  ):
        template_content_dict = getHelmTemplateContent( templateDirOfHelmValues )
    for hiera_ in hierarchy_ls:
        helm_string_list.append(   constructHelmString( hiera_  ) )
    for template_file, template_string in template_content_dict.items():
        for helm_string in helm_string_list:
            if helm_string != constants.YAML_SKIPPING_TEXT : 
                if helm_string in template_string: 
                    match_count = template_string.count( helm_string  )
                    for _ in range(match_count):
                        templ_list.append( (template_file, helm_string ) )
    return templ_list

def getValidTaints(  lis_template_matches ): 
    '''
    provides a mapping between the key where the secret occurred and the 
    files that re affected by teh key 
    '''
    taint_lis  = []
    for match in lis_template_matches:
        script_name, helm_string = match 
        inceptor = helm_string.split( constants.DOT_SYMBOL )[-1]
        taint_lis.append( (inceptor, script_name) )
    return taint_lis 



def mineSecretGraph( path2script, yaml_dict , secret_dict ):
    within_match_head = None 
    hierarchy_list = []
    for k_, v_ in secret_dict.items():
        for tup_item in v_:
            for value in tup_item:
                hierarchy_keys = parser.keyMiner(yaml_dict, value)
                hierarchy_keys = [x_ for x_ in hierarchy_keys if x_ != constants.YAML_SKIPPING_TEXT ] 
                compo_hiera_keys = [ constants.DOT_SYMBOL.join(str_) for str_ in combinations( hierarchy_keys , 2 )] ## take 2 strings at a time 
                # print(compo_hiera_keys) 
                for h_key in hierarchy_keys:
                    hierarchy_list.append( (h_key, k_ , v_) )
                '''
                the purpose of composite hierarchy keys is to get nested values that are referenced 
                takign 2 strings at a time 
                '''
                for compo_h_key in compo_hiera_keys:
                    hierarchy_list.append( ( compo_h_key, k_, v_  ) )
    
    templ_match_list = []
    if( parser.checkIfValidHelm(path2script) ):                    
        templ_match_list = getMatchingTemplates( path2script, hierarchy_list  )
    else:
        if( len(hierarchy_list) > 0 ):
            '''
            check if valueFrom exists 
            '''
            if constants.VALU_FROM_KW not in hierarchy_list: 
                    within_match_head = hierarchy_list[0]
    valid_taints = getValidTaints( templ_match_list ) 
    # print( templ_match_list ) 
    return within_match_head, templ_match_list, valid_taints 





# if __name__=='__main__':