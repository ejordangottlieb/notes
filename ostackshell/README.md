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

### Create Port and Disable Port Security
This requires that security groups are disabled during the initial group creation.

```
neutron port-create --no-security-groups [parent network ID]

neutron port-update [port ID] --port-security-enabled=False
```

### Attach Port to Nova Instance

```
nova interface-attach --port-id [port ID] [host ID]
```


