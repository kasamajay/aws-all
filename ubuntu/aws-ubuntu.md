# Create VM with ubuntu 20.04 LTS
```
ssh into Vm using ubuntu user
sudo apt update -y
sudo apt install tree
sudo apt install net-tools
sudo apt install docker.io  (this will install docker from ubunto repo) [alternatively docker can be installed by adding repo from docker and install docker-ce package]
sudo usermod -aG docker $(whoami)
sudo reboot
```
----
```
docker ps
docker volume ls
docker network ls
```

```
docker images
docker image ls
```
---
```
sudo apt install ansible -y
ansible --version (most important to check the file that ansible looks for imporant files like inventory, configuration, modules etc)
ansible -h (for help)

ansible -m ping localhost
```
