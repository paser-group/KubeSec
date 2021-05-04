'''
Akond Rahman 
May 03, 2021 
Code to detect security anti-patterns 
'''
import parser 

def scanForSecrets(yaml_d): 
    key_lis  = []
    parser.getKeyRecursively( yaml_d, key_lis )
    for key_ in key_lis:
        value_ = parser.getValFromKey( yaml_d, key_ )
        scanUserName( key_, value_  )


def scanSingleManifest( path_to_script ):
    checkVal = parser.checkIfValidK8SYaml( path_to_script )
    # print(checkVal) 
    if(checkVal):
        yaml_dict = parser.loadYAML( path_to_script )
        scanForSecrets( yaml_dict )



if __name__ == '__main__':
    test_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml'
    scanSingleManifest(test_yaml) 