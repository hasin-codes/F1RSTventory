import toml

def load_config():
    return toml.load('.streamlit/config.toml')

config = load_config()
