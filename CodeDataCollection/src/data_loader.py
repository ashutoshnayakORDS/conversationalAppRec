import pandas as pd
import json

def load_data(apps_meta_path,app_information_dict_path):
    """Loads apps_meta from a parquet file."""
    apps_meta_data = pd.read_parquet(apps_meta_path)

    """Loads apps information"""
    try:
        with open(app_information_dict_path) as f:
            app_information_dict = json.load(f)

    except:
        # contains the text
        app_information_dict = {}

    return (apps_meta_data,app_information_dict)