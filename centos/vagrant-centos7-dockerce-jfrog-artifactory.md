# running jfrog artifactory pro as docker container on centos 7 spun on windows machine using vagrant

loads of time taken to download the artifactory image from docker.bintray.io (jfrog's public container registry)
- make sure to have good network connection (spend on it)
- make sure to have good disk (speed and quantity) on your PC (spend on quality)
- make sure to have loads of RAM
- make sure to have loads of CPU


I had to increase the vCPUs and RAM for vagrant's centos7 VM

```
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false
  
    vb.cpus = "3"
    # Customize the amount of memory on the VM:
    vb.memory = "8192"
  end
  ```
  
 Hoping it works faster now

 ```
 sudo su -
 cd /
 mkdir -p $JFROG_HOME/artifactory/var/etc
 cd $JFROG_HOME/artifactory/var/etc
 touch system.yaml 
 chown -R 1030:1030 $JFROG_HOME/artifactory/var/etc
 chmod -R 777 $JFROG_HOME/artifactory/var/etc
 docker run --name artifactory -v $JFROG_HOME/artifactory/var/:/var/opt/jfrog/artifactory -d -p 8081:8081 -p 8082:8082 docker.bintray.io/jfrog/artifactory-pro:latest
 ```

localhost:8082
No license found. If you have a license click here to activate. To purchase a license, visit our website or contact sales@jfrog.com

