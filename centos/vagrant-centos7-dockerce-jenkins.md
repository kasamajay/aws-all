# running jenkins as docker container on centos 7 spun on local windows pc using vagrant

## vagrant tweaks
```
cpus = "2"
memory = "2048"

Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 50000, host: 50000
end
```


> docker installation one of my own documentation

`docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts-jdk11`

## below are concerns
- yet to explore, to make jenkins run faster
- jenkins options to set higher heap memory for jenkins jvm
- sample java application build (lots of time, lots of data downloaded from internet from external central maven repository)
- loads of storage used 
