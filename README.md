# Libcloud RightScale UCA Agent

## Installation

```bash
cd uca # UCA bin path
git clone https://github.com/tonybaloney/rightscale-agent-libcloud plugins
cd plugins
pip install -r requirements.txt
```

## Configuration

Edit `config.yaml` to configure which libcloud driver to use and the credentials to connect, for example:

```yaml
provider: dimensiondata
connection:
    key: my_username
    secret: my_PASsword!
    region: dd-au
```

__`config.yaml`__ must live in the UCA bin directory, not the plugin directory.

## Mapping driver specific values

Libcloud supports a dictionary called __extra__ in the `Node` class. You can map the values of these to RightScale instance values using a map
attribute in __`config.yaml`__.

For example:

```yaml
maps:
    list_instances:
        created_at: "deployedTime"
        memory_mb: "memoryMb"
        os_platform: "OS_type"
```

The key represents the key in RightScale and the value represents the key in Libcloud