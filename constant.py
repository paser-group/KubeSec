import os



# Rolling Update
pod_replicas = 'replicas'
pod_strategy = 'strategy'
pod_strategy_type = 'type'
pod_strategy_rolling_update = 'rollingUpdate'

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
network_policy_ingress_object = 'Ingress'
network_policy_egress_object = 'Egress'
network_policy_ingress = 'ingress'
network_policy_egress = 'egress'
network_ingress_enabled = 'enabled'

#Pod Policy
pod_spec = 'spec'
pod_container = 'container'
pod = 'Pod'
pod_security_policy_object = 'PodSecurityPolicy'

pod_policy_security_context = 'securityContext'


container_privilege_escalation = 'allowPrivilegeEscalation'
container_privilege_given = 'privileged'

container_linux_security = 'seLinuxOptions'
container_seccomp_security = 'seccompProfile'


# Will Explore later
container_user = 'runAsUser'
container_user_group = 'runAsGroup'

user_permission_pod = '1000'
user_permission_container = '2000'


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