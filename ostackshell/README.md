# Openstack shell templates
A list of often used openstack commands

## Glance

### Import Image
```
openstack image create [image name] --file [image loc] --disk-format qcow2 --container-format bare --public
```

## Neutron

### Create network with port security disabled
```
neutron net-create [net name] --port_security_enabled=False
```

### Create flat provider network with security disabled
```
neutron net-create [net name] --shared --port_security_enabled=False --provider:physical_network [phys net name] --provider:network_type flat
```
