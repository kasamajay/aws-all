# start the aws vm with centos (amazon marketplace ami)
ssh -i .ssh/<key>.pem centos@<public ip>
cat /etc/os-release
sudo yum update -y

---

sudo yum install tree -y
sudo yum install git -y

sudo yum install wget -y
sudo yum install bind-utils -y #for commands like dig, nslookup

---
yum list ansible (note: ansible is not found in default repos of centos)
yum install ansible (won't find the ansible package)

sudo yum install epel-release
sudo yum update -y
sudo yum install ansible -y


ansible --version
ansible -m ping localhost

---
python (python2 is installed by default)

sudo yum list python3

sudo yum install python3 -y

python3 --help | more

mkdir pythonapps
cd pythonapps
mkdir app1
cd app1
python3 -m venv app1_py_env
tree .
source app1_py_env/bin/activate
deactivate



----
docker installation on centos

https://docs.docker.com/engine/install/centos/

sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
	
sudo yum install docker-ce docker-ce-cli containerd.io

#yum list docker-ce --showduplicates | sort -r
#sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io

sudo systemctl start docker && sudo systemctl enable docker

sudo usermod -aG docker $(whoami)
sudo reboot


docker info
docker --version

docker ps
docker images

docker volume ls
docker network ls

ip a (check for docker network)

sudo yum install tree -y

ls -ld /var/lib/docker

sudo tree /var/lib/docker

----

docker info | more (this gives good information about the docker home directory, docker registry, storage drivers, network plugins etc)

sudo systemctl status docker
journalctl -u docker

important folders
  /var/lib/docker
  
ip a (check for docker network)

