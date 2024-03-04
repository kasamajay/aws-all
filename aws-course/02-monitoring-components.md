# Monitoring pipeline
1. install prometheus
```
https://prometheus.io/docs/introduction/overview/
https://prometheus.io/docs/prometheus/latest/installation/
wget https://github.com/prometheus/prometheus/releases/download/v2.45.3/prometheus-2.45.3.linux-amd64.tar.gz
tar xvfz prometheus-2.45.3.linux-amd64.tar.gz
cd /home/ec2-user/monitoring/prometheus-2.45.3.linux-amd64
./prometheus  # check and adjust prometheus.yml

expose 9090 port on security group
browser <public-ip-address-of-instance>:9090

```
2. install node exporter
3. connect prometheus with node exporter
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar xvzf node_exporter-1.7.0.linux-amd64.tar.gz
./node-exporter

node exporter will expose the metrics on 9100 port
edit the prometheus > scrap config > add node target > restart prometheus
browser > prometheus > targets
```
4. install grafana
5. connect grafana with prometheus
```
https://grafana.com/grafana/download?pg=oss-graf&plcmt=hero-btn-1
wget https://dl.grafana.com/oss/release/grafana-10.3.3.linux-amd64.tar.gz
tar -zxvf grafana-10.3.3.linux-amd64.tar.gz
cd bin
./grafana-server
expose 3000 port on security group
browser <public-ip-address-of-instance>:3000
connections > add > prometheus > http://localhost:9090
https://grafana.com/grafana/dashboards/1860-node-exporter-full/
right top > import dashboard > get the dashboard ID (google search grafana dashboard for node exporter)
```
6. create another ec2 instance
   ```
   install node exporter, unpack, run-it
   prometheus node > kill prometheus > edit prometheus config > add new target to scrap config > start prometheus
   check the grafana tab browser > check dashboard
   ```
7. create another ec2 instance
   ```
   install node exporter, unpack, run-it
   prometheus node > kill prometheus > edit prometheus config > add new target to scrap config > start prometheus
   check the grafana tab browser > check dashboard
   ```
