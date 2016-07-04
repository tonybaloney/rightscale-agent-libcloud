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