
#golang installation

wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.13.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin

# ~/.bash_profile
export PATH=$PATH:/usr/local/go/bin
source ~/.bash_profile

# test go installation

mkdir ~/go
mkdir -p ~/go/src/hello

# vi ~/go/src/hello/hello.go

package main

import "fmt"

func main() {
    fmt.Printf("Hello, World\n")
}


cd ~/go/src/hello
go build

./hello
