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

#### Category-4.3 Log monitor
```
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
#### Category-11.1 Insecure metadata of Kubernetes cluster
Sample code snippets:




