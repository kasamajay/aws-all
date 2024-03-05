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
journalctl -u fluent-bit
```
2. elasticsearch
```
https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.12.2-linux-x86_64.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.12.2-linux-x86_64.tar.gz.sha512

sudo yum install perl-Digest-SHA

shasum -a 512 -c elasticsearch-8.12.2-linux-x86_64.tar.gz.sha512 
tar -xzf elasticsearch-8.12.2-linux-x86_64.tar.gz
cd elasticsearch-8.12.2/

./bin/elasticsearch
```
3. kibana
```
```
