# Centos 7 Notes
Various examples of Centos 7 Syntax

## Centos Networking

### Basic Bridging

- /etc/sysconfig/network-scripts/ifcfg-brname
```
DEVICE=brname
BOOTPROTO="static"
IPADDR="x.x.x.x"
NETMASK="x.x.x.x"
ONBOOT="yes"
TYPE="Bridge"
NM_CONTROLLED="no"
```

- /etc/sysconfig/network-scripts/ifcfg-ethname
```
DEVICE=ethname
TYPE=Ethernet
BOOTPROTO=none
ONBOOT=yes
NM_CONTROLLED=no
BRIDGE=brname
```

