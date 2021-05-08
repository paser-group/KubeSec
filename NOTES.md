### Integrating Taint Tracking for Kubernetes 


#### File types  ( **COMPLETED** ) 

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
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/clusters//clouds.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/dind/group_vars/all/distro.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/kafka/operator-objects/045-Crd-kafkamirrormaker.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/kafka/operator-objects/040-Crd-kafka.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/onap_oom_automatic_installation/roles/oom_postconfigure/tasks/main.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/doc/data/descriptions/stackgres-operator.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/crds/opendatahub_v1alpha1_opendatahub_cr.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/roles/grafana/tasks/main.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/kafka/operator-objects/042-Crd-kafkaconnects2i.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/opendatahub-operator/deploy/kafka/operator-objects/041-Crd-kafkaconnect.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_alertmanagerCustomResourceDefinition.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/dind/roles/dind-cluster/tasks/main.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/etcd/meta/main.yml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_servicemonitorCustomResourceDefinition.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-vets-service/src/main/resources/application-k8s.yml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-customers-service/src/main/resources/application-k8s.yml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-visits-service/src/main/resources/application-k8s.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-vets-service/src/main/resources/application.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-customers-service/src/main/resources/application.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/spring-petclinic-visits-service/src/main/resources/application.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/adduser/tasks/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/bootstrap-os/molecule/default/molecule.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubernetes/preinstall/meta/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubernetes/client/tasks/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/kvm-setup/roles/kvm-setup/tasks/user.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/vault/roles/vault/meta/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/vault/roles/vault/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/crds/SGCluster.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/koris/deploy/manifests/ext-cloud-openstack.yml (`kind: List`)
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/doc/data/descriptions/stackgres-operator.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/download/tasks/prep_kubeadm_images.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/vault/roles/vault/tasks/shared/config_ca.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubecf/.gitlab/deploy/runner/kubernetes/values.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/kubernetes-apps/cluster_roles/defaults/main.yml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/contrib/dind/roles/dind-host/tasks/main.yaml

#### Helm charts  ( **COMPLETED** ) 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/helm/cp-helm-charts/charts/cp-control-center/templates 

Example of how charts are used. No secuirty violations 

#### Default namespace  ( **COMPLETED** ) 

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


> /Users/arahman/K8S_REPOS/GITLAB_REPOS/spring-petclinic-kubernetes/helm/cp-helm-charts/examples/ksql-demo.yaml 
> This is an example of true positive as it default namespace is used for a pod 

```
apiVersion: v1
kind: Pod
metadata:
  name: ksql-demo
  namespace: default
```

##### False  Positive Instances 


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

#### Insecure HTTP  ( **COMPLETED** ) 

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


>  `/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/gitlab/gitlab-deployment.yml` are TPs: `kind: Deployment` 

##### False  Positive Instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_alertmanagerCustomResourceDefinition.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_prometheusCustomResourceDefinition.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_prometheusruleCustomResourceDefinition.yaml :  _CustomResourceDefinition_ does not go into deployments ... so FPs 

> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/lb/glb-configmap-var.yaml`, has a configmap called `nginx`, which is never used in the repo `/Users/arahman/K8S_REPOS/GITLAB_REPOS/advanced-kubernetes-workshop/` so FP. Same for `/Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/gitlab-runner/gitlab-runner-docker-configmap.yml` 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/resources/gangway.yaml, used values go nowhere, so FP. Also, as this is not a validly formatted manifest, tool will not detect HTTP instances, which is correct. 




> /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/configuration/grafana/values.yaml, part of a Helm chart, but used no where , so FP 





#### Hard-coded Secrets  ( **COMPLETED** ) 

##### True positive instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/values.yaml ... user name and password 
used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/templates/integrate-grafana-job.yaml`, so TP 


> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/tango-base/values.yaml` is TP as used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/tango-base/templates/databaseds.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/tango-base/templates/tangodb.yaml` 

> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/archiver/values.yaml` is TP as values used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/archiver/templates/archiverdb.yaml`, `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/archiver/templates/cleaner.yaml`

> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/dsh-lmc-prototype/values.yaml` is TP as it used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/dsh-lmc-prototype/templates/dslhm.yaml` 


> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/minecraft/values.yaml` is TP as used in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/minecraft/templates/secrets.yaml`




##### False positive instances 

> */Users/arahman/K8S_REPOS/GITLAB_REPOS/kubecf/deploy/helm/kubecf/values.yaml* : invalid username 
```
      bbs:
        name: diego
        password: ~
        username: ~
```

> */Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/nextcloud/values.yaml* , valid user name, but the values are not used
by any helm charts 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/django-k8s-starter//rabbit-values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/postgres/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/keycloak/values.yaml,  and : valid user name and password but not used, so FP 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/partial-deployments/tango-db-standalone/values.yaml and /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/matomo/values.yaml are FP as values not used 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/postgres/values-production.yaml and /Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/test/sample-secret-1.yaml are FPs as values are not used 

> */Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/keycloak/values.yaml* FP for passowrd as not strings are assigned 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/install/helm/stackgres-operator/crds/SGBackup.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/data-image/airflow_image/prometheus_config.yml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/00_operator_servicemonitorCustomResourceDefinition.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/dex/00-dex.yml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/demo-kubernetes-components/mongo-express.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/e2e/spec/sql-scripts.values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/e2e/spec/aks/backup-with-aks-storage.values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/stackgres/stackgres-k8s/e2e/spec/eks/backup-with-s3-storage.values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/githook/config/samples/2-v1alpha1_githooks.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/deploy/varnish.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/load-balancer/lego/deployment.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubecf/deploy/helm/kubecf/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/configuration/cert-manager/letsencrypt.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/configuration/bank-vaults/vault-secrets-webhook/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-gitlab-demo/gitlab-runner/gitlab-runner-docker-deployment.yml 

^ FP due to parsing issues 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/varnish-coffee.yaml (`valueFrom:` inferring data from environment, reff: https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/). Also the following: 

- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/varnish-system.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/varnish.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/varnish-coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/varnish-tea.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-varnish-ns/varnish-coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-varnish-ns/varnish-tea.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/demo-kubernetes-components/mongo.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes/configurations/deployment.yml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-sigs-kubespray/roles/network_plugin/calico/tasks/typha_certs.yml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/linode-kubernetes-engine-demo/test-mongo-express.yaml





> FP in `/Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/sni/values.yaml` and `/Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/hello/values.yaml` (`key:` and `crt:` ) as these are not used 


#### No Rolling Updates  ( **COMPLETED** ) 

##### True Positive Instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/deploy/varnish.yaml , TP, not using rolling update and also used by a deployment 
> Also, the following:
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/varnish-coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/varnish-system.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/varnish.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/varnish-coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/varnish-tea.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-varnish-ns/varnish-tea.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/namespace/varnish.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/turkce-kubernetes/kubernetes-playground/imperative-declarative-yontemler/yaml/gcr-deployment.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/test/e2e/deleteTLSsecret/cafe.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/other.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/tea.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/other.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/tea.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/coffee.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/tea.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-varnish-ns/coffee.yaml 
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-varnish-ns/tea.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/namespace/cafe.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/externalname/cafe.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/sni/beverage.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/hello/cafe.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/hello/cafe.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/basic-kubectl-commands/demo-test-deployment.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/basic-microservice-for-learning/kubernetes_dev/randomnum_svc.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/basic-microservice-for-learning/kubernetes_prod/randomnum_svc.yaml
- /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubecf/.concourse/pipeline.yaml 
- 



> Random example collected from Internet for testing
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-test
spec:
  replicas: 10
  selector:
    matchLabels:
      service: http-server
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  minReadySeconds: 5
  template:
    metadata:
      labels:
        service: http-server
    spec:
      containers:
      - name: nginx
        image: nginx:1.10.2
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
```

##### False Positive Instances 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/sni/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/tls/hello/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/varnish_pod_template/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/hello/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/justin@kubernetes/src/services/keycloak/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/tango-base/values.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/turkce-kubernetes/kubernetes-playground/replication-yontemlerine-genel-bakis/replication/rs.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/turkce-kubernetes/kubernetes-playground/replication-yontemlerine-genel-bakis/replication/rc.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/koris/addons/prometheus/42_prometheus_Prometheus.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/values-tea.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/values-other.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/cluster-and-ns-wide/values-coffee.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/values-tea.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/values-other.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/clusterwide/values-coffee.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/values-tea.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/k8s-ingress/examples/architectures/multi-controller/values-coffee.yaml, 

^ all of these are FPs they do not use `type: RollingUpdate`, but they do not map to `kind: Deployment` 

> /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-tutorial-series-youtube/kubernetes-configuration-file-explained/nginx-deployment-result.yaml : this is a FP because even with `type: RollingUpdate` and `kind: Deployment` , the tool throws an alert 
> /Users/arahman/K8S_REPOS/GITLAB_REPOS/obtao@kubernetes/kubernetes/app/php-fpm-deployment.yaml : this is a FP because even with `type: RollingUpdate` and `kind: Deployment` , the tool throws an alert 
> /Users/arahman/K8S_REPOS/GITLAB_REPOS/obtao@kubernetes/kubernetes/app/nginx-deployment.yaml : this is a FP because even with `type: RollingUpdate` and `kind: Deployment` , the tool throws an alert 


#### Privilege Escalation   ( **COMPLETED** ) 

##### True Positive Instances 

> `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/test/sample-pod.yaml` for the following
```
kind: Pod
metadata:
 name: sample-pod
spec:
 #hostNetwork: true
 containers:
 - name: sample-pod
   #image: call518/oaas-init-container
   image: call518/oaas-ocata
   securityContext:
     privileged: true
```

`securityContext:  privileged: true` this is the part that is probelmatic 

Same thing happens for 
- `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/test/sample-nfs-server.yaml`
- `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/test/sample-neutron.yaml`
- `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/test/sample-pod-1.yaml`
- `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-newton/nfs-server.yaml`
- `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-pike/nfs-server.yaml`
- `/Users/arahman/K8S_REPOS/GITLAB_REPOS/OpenStack-on-Kubernetes/src-ocata/nfs-server.yaml`
- 

##### False Positive Instances 

- /Users/arahman/K8S_REPOS/GITLAB_REPOS/turkce-kubernetes/kubernetes-playground/daemonset-ve-kullanimi/daemonset/fluentd-ds.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/calico-cumulus/demo-multicast/daemonset-pimd.yaml, /Users/arahman/K8S_REPOS/GITLAB_REPOS/kubernetes-extras/files/templates/calico/calico.yaml, this are FPs as `kind: DaemonSet` 


### Rules to detect secuirty anti-patterns: 

- `Missing security context`: ( **COMPLETED** ) A kubernetes Pod or Deployment does not have security context specified i.e., the following is not used 
```
spec:
  securityContext:
```

- `Over-allocated privilege`: ( **COMPLETED** ) A Kubernetes Pod or Deployment uses `allowPrivilegeEscalation=true` or `privileged: true` while specifying security context, i.e., the following is used
```
spec:
 #hostNetwork: true
 containers:
 - name: sample-pod
   #image: call518/oaas-init-container
   image: call518/oaas-ocata
   securityContext:
     privileged: true
``` 
- `Default namespace`:  ( **COMPLETED** )  A Kubernetes pod or deployment uses `namespace: default` 

- `Insecure HTTP`: ( **COMPLETED** )  Use of `http://` as a value, where they relevant key maps back to a pod or deployment

- `Hard-coded secret`: ( **COMPLETED** ) Use or hard-coded user name and passwords , must map to a pod, deployment, configmap, or a helm deployment 

- `Not rolling update`:  ( **COMPLETED** )  not using `type: RollingUpdate` in a deployment as shown in below

```
> reff: https://tachingchen.com/blog/kubernetes-rolling-update-with-deployment/ 
strategy:
  # indicate which strategy we want for rolling update
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 1
```

- `Unrestricted Network`:  ( **COMPLETED** )   No NetworkPolicy for a pod. Need to remember _NetworkPolicies are an application-centric construct which allow you to specify how a pod is allowed to communicate with various network "entities" (we use the word "entity" here to avoid overloading the more common terms such as "endpoints" and "services", which have specific Kubernetes connotations) over the network._

`kind: NetworkPolicy` needs to be in a YAML file, and the same file should also specify a pod selector label *x*, where *x* is a label of a pod. Example below: 

```
- podSelector:
        matchLabels:
          role: frontend
```


Another way is to use any one of the following that alllows all ingress and egress connections respectively:
```
spec:
  podSelector: {}
  ingress:
  - {}
```

```
spec:
  podSelector: {}
  egress:
  - {}
```

- `Unrestricted Resource Request`:  ( **COMPLETED** )   No resource limit for Deployment or Pod i.e. the following is not specified for a pod: both cpu and memory 
must be present  
```
      limits:
        memory: "128Mi"
        cpu: "500m"
```


### Limitations 

- Tool will report FP isntances for /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/sdp-prototype/Chart.yaml and /Users/arahman/K8S_REPOS/GITLAB_REPOS/skampi/charts/skampi/charts/skuid/Chart.yaml ... extra check will generate a lot of false negatives 