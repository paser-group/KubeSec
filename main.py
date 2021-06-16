'''
Akond Rahman 
May 31, 2021
Source Code to Run Tool on All Scripts 
'''
import scanner 
import pandas as pd 
import constants

def getCountFromAnalysis(ls_):
    list2ret           = []
    for tup_ in ls_:
        dir_name       = tup_[0]
        script_name    = tup_[1]        
        within_secret  = tup_[2]
        templa_secret  = tup_[3]                
        taint_secret   = tup_[4]         
        privilege_dic  = tup_[5]
        http_dict      = tup_[6]        
        secuContextDic = tup_[7]
        nSpaceDict     = tup_[8]                
        absentResoDict = tup_[9]                 
        rollUpdateDic  = tup_[10]
        netPolicyDict  = tup_[11]                

        print( within_secret )

        list2ret.append(  ( dir_name, script_name, len(privilege_dic), len(http_dict), len(secuContextDic), len(nSpaceDict), len(absentResoDict), len(rollUpdateDic), len(netPolicyDict)  )  )
    return list2ret



if __name__ =='__main__':
    # ORG_DIR         = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V1_GITLAB_OUTPUT.csv'

    ORG_DIR         = '/Users/arahman/K8S_REPOS/TEST_REPOS/'
    OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V1_TEST_OUTPUT.csv'

    content_as_ls   = scanner.runScanner( ORG_DIR )
    df_all          = pd.DataFrame( getCountFromAnalysis( content_as_ls ) )

    # df_all.to_csv( OUTPUT_FILE_CSV, header= constants.CSV_HEADER , index=False, encoding= constants.CSV_ENCODING ) 



