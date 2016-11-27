# Ansible Cookbook
Useful techniques, playbook syntax, and module use examples.   


## Variables

### How to increment an ansible fact
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

### Creating and updating a dynamic list


