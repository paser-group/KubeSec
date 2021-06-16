'''
Akond Rahman 
April 30, 2021 
Placeholder for constants for KubeTaint
'''

FILE_READ_FLAG               = 'r'
TEMP_KEY_NAME                = 'TEMP_KEY_DUMMY'
API_V_KEYNAME                = 'apiVersion'
KIND_KEY_NAME                = 'kind'
QUOTE_SYMBOL                 = "'"
K8S_FORBIDDEN_KW_LIST        = ['CustomResourceDefinition', 'OpenDataHub', 'List', 'ClusterServiceVersion', 'ClusterIssuer']
HELM_KW                      = 'helm'
CHART_KW                     = 'chart'
VALUE_KW                     = 'values'
SERVICE_KW                   = 'services'
INGRESS_KW                   = 'k8s-ingress'
HELM_DEPLOY_KW               = 'deploy' 
YAML_SKIPPING_TEXT           = ''
YAML_EXTENSION               = 'yaml'
YML_EXTENSION                = 'yml'
TEMPLATES_DIR_KW             = '/templates/'
DOT_SYMBOL                   = '.'
HELM_VALUE_KW                = 'Values' 
VALU_FROM_KW                 = 'valueFrom'
PRIVI_KW                     = 'privileged'
SECU_CONT_KW                 = 'securityContext'
CONTAINER_KW                 = 'containers'
SPEC_KW                      = 'spec'
DEAMON_KW                    = 'DaemonSet' 
HTTP_KW                      = 'http://'
CONFIGMAP_KW                 = 'ConfigMap'
SLASH_SYMBOL                 = '/'
SH_EXTENSION                 = 'sh'
WWW_KW                       = 'www'
ORG_KW                       = 'org'
CONFIG_KW                    = 'configuration'
DEPLOYMENT_KW                = 'Deployment' 
POD_KW                       = 'Pod'
DEFAULT_KW                   = 'default' 
K8S_SERVICE_KW               = 'Service'
K8S_APP_KW                   = 'app'
LIMITS_KW                    = 'limits'
CPU_KW                       = 'cpu'
MEMORY_KW                    = 'memory' 
STRATEGY_KW                  = 'strategy'
ROLLING_UPDATE_KW            = 'rollingUpdate'
VAL_ROLLING_UPDATE_KW        = 'RollingUpdate'
NET_POLICY_KW                = 'NetworkPolicy'
POD_SELECTOR_KW              = 'podSelector'
MATCH_LABEL_KW               = 'matchLabels'
ANLYZING_KW                  = 'Analyzing... '
SIMPLE_DASH_CHAR             = '-----'


SECRET_USER_LIST             = ['user']
SECRET_PASSWORD_LIST         = ['pwd', 'password', 'passwd', 'admin_pass'] 
FORBIDDEN_USER_NAMES         = ['domain', 'group', 'mode', 'schema', 'email', '_tenant', '_tree_dn', '_attribute', '_emulation', '_allow_', '_emulation', '%(', '_age'] 
FORBIDDEN_PASS_NAMES         = ['_auth', '_file', '_path', '_age', '_content', '_hash'] 
INVALID_SECRET_CONFIG_VALUES = [ ':undef', '[]', '/',  'hiera', 'unset', 'undefined', '%(' ]  
LEGIT_KEY_NAMES              = ['crt', 'key']
VALID_KEY_STRING             = ['-----BEGIN CERTIFICATE-----', '-----BEGIN RSA PRIVATE KEY-----']


CSV_HEADER                   = ['DIR', 'YAML_FULL_PATH', 'UNFILTERED_SECRET', 'VALID_TAINT_SECRET', 'LEAST_PRIVIL', 'INSECURE_HTTP', 'NO_SECU_CONTEXT', 'NO_DEFAULT_NSPACE', 'NO_RESO', 'NO_ROLLING_UPDATE', 'NO_NETWORK_POLICY']
CSV_ENCODING                 = 'latin-1'
