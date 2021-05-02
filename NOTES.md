### Exploration of Shamim's work 


#### File types 

Shamim is scanning all YAML files. Need to find YAML files that describe K8S deployments. 
Need to ignore files like: 

- /Users/arahman/K8S_REPOS/GITLAB_REPOS/githook/config/crd/bases/tools.pongzt.com_githooks.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubernetes-apps/network_plugin/contiv/tasks/configure.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/container-engine/cri-o/tasks/crio_repo.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/bootstrap-os/tasks/bootstrap-debian.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/vault/roles/vault/tasks/bootstrap/start_vault_temp.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-owners-service/src/main/resources/application-k8s.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-notifications-service/src/main/resources/application-k8s.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/crds/SGBackupConfig.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/crds/seldon-deployment-crd.yaml (K8S `CustomResuourceDefinition` ... needs `KubeCtl` to execute ... so cannot guarantee any file liek this will be executable) 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/crds/opendatahub_v1alpha1_opendatahub_cr.yaml (K8S `OpenDataHub` ... needs `KubeCtl` to execute ... so cannot guarantee any file like this will be executable) 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/repository/index.yaml (has `apiVersion` but no `kind:`)
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/tests/files/packet_debian10-containerd.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/tests/testcases/040_check-network-adv.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/test-infra/image-builder/roles/kubevirt-images/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/container-engine/docker/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/container-engine/containerd/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/obtao@kubernetes/kubernetes/elastic-stack/values.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-owners-service/src/main/resources/application.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-notifications-service/src/main/resources/application.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/e2e/spec/restore.backup.values.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/olm-catalog/opendatahub-operator/0.3.0/opendatahub-operator.v0.3.0.clusterserviceversion.yaml  (`K8S ClusterServiceVersion` needs to be excuted by command line so no guarantee)
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/olm-catalog/opendatahub-operator/0.2.0/opendatahub-operator.v0.2.0.clusterserviceversion.yaml (`K8S ClusterServiceVersion` needs to be excuted by command line so no guarantee)
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/onap_oom_automatic_installation/vars/ddf.yml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/onap_oom_automatic_installation/roles/oom_prepare/tasks/main.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi//.gitlab-ci.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubernetes-apps/network_plugin/weave/tasks/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/network_plugin/contiv/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubespray-defaults/defaults/main.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-vets-service/src/main/resources/application-k8s.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-frontend-service/src/main/resources/application-k8s.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-customers-service/src/main/resources/application-k8s.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-visits-service/src/main/resources/application-k8s.yml




#### Helm charts 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/helm/cp-helm-charts/charts/cp-control-center/templates 

Example of how charts are used. No secuirty violations 

#### Default namespace 

##### True Positive Instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml
> This is an example of a TP as the default namespace is acutually used by a Deployment 
```
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "1"
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app":"nginx"},"name":"nginx-deployment","namespace":"default"},"spec":{"repli$
  creationTimestamp: "2020-01-24T10:54:56Z"
  generation: 1
  labels:
    app: nginx
  name: nginx-deployment
  namespace: default
  resourceVersion: "96574"
  selfLink: /apis/apps/v1/namespaces/default/deployments/nginx-deployment
  uid: e1075fa3-6468-43d0-83c0-63fede0dae51
```


> /Users/arahman/K8S_REPOS/GITLAB_REPOS/data-image/airflow_image/manifests/services.yml
This file uses 
```
apiVersion: v1
kind: Service
metadata:
  name: airflow-webserver
  namespace: default
spec:
  selector:
    app: airflow

```
`app: airflow` is later used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/data-image/airflow_image/manifests/deployment.yaml` as 
```
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: airflow-deployment
  namespace: default
spec:
  selector:
    matchLabels:
      app: airflow
```

so TP. 


##### False  Positive Instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/helm/cp-helm-charts/examples/ksql-demo.yaml 
> This is an example of false positive as it default namespace is not used for a deployment 

```
apiVersion: v1
kind: Pod
metadata:
  name: ksql-demo
  namespace: default
```

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/deploy/serviceaccount-varnish.yaml ... another example of a FP 
> /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/keycloak/ingress.yaml ... another example of a FP, as the default namespace is used in the file as a service, whcih is not used anywhere else 
> /Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/lb/rl50.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/lb/rl100.yaml ...  examples of FPs 




> nano -c /Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/cl1-k8s/cl1-lb.yaml 
> This will be a TP if the Service is used by a deployment, using the provided selector `selector:
    load-balancer-myapp-GKE_1-lb: "true"` 
> So far not seeing any mathcing deployments, so FP. 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/cl2-k8s/cl2-ingress.yaml
> This file uses an Ingress that is consumed by the Service `serviceName: "myapp-GKE_2-lb"`. The service is later used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/cl2-k8s/cl2-lb.yaml` in 
```
kind: "Service"
metadata:
  name: "myapp-GKE_2-lb"
...
  selector:
    load-balancer-myapp-GKE_2-lb: "true"
```
If the selector is available in a `kind:Deployment` only then we can determine it as a TP. So far not seeing any deployments that
match, so FP 

#### Insecure HTTP 

##### True Positive Instances 

> In `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-init-container-scripts.yaml ` we have  a config map as shown below: 
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: init-container-scripts
```
This config map is consumed by `update-configMap-init-container-scripts.sh` as `kubectl create -f configMap-init-container-scripts.yaml`
This is a TP, as ConfigMaps can be used from the command line. 

Same argument goes for `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-init-container-scripts.yaml`

and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-init-container-scripts.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-nova-compute-setup.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-nova-compute-setup.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-nova-compute-setup.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-nova-compute-setup.yaml` (This one has instances of 0.0.0.0) and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-glance-setup.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-ceilometer-central-setup.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-openstack-openrc.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-heat-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-glance-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-ceilometer-central-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-openstack-openrc.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-heat-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-glance-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-ceilometer-central-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-openstack-openrc.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-heat-setup.yaml`,
`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-glance-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-cinder-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-nova-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-horizon-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-neutron-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-cinder-setup.yaml`,`/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-nova-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-neutron-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-aodh-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-cinder-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-nova-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-neutron-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-aodh-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-cinder-setup.yaml`,  `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-nova-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-neutron-server-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-aodh-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/configMap-keystone-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-keystone-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/configMap-horizon-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-keystone-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/configMap-horizon-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-keystone-setup.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-queens/configMap-horizon-setup.yaml`

Note to self: Other ways to store config maps are using Pod, with the `valueFrom:  configMapKeyRef: name` tag and through Volumes with the `configMap: name:` tag. Reff: https://kubernetes.io/docs/concepts/configuration/configmap/


> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-elastic-logging//kibana-deployment.yaml` , `/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/gitlab/gitlab-deployment.yml` are TPs: `kind: Deployment` 

##### False  Positive Instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_alertmanagerCustomResourceDefinition.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_prometheusCustomResourceDefinition.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_prometheusruleCustomResourceDefinition.yaml :  parsing issues 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/lb/glb-configmap-var.yaml, has a configmap called `nginx`, which is never used in the repo `/Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/` so FP. Same for `/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/gitlab-runner/gitlab-runner-docker-configmap.yml` 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/configuration/grafana/values.yaml, part of a Helm chart, but used no where , so FP 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/resources/gangway.yaml, used values go nowhere, so FP 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/sdp-prototype/Chart.yaml and /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/skuid/Chart.yaml FP as URL from another website 



