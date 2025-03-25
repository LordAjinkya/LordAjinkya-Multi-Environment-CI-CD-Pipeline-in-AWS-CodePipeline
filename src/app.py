import json
import os

# Get environment (Default: dev)
env = os.getenv("APP_ENV", "dev")

# Load respective config file
config_path = f"configs/{env}-config.json"
with open(config_path, "r") as config_file:
    config = json.load(config_file)

print(f"Running in {env.upper()} environment")
print(f"Database: {config['database_url']}")
