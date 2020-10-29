import yaml


def load_devices(filename="configs/devices.yml") -> dict:
    with open(filename, "r") as f:
        return yaml.safe_load(f.read())
