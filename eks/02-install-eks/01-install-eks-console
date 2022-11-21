# Install EKS using AWS CLI and AWS Console
- (Instructions to Installing EKS Cluster using AWS CLI and AWS Console)[https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html]

## Setup AWS CLI with IAM User's creds

- Grab IAM User's creds 
  - AWS Console
  - Right top 
  - Click on user
  - Click on Security credentials
  - Create Access Key (Button) > Download

- AWS CLI Configure VM with aws IAM credentials
```
aws configure
# region eu-west-2 (for me)
aws configure list
aws s3 ls
```

## Setup the VPC for the EKS (using AWS CLI, this will create cloudformation stack which creates the VPC and Subnets for the EKS)

```
export MY_AWS_REGION=eu-west-2
export MY_EKS_CLUSTER_NAME=my-eks-vpc-stack

aws cloudformation create-stack \
  --region ${MY_AWS_REGION} \
  --stack-name ${MY_EKS_CLUSTER_NAME} \
  --template-url https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml

cat <<EOF > eks-cluster-role-trust-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

aws iam create-role \
  --role-name myAmazonEKSClusterRole \
  --assume-role-policy-document file://"eks-cluster-role-trust-policy.json"

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy \
  --role-name myAmazonEKSClusterRole

```

## Create EKS using the AWS Console
1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.

2. Make sure that the AWS Region shown in the upper right of your console is the AWS Region that you want to create your cluster in. If it's not, choose the dropdown next to the AWS Region name and choose the AWS Region that you want to use.

3. Choose Add cluster, and then choose Create. If you don't see this option, then choose Clusters in the left navigation pane first.

4. On the Configure cluster page, do the following:

    1. Enter a Name for your cluster, such as my-cluster. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 100 characters.
    2. For Cluster Service Role, choose myAmazonEKSClusterRole.
    3. Leave the remaining settings at their default values and choose Next.
    4. On the Specify networking page, do the following:
    5. Choose the ID of the VPC that you created in a previous step from the VPC dropdown list. It is something like vpc-00x0000x000x0x000 | my-eks-vpc-stack-VPC.
    6. Leave the remaining settings at their default values and choose Next.
    7. On the Configure logging page, choose Next.
    8. On the Review and create page, choose Create.
    9. To the right of the cluster's name, the cluster status is Creating for several minutes until the cluster provisioning process completes. Don't continue to the next step until the status is Active.