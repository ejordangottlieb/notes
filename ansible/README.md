# Ansible Cookbook
Useful techniques, playbook syntax, and module use examples.   

## Variables

### How to increment an Ansible fact
This example will replicate python x += 1 integer increment:

```yaml
- name: Set x to initial value
  set_fact: x=1

- name: Increment x by 1 loop
  set_fact: x={{ x | int + 1 }}
  with_sequence: start=0 end=32

- name: Debug print the value of x
  debug: msg="{{ x }}"
```

### Creating and Updating a Dynamic List
Use to store and employ facts generated during a playbook run.  This particular snippet pulls a list from a registered variable containing the stdout of multiple iterations of "openstack volume show -f json."  Each instance of stdout is stored in my_list.  The server_list dict is provided during the playbook run using the -e option (not included in this example).

```yaml
- name: For each server entry report volume ID
  shell: openstack volume show "{{ item.key }}_volume" -f json
  with_dict: "{{ server_list }}"
  register: report_volume_IDs

- name: Initialize empty list
  set_fact:
    my_list: []

- name: Store each instance of JSON output in my_list
  set_fact:
   my_list: "{{ my_list + [ item.stdout|from_json ] }}"
  with_items:
    "{{ report_volume_IDs.results }}"
```


