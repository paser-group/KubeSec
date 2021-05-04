'''
Akond Rahman 
May 03, 2021 
Code to detect security anti-patterns 
'''
import parser 

def scanSingleManifest( path_to_script ):
    checkVal = parser.checkIfValidK8SYaml( path_to_script )
    print(checkVal) 


if __name__ == '__main__':
    test_yaml = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml'
    scanSingleManifest(test_yaml) 