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

https://docs.fluentbit.io/manual/pipeline/outputs/elasticsearch
cd /etc/fluent-bit
[OUTPUT]
    Name es
    Match *
    Host xxx
    Port 443
    Logstash_Format On
    Logstash_Prefix test
    Suppress_Type_Name On
    tls On
    HTTP_User admin
    HTTP_Passwd xxx

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

this needs a bigger instance, failed to start, so going with aws opensearch managed cluster (alias managed domain)

managed aws opensearch domain (free, takes about 10mins to create)
 > public
 > fine grained
 > master username and password
 > t3.small.search
```
3. kibana
```
get url from managed aws opensearch domain (_dashboards) and access with master username and password from browser
```
