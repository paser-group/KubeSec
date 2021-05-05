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
YAML_SKIPPING_TEXT           = ''
YAML_EXTENSION               = 'yaml'
YML_EXTENSION                = 'yml'
TEMPLATES_DIR_KW             = '/templates/'
DOT_SYMBOL                   = '.'
HELM_VALUE_KW                = 'Values' 
VALU_FROM_KW                 = 'valueFrom'

SECRET_USER_LIST             = ['user']
SECRET_PASSWORD_LIST         = ['pwd', 'password', 'passwd', 'admin_pass'] 
FORBIDDEN_USER_NAMES         = ['domain', 'group', 'mode', 'schema', 'email', '_tenant', '_tree_dn', '_attribute', '_emulation', '_allow_', '_emulation', '%(', '_age'] 
FORBIDDEN_PASS_NAMES         = ['_auth', '_file', '_path', '_age', '_content', '_hash'] 
INVALID_SECRET_CONFIG_VALUES = [ ':undef', '[]', '/',  'hiera', 'unset', 'undefined', '%(' ]  
LEGIT_KEY_NAMES              = ['crt', 'key']
VALID_KEY_STRING             = ['-----BEGIN CERTIFICATE-----', '-----BEGIN RSA PRIVATE KEY-----']
