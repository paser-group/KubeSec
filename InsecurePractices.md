# Qualitative Analysis 

## What insecure practices are observed in Kubernetes?

### Category-1: Authentication and Authorization

#### Category-1.1: Anonymous access to K8s server

Sample code snippets: 

#### Category-1.2 Default Authorization mode enabled 

Sample code snippets

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

#### Category-3.2 Untrusted registry 
Sample code snippets: 

#### Category-3.3 Vulnerable code and images
Sample code snippets: 


### Category-4 Logging 
#### Category-4.1 Alert configurations
#### Category-4.2 Log setup at application level, pod and cluster level
#### Category-4.3 Log monitor

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

### Category-7 Continuous Update
#### Category-7.1 Outdated K8s version 
#### Category-7.2 Not using rolling update strategy

### Category-8 Limit CPU, memory usage
Guideline: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/
#### Category-8.1 Default Memory Requests and Limits for a Namespace
Sample code snippets: 

#### Category-8.2 Default CPU Requests and Limits for a Namespace
Sample code snippets: 

#### Category-8.3 Not configuring Minimum and Maximum Memory Constraints for a Namespace
Sample code snippets: 

#### Category-8.4 Not configuring Minimum and Maximum CPU Constraints for a Namespace
Sample code snippets: 

#### Category-8.5 Not configuring Memory and CPU Quotas for a Namespace
Sample code snippets: 

#### Category-8.6 Not configuring a Pod Quota for a Namespace
Sample code snippets: 


### Category-9 Enable SSL/TLS support 
#### Category-9.1 Missing SSL/TLS support for communication between K8s components
Sample code snippets: 

### Category-10 Separate sensitive workloads 
#### Category-10.1 Not separating sensitive workloads to run on a dedicated set of machines
Sample code snippets:

### Category-11 Secure metadata access
#### Category-11.1 Insecure metadata of Kubernetes cluster
Sample code snippets:




