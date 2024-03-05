# CPU, Memory, Disk load testing
1. CPU
```
stress --cpu 2 --timeout 30s
```
3. Memory
```
stress --vm 1 --vm-bytes 500M --timeout 60s
```
3. Disk
   ```
   mkdir tmp
   cd tmp
   fallocate -l 1G myfile.txt
   ```
