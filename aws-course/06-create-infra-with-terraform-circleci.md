# Terraform, CircleCI
1. create iam user `terraform`
2. create s3 bucket (same name which is used in terraform backend s3 block)
3. create dynamodb table (same name which is used in terraform backend s3 block) (LockID partition-key string type)
4. give ec2, s3, dynamodb full access to `terraform` user
5. create security creds for `terraform` user
6. create circle-ci org settings > contexts > create context xxx > add environment variables
```
AWS_ACCESS_KEY_ID      xxx
AWS_ACCOUNT_ID         290653579848
AWS_SECRET_ACCESS_KEY  xxx	
```
5. add .circleci/config.yml
6. add jobs `plan`, `apply` (use cimg/aws:2024.03 https://circleci.com/developer/images/image/cimg/aws)
7. add workflow plan, hold (type: approval, requires: [plan]), apply (requires: [hold])
8. each job, uses `checkout` step


