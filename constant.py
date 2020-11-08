import os



# Pod Security Policy
# Network Security Polic0.5

# Function Parameter

return_key = 'key'
return_value = 'value'
kind = 'kind'

#NO TLS

http_no_tls = "http:"

### RBAC authorization

rbac_api_version = 'rbac.authorization.k8s.io/v1'
rbac_object_role = 'Role'
rbac_role_binding = 'RoleBinding'
rbac_object_cluster_role = 'ClusterRole'
rbac_cluster_role_binding = 'ClusterRoleBinding'

#Network Policy

network_policy_api_version = 'networking.k8s.io/v1'
network_policy_object = 'NetworkPolicy'
network_policy_ingress = 'Ingress'
network_policy_egress = 'egress'

#Pod Policy
pod = 'Pod'
pod_policy_security_context = 'securityContext'

#Limit CPU, memory usage

limit_resources = 'resources'
limit_memory = 'limits'
limit_requests = 'requests'

#default_namespace
namespace_key = 'namespace'
namespace_value_default = 'default'

#hard-coded password
user_only  = 'user'
user_name = 'username'
password = 'password'
password_key = 'key'
empty_string = ''