# EC2, EBS, Linux, Disks (fdisk, mkfs)
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
1. Steps to create EC2 Instance,
```
Using console create EC2 Instance > London region > t2.micro > Amazon Linux > Security groups (allow ssh) > no key pair
```
2. create EBS Volume
```
EC2 console > EBS > Create Volume (in the same availability zone as above EC2 instance) > 1GGB
```
3. Attach Volume to Instance,
```
Attaching new volume to Instance
```
4. list block devices,
```
lsblk
```
5. format disks,
6. create partitions,
7. file systems on partitions,
8. mount the new file systems to directories
```
    1  lsblk
    2  sudo fdisk -l
    3  sudo fdisk /dev/xvdf
    4  lsblk
    6  sudo mkdir /data
    7  sudo mkfs -t xfs /dev/xvdf1
    8  lsblk
    9  sudo mount /dev/xvdf1 /data
   10  lsblk
   11  cd /
   12  ls -l
   14  history
```
