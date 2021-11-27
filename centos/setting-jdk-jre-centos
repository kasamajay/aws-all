# setting up java in centos

# java jdk vendors (oracle, amazon, ibm, redhat, azul, openjdk etc)
# java jdk version (lts versions, jdk releases every 6months etc)
# oracle release both commerical version jdk (otn license) and opensource version of jdk (openjdk)
# oracle jvm is hotspot jvm
# below are different openjdk release by different companies like redhat, azul, amazon, adoptjdk
# adoptjdk release openjdk binaries and their own optimized jvm 
# amazon corretto release both jdk and jvm of their own
# azul calls jvm as zing (most powerful)

# developer needs jdk, jre, jre (jdk for compiling the code to class file, jre for java libraries and jvm for actually running class file(byte code))
# server infrastructure needs jre (jre include java libraries and jvm), jvm is bytecode interpreter

# java jdk 11 (released in sept 2018) is LTS. supported till 2026
# next lts java jdk is 17 (to be released in sep 2021) will be supported for 3 years

sudo yum list java
# below is jre 8 installation (works)
sudo yum install java-1.8.0-openjdk 

# below is jdk 8 installation
sudo yum install java-1.8.0-openjdk-devel 

# below is jre 11 installation 
sudo yum install java-11-openjdk

# below is jdk 11 installation
sudo yum install java-11-openjdk-devel


ls -l $(which javac)  #they point to /usr/lib/jvm . also check what is /etc/alternatives/java points to
ls -l $(which java)


java -version
# alternatives is the command to install different versions of java jdk and also configure what version to be default
alternatives --config java 
