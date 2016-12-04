# Exabgp Notes Page
Various examples of Exabgp Syntax

## Static Configuration Examples

### BGP/MPLS IPv4 Virtual Private network
This example advertises two VPN prefixes with the following attributes:

- Prefix: 172.16.3.0/24
-- rd 1:1
-- med 0;
-- next-hop 1.1.1.1
-- route-target(RT) 100:100
-- label 24014 (the target label of the terminating PE VRF)
- Prefix: 192.168.0.0/16
-- rd 1:1
-- med 0;
-- next-hop 1.1.1.1
-- route-target(RT) 100:100
-- label 24014
-- The prefix will be advertised as multiple /22 prefixes

```
neighbor 1.1.1.5 {
        description "a VPNV4 test peer";
        router-id 192.168.122.60;
        local-address 1.1.1.6;
        local-as 65001;
        peer-as 65001;
        hold-time 180;

        static {
                route 172.16.3.0/24 {
                    rd 1:1;
                    med 0;
                    next-hop 1.1.1.1;
                    extended-community [ 0x0002006400000064 ];
                    label 24014;
                }
                route 192.168.0.0/16 {
                    rd 1:1;
                    med 0;
                    next-hop 1.1.1.1;
                    extended-community [ 0x0002006400000064 ];
                    label 24014;
                    split /22;
        }
}
```

