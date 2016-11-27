# Ansible Cookbook


## Variables

### How to increment a ansible fact
An equivalent to python x += 1

```yaml
- name: Set x to initial value
  set_fact: x=1

- name: Increment x by 1 loop
  set_fact: x={{ x | int + 1 }}
  with_sequence: start=0 end=32

- name: Debug print the value of x
  debug: msg="{{ x }}"
```

