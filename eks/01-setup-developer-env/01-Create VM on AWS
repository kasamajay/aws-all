# Developer machine 
- Create new VM on your developer laptop
- or 
- Create new VM on AWS 

## Create new VM on AWS
- Login to AWS Mgmt console
- Choose London region (for me)
- VPC > Check for default VPC > if no default VPC > Create Default VPC
- EC2 > Create Launch template 
  - Amazon linux 2
  - keypair
  - t3.medium
  default vpc
  - public subnet
  - Public IP
  - 20GB
  - spot
- Create VM  (from above launch template)
  - Amazon linux 2
  - keypair
  - default vpc
  - public subnet
  - Public IP
  - t3.medium
  - 20GB
- EC2 > wait for the instance to be ready
- EC2 > Security Group > Add rule to allow SSH traffic from all Internet IPs 0.0.0.0/0
- EC2 > EC2 Connect
