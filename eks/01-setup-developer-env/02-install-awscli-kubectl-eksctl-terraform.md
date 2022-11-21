# Installation of tools

## Install AWS CLI
- Check aws cli version `aws --version`
- Google search for install aws cli
- (Link for AWS CLI Installation Instructions)[https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html]
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

## Install kubectl cli
- Check kubectl `kubectl cluster-info`
- Google search for install kubectl
- (Link for kubectl Installation Instructions)[https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/]
```
curl -LO https://dl.k8s.io/release/v1.22.0/bin/linux/amd64/kubectl
chmod +x kubectl 
sudo cp kubectl /usr/local/bin/
kubectl version --client
```

## Install eksctl cli
- Check (eksctl official website)[https://eksctl.io/]
- Check (eksctl github)[https://github.com/weaveworks/eksctl]
- Check (Link for eksctl Installation Instructions)[https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html]
```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```

## Install Terraform CLI
- Google search for install terraform
- (Link for terraform Installation Instructions)[https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#install-terraform]
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform
terraform -version
```


