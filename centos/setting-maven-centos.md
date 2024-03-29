# Maven is a Java tool, so you must have Java installed in order to proceed.

The official CentOS repositories contain Maven packages that can be installed with the yum package manager. This is the easiest way to install Maven on CentOS. However, the version included in the repositories may lag behind the latest version of Maven.

https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

java -version
# alternatives is the command to install different versions of java jdk and also configure what version to be default
alternatives --config java 

# installing maven from centos repos, gets older version. it also brings in its own java 
sudo yum install maven -y 
mvn --version  #for maven version 3.6.x we need java 9 and above


# Maven 3.3+ requires JDK 1.7 or above to be installed
wget https://dlcdn.apache.org/maven/maven-3/3.8.4/binaries/apache-maven-3.8.4-bin.tar.gz -P /tmp

sudo tar xf /tmp/apache-maven-3.8.4-bin.tar.gz -C /opt 
sudo ln -s /opt/apache-maven-3.8.4 /opt/maven 

# /etc/profile.d/maven.sh
export JAVA_HOME=/usr/lib/jvm/jre-openjdk
export M2_HOME=/opt/maven
export MAVEN_HOME=/opt/maven
export PATH=${M2_HOME}/bin:${PATH}

sudo chmod +x /etc/profile.d/maven.sh

source /etc/profile.d/maven.sh

mvn -version # unfortunately mvn still uses jdk 8, not sure how to make maven use jdk 11
