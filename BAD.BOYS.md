# Bad Boys 

## TODOs 


## Already Handled 

#### FP instances for no resource limits 

`Not a 'no resource limits', as not 'kind:Pod' ` : [reff: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/]
- 10 YAML manifests: all handled, and under `TEST_ARTIFACTS/fp.no.reso*.yaml`  , 10 test cases added 



#### FP instances for no security context 

- `Not a 'no security context', as not 'kind:Pod' ` : https://github.com/in28minutes/spring-microservices-v2/blob/main/05.kubernetes/currency-exchange-service/backup/deployment-03-probes-configured.yaml [reff: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/]  


#### FP instances for default namespaces 

- `Not a default namespace`: https://github.com/kubernetes-native-testbed/kubernetes-native-testbed/blob/develop/manifests/cicd/cd-manifests/infra/nginx-ingress-cd.yaml and https://github.com/narenarjun/ultimate-stack/blob/master/kubernetes/staging/gitops-setup/argocd-app-config.yaml and https://github.com/stacksimplify/aws-eks-kubernetes-masterclass/blob/master/09-EKS-Workloads-on-Fargate/09-02-Fargate-Profiles-Advanced-YAML/kube-manifests/02-Applications/01-ns-app1/02-Nginx-App1-Deployment-and-NodePortService.yml 


#### Hard-coded secrets (all are FP instances and handled properly)

- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/glance-pv.yaml 
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/nfs-server.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/nfs-server-pvc.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-env-common.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-nova-server-setup.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-pike/glance-pvc.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-ocata/ceilometer-central-pvc.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-tutorial-series-youtube/pull-images-from-private-reporsitory-in-k8s/my-app-deployment.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-tutorial-series-youtube/pull-images-from-private-reporsitory-in-k8s/docker-secret.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-tutorial-series-youtube/container-communication-k8s-networking/nginx-sidecar-container.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-service.yaml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/gitlab-ns.yml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/gitlab/redis-svc.yml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/gitlab/gitlab-config-storage.yml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/gitlab/postgresql-configmap.yml 
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/gitlab-runner/gitlab-runner-docker-deployment.yml
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/load-balancer/nginx/tcp-configmap.yaml


##### Save for Taintube (ALREADY HANDLED)
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-horizon-setup.yaml 
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-neutron-server-setup.yaml 
- /Users/arahman/K8S_REPOS/TEST_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-openstack-openrc.yaml 
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-tutorial-series-youtube/container-communication-k8s-networking/postgres.yaml 
- /Users/arahman/K8S_REPOS/TEST_REPOS/kubernetes-gitlab-demo/gitlab/gitlab-deployment.yml


##### Parsing is still a problem (LEAVE AS LIMITATION )
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-extras/files/templates/calico/calico.yaml (NESTED YAML: HOST NETWORK)
- https://github.com/oktadev/jhipster-microservices-example/blob/master/kubernetes/registry/application-configmap.yml (template generated content where secret is provided) 

