# Qualitative Analysis 

## What insecure practices are observed in Kubernetes?

### Category-1: Authentication and Authorization

#### Category-1.1: Anonymous access to K8s server

Sample code snippets: 

#### Category-1.2 Default Authorization mode enabled 

Sample code snippets

### Category-2: Implementing Kubernetes Specific security policies

#### Category-2.1 Network Specific Policies
Sample code snippets: 

#### Category-2.2 Pod Specific Policies
Sample code snippets: 

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




