```
important files

~/.aws/config
~/.aws/credentials


download aws cli (linux binary, move to /usr/local/bin, executable permissions)
aws configure # set the aws credentials

AWS Named profiles (below user1 is named profile)

sample ~/.aws/config

[default]
region=us-west-2
output=json

[profile user1]
region=us-east-1
output=text

sample ~/.aws/credentials

[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[user1]
aws_access_key_id=AKIAI44QH8DHBEXAMPLE
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY

#using aws named profiles
aws ec2 describe-instances --profile user1
export AWS_PROFILE=user1
```