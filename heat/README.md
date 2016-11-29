# Openstack Heat Cookbook
Various examples of Heat usage.   

## Basic Template Skeleton
Current valid version options are:
- 2013-05-23
- 2014-10-16
- 2015-04-30
- 2015-10-15
- 2016-04-08
- 2016-10-14 (newton)
- 2017-02-24 (ocata)                  

```yaml
heat_template_version: [ version ]

description:  >

  # Template description
  # ...

parameters:
  example_parameter:
    type: [ string | number | json | comma_delimited_list | boolean ]
    label: [ human readable label ]
    description: |
       The description 
    default: [ a default value if none is provided ]

resources:
  example_resource_server:
    type: OS::Nova::Server
    properties:
      name: [name]
      flavor: [flavor]
      networks:
        # Choose either format below
        - uuid: [ net UUID]
        - network: [net name]
  example_resource_network:
    type: OS::Neutron::Net
    properties:
      name: [ Name ]
      port_security_enabled: [ True | False ]
      shared: [ True | False ]
      tenant_id: String
      # value_specs: {...}
  example_resource_port:
    type: OS::Neutron::Port
    properties:
      admin_state_up: Boolean
      binding:vnic_type: String
      device_id: String
      device_owner: String
      dns_name: String
      mac_address: String
      name: String
      network: String
      port_security_enabled: Boolean
      qos_policy: String
      security_groups: [Value, Value, ...]
      value_specs: {...}
```

