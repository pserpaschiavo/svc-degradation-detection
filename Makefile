setup-calico: 
	@kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.1/manifests/tigera-operator.yaml
	@sleep 10
	@kubectl apply -f kubernetes/calico/custom-resources.yaml

remove-calico:
	@kubectl delete -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.1/manifests/tigera-operator.yaml
	@kubectl delete -f kubernetes/calico/custom-resources.yaml


setup-flannel:
	@kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

remove-flannel:
	@kubectl delete -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

setup-multus:
	@kubectl apply -f https://raw.githubusercontent.com/k8snetworkplumbingwg/multus-cni/master/deployments/multus-daemonset-thick.yml

remove-multus:
	@kubectl delete -f https://raw.githubusercontent.com/k8snetworkplumbingwg/multus-cni/master/deployments/multus-daemonset-thick.yml

setup-ovs:
	@kubectl apply -f https://github.com/kubevirt/cluster-network-addons-operator/releases/download/v0.89.1/namespace.yaml
	@kubectl apply -f https://github.com/kubevirt/cluster-network-addons-operator/releases/download/v0.89.1/network-addons-config.crd.yaml 
	@kubectl apply -f https://github.com/kubevirt/cluster-network-addons-operator/releases/download/v0.89.1/operator.yaml
	@kubectl apply -f https://gist.githubusercontent.com/niloysh/1f14c473ebc08a18c4b520a868042026/raw/d96f07e241bb18d2f3863423a375510a395be253/network-addons-config.yaml

setup-metallb:
	@kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.8/config/manifests/metallb-native.yaml

remove-metallb:
	@kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.8/config/manifests/metallb-native.yaml

setup-cert-manager:
	@helm repo add jetstack https://charts.jetstack.io
	@helm repo update
	@helm upgrade --install cert-manager jetstack/cert-manager \
  		--namespace cert-manager \
  		--create-namespace \
  		--set crds.enabled=true

setup-prometheus:
	@helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	@helm repo update
	@helm install prometheus prometheus-community/kube-prometheus-stack \
  		--namespace monitoring \
  		--create-namespace \
		--values kubernetes/prometheus/values.yaml

setup-ebs:
	@helm repo add openebs https://openebs.github.io/charts
	@helm repo update
	@helm upgrade --install openebs --namespace openebs openebs/openebs --create-namespace
	@kubectl patch storageclass openebs-hostpath -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

setup-lpp:
	@kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.30/deploy/local-path-storage.yaml

