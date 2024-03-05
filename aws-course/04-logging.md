# fluent-bit, elasticsearch, kibana
1. fluent-bit
```
https://docs.fluentbit.io/manual/installation/linux/amazon-linux

please add a new file called fluent-bit.repo in /etc/yum.repos.d/ with the following content

[fluent-bit]
name = Fluent Bit
baseurl = https://packages.fluentbit.io/amazonlinux/2023/
gpgcheck=1
gpgkey=https://packages.fluentbit.io/fluentbit.key
enabled=1

sudo yum install fluent-bit
sudo systemctl start fluent-bit
```
2. elasticsearch
```
```
3. kibana
```
```
