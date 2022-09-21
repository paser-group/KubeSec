'''
Akond Rahman 
Sep 21, 2022
Source Code to Run Tool on All Kubernetes Manifests  
'''
import scanner 
import pandas as pd 
import constants

def getCountFromAnalysis(ls_):
    list2ret           = []
    for tup_ in ls_:
        within_sec_cnt = 0 
        dir_name       = tup_[0]
        script_name    = tup_[1]        
        within_secret  = tup_[2]  # a list of dicts: [unameDict, passwordDict, tokenDict]
        within_sec_cnt = len(within_secret[0]) + len( within_secret[1]  ) + len( within_secret[2] )
        '''
        ### format: ('data', 'password', ([], ['MTIzNAo='], [])) => (<rootKey>, <key>, <data_list>) ... need the list of the last tuple
        if isinstance( within_secret, tuple ):
            within_sec_cnt = len( within_secret[-1][1] )
            # print( script_name,  within_secret, within_sec_cnt, type(within_secret) ) 
        '''
        templa_secret  = tup_[3]       ### format: a list , we will not use this in dumping       
        taint_secret   = tup_[4]       ###   format: a list 
        privilege_dic  = tup_[5]
        http_dict      = tup_[6]        
        secuContextDic = tup_[7]
        nSpaceDict     = tup_[8]                
        absentResoDict = tup_[9]                 
        rollUpdateDic  = tup_[10]
        netPolicyDict  = tup_[11]                
        pidfDict       = tup_[12]                
        ipcDict        = tup_[13]                 
        dockersockDic  = tup_[14]
        hostNetDict    = tup_[15]                        
        cap_sys_dic    = tup_[16]
        host_alias_dic = tup_[17]
        allow_priv_dic = tup_[18]
        unconfined_dic = tup_[19]
        cap_module_dic = tup_[20]
        k8s_flag       = tup_[21]
        helm_flag      = tup_[22]

        list2ret.append(  ( dir_name, script_name, within_sec_cnt, len(taint_secret), len(privilege_dic), len(http_dict), len(secuContextDic), len(nSpaceDict), len(absentResoDict), len(rollUpdateDic), len(netPolicyDict), len(pidfDict), len(ipcDict), len(dockersockDic), len(hostNetDict), len(cap_sys_dic), len(host_alias_dic), len(allow_priv_dic), len(unconfined_dic), len(cap_module_dic) , k8s_flag, helm_flag  )  )
    return list2ret


if __name__ == '__main__':

    '''
    DO NOT DELETE ALL IN K8S_REPOS AS TAINT TRACKING RELIES ON BASH SCRIPTS, ONE OF THE STRENGTHS OF THE TOOL 
    '''
    # ORG_DIR         = '/Users/arahman/K8S_REPOS/GITHUB_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_GITHUB_OUTPUT.csv'

    # ORG_DIR         = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_GITLAB_OUTPUT.csv'


    # ORG_DIR         = '/Users/arahman/K8S_REPOS/BRINTO_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_BRINTO_OUTPUT.csv'

    # ORG_DIR         = '/Users/arahman/K8S_REPOS/TEST_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_TEST_OUTPUT.csv'

    content_as_ls   = scanner.runScanner( ORG_DIR )
    df_all          = pd.DataFrame( getCountFromAnalysis( content_as_ls ) )

    df_all.to_csv( OUTPUT_FILE_CSV, header= constants.CSV_HEADER , index=False, encoding= constants.CSV_ENCODING ) 




