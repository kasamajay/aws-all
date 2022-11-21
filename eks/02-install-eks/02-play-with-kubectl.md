# Install EKS using AWS CLI and AWS Console
Pre-requisites, have eks cluster with node-group (managed nodes)
- EKS Cluster control plane
- EKS Cluster data plane (node groups, with couple of nodes)

## Explore the EKS cluster with Kubectl commands
- Play with kubectl commands on the cluster
- Get the kubeconfig set (pull the kubeconfig from eks cluster)
- (Setup kubectl autocompletion)[https://kubernetes.io/docs/reference/kubectl/cheatsheet/]
- Note: explore the non namespaced resources (e.g. nodes, pv, storageclasses, ingressclasses, clusterroles, clusterrolebindings, validatingwebhooks, mutatingwebhooks etc)
- Note: explore the namespaced resoure (pods, services, deployments, statefulsets, daemonsets, pvc, serviceaccounts, roles, rolebindings etc)
- Note: explore default namespace
- Note: explore kube-system namespace
- Note: (explore the shortnames and full list of resource types available to explore)[https://kubernetes.io/docs/reference/kubectl/#resource-types]
- (Full kubectl cli reference)[https://kubernetes.io/docs/reference/kubectl/]