import os
import json

def LoadConfig():
    """
    Load configuration from the config.json file located relative to this script.

    Returns:
    - A dictionary containing the configuration.
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_directory, '..', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
