# EC2, EBS, Linux, Disks
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
