# Qualitative Analysis 

## What insecure practices are observed in Kubernetes?

### Category-1: Authentication and Authorization

#### Category-1.1: Anonymous access to K8s server

This is done at kube-apiserver.yaml file at the master node by properly setting the flags.


Sample code snippets: 

#### Category-1.2 Default Authorization mode enabled 

The RBAC API declares four kinds of Kubernetes object: `Role`, `ClusterRole`, `RoleBinding` and `ClusterRoleBinding`.   
Reference: https://kubernetes.io/docs/reference/access-authn-authz/rbac/

Check for ```Kind: RBAC_OBJECT(any of the 4 above)```   
Case 1: What if the namespace not specified?  
Case 2: What if inside a K8s repository there is no yaml file for RBAC? 

Sample code snippets:   
For case 1: No namespace specified 

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: unprivileged-rbac-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: unprivileged-rbac
subjects:
- kind: ServiceAccount
  name: unprivileged-user
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: default-psp
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: unprivileged-psp
subjects:
- kind: ServiceAccount
  name: default

```


### Category-2: Implementing Kubernetes Specific security policies

#### Category-2.1 Network Specific Policies

By default, pods are non-isolated; they accept traffic from any source. Pods become isolated by having a NetworkPolicy that selects them.

Reference:
https://kubernetes.io/docs/concepts/services-networking/network-policies/
https://github.com/ahmetb/kubernetes-network-policy-recipes   
CNCF Talk: https://www.youtube.com/watch?v=3gGpMmYeEO8   

I found 1 or 2 repositories that uses NetworkPolices. Typically a K8s cluster using Network Policy should be like the snippet.
https://kubernetes.io/docs/concepts/services-networking/network-policies/#networkpolicy-resource
``` 
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: ...
  namespace: ...
spec:
  podSelector:
    matchLabels:
        ....
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - ipBlock:
    - namespaceSelector:
        matchLabels:
          project: YYYY
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: XXXX
  egress:
  - to:
    - ipBlock:
        cidr: 10.0.0.0/24
    ports:
    - protocol: TCP
      port: XXXX
```


Sample code snippets: This is a rare example
```
networkPolicy:
  ## Enable creation of NetworkPolicy resources.
  ##
  enabled: false
```
source: `GITLAB_REPOS/justin@kubernetes/src/services/postgres/values-production.yaml`


#### Category-2.2 Pod Specific Policies
 
reference: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
`securityContext` field is missing from container manifest file for both `Pod` and `Container`  
Sample code snippets:
```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: pvc-name
```
Source: GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-volumes/pods-with-volume.yaml

#### Category-2.3 Generic Policies
Sample code snippets: 


### Category-3 Vulnerability Scanning
#### Category-3.1 Vulnerable container
Sample code snippets: 

#### Category-3.2 Public or Untrusted registry 
Reference: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/

Sample code snippets: Use of public image instead of private registry 
```

apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: nginx-app
spec:
  containers:
    - name: nginx-container
      image: nginx

```
#### Category-3.3 Vulnerable code and images
Sample code snippets: 


### Category-4 Logging 
#### Category-4.1 Alert configurations
#### Category-4.2 Log setup at application level, pod and cluster level
Reference: https://kubernetes.io/docs/tasks/debug-application-cluster/audit/
> An audit policy file can be passed a file with the policy to kube-apiserver using the --audit-policy-file

Check for `audit.k8.io/v1`  
Sample audit policy file:
```
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
```
#### Category-4.3 Log monitor
> I found third party alert configuration and monitoring support for kubernetes https://github.com/prometheus-operator/prometheus-operator/

Sample code: Using `Promethus` object
```
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: example
    ... 
```

Sample code: Using `PrometheusRule` object
```
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata: ... 
```

### Category-5 Namespace Separation
#### Category-5.1 Use of "default" namespace 
Sample code snippets: 
```
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: airflow-deployment
  namespace: default
 ```
  
### Category-6 Encrypt and restrict etcd 
#### Category-6.1 Unrestricted etcd access
#### Category-6.2 Unencrypted etcd server secrets
reference: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/  
Check kubernetes object encryption configuration object.
```
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
    - secrets
    providers:
        ... 
```
I found NO USE of encryption configuration in the sample 44 ` Gitlab` and 50 `github` repositories.  
EXTRA: Before and after encryption configuration https://www.youtube.com/watch?v=UYUbuL2WYn8
### Category-7 Continuous Update
#### Category-7.1 Outdated K8s version 
#### Category-7.2 Not using rolling update strategy 
I found some unofficial reference for using `rolling update` strategy   and found instances of using rolling update in sample repositories as well but I did not find any official reference.

Unofficial reference: https://blog.container-solutions.com/kubernetes-deployment-strategies  
Code snippet:
```
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2        # how many pods we can add at a time
      maxUnavailable: 0  # maxUnavailable define how many pods can be unavailable
                         # during the rolling update
```

### Category-8 Limit CPU, memory usage
Guideline: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/
#### Category-8.1 Default Memory Requests and Limits for a Namespace
Check `LimitRange` and `ResourceQuota` object or for pod check the following type of code snippet
```
containers:
  - name: zzzzz
    image: yyyy
    resources:
      limits:
        memory: "xGi"
      requests:
        memory: "yGi"
```  
Sample code snippets: No resource limit 
```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: busybox-container
      image: busybox
      volumeMounts:
        - name: config-dir
          mountPath: /etc/config
  volumes:
    - name: config-dir
      configMap:
        name: bb-configmap

```

### Category-9 Enable SSL/TLS support 
#### Category-9.1 Missing SSL/TLS support for communication between K8s components
I could not find any way check certificates for secure communication between services.
Sample code snippets: 
Use of `http://` with out TLS
```
kind: ConfigMap
apiVersion: v1
metadata:
  name: room-reservation-service
data:
  application.yml: |-
    server:
      port: 8080
    spring:
      cloud:
        kubernetes:
          discovery:
            service-labels:
              group: ca.zhoozhoo.spring.cloud.kubernetes
      zipkin:
        baseUrl: http://host.docker.internal:9411
      security:
        oauth2:
          resourceserver:
            jwt:
              issuer-uri: http://host.docker.internal:8180/auth/realms/spring-cloud-gateway-realm
    management:
      endpoint:
        health:
          enabled: true
        info:
          enabled: true
```
source: ` GITHUB_REPOS/spring-cloud-kubernetes-examples/spring-cloud-kubernetes-room-reservation-service/room-reservation-service-configmap.yml`
### Category-10 Separate sensitive workloads 
#### Category-10.1 Not separating sensitive workloads to run on a dedicated set of machines
Sample code snippets:

### Category-11 Secure metadata access
Reference: https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/#restricting-cloud-metadata-api-access
> When running Kubernetes on a cloud platform limit permissions given to instance credentials, use network policies to restrict pod access to the metadata API, and avoid using provisioning data to deliver secrets.


#### Category-11.1 Insecure metadata of Kubernetes cluster
Sample code snippets:
##PREVIOUS CATEGORIES 
### Category-12 Hardcoded secret
Although this events are quite rare.  
Sample code snippets:  
source:  GITLAB_REPOS/justin@kubernetes/src/services/nextcloud/values.yaml

```
## Official nextcloud image version
## ref: https://hub.docker.com/r/library/nextcloud/tags/
##
image:
  repository: nextcloud
  tag: 15.0.2-apache
  pullPolicy: IfNotPresent
  # pullSecrets:
  #   - myRegistrKeySecretName

nameOverride: ""
fullnameOverride: ""

# Number of replicas to be deployed
replicaCount: 1

## Allowing use of ingress controllers
## ref: https://kubernetes.io/docs/concepts/services-networking/ingress/
##
ingress:
  enabled: true
  annotations: {}

nextcloud:
  host: nextcloud.corp.justin-tech.com
  username: admin
  password: changeme


internalDatabase:
  enabled: true
  name: nextcloud


##
## External database configuration
##
externalDatabase:
  enabled: false

  ## Database host
  host:

  ## Database user
  user: nextcloud

  ## Database password
  password:

  ## Database name
  database: nextcloud

##
## MariaDB chart configuration
##
mariadb:
  ## Whether to deploy a mariadb server to satisfy the applications database requirements. To use an external database set this to false and configure the externalDatabase parameters
  enabled: true

  db:
    name: nextcloud
    user: nextcloud
    password: changeme

  ## Enable persistence using Persistent Volume Claims
  ## ref: http://kubernetes.io/docs/user-guide/persistent-volumes/
  ##
  persistence:
    enabled: true
    storageClass: "nfs-client"
    accessMode: ReadWriteOnce
    size: 8Gi

service:
  type: ClusterIP
  port: 8080
  loadBalancerIP: nil


## Enable persistence using Persistent Volume Claims
## ref: http://kubernetes.io/docs/user-guide/persistent-volumes/
##
persistence:
  enabled: true
  ## nextcloud data Persistent Volume Storage Class
  ## If defined, storageClassName: <storageClass>
  ## If set to "-", storageClassName: "", which disables dynamic provisioning
  ## If undefined (the default) or set to null, no storageClassName spec is
  ##   set, choosing the default provisioner.  (gp2 on AWS, standard on
  ##   GKE, AWS & OpenStack)
  ##
  storageClass: "nfs-client"

  ## A manually managed Persistent Volume and Claim
  ## Requires persistence.enabled: true
  ## If defined, PVC must be created manually before volume will be bound
  # existingClaim:

  accessMode: ReadWriteOnce
  size: 8Gi

resources: {}
  # We usually recommend not to specify default resources and to leave this as a conscious
  # choice for the user. This also increases chances charts run on environments with little
  # resources, such as Minikube. If you do want to specify resources, uncomment the following
  # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
  # limits:
  #  cpu: 100m
  #  memory: 128Mi
  # requests:
  #  cpu: 100m
  #  memory: 128Mi

nodeSelector: {}

tolerations: []

affinity: {}


```




