'''
saves the app information (json dictionary) in the data folder
'''
import json

def save_data(apps_meta_data,apps_meta_path,app_information_dict, app_information_dict_path):
    """Saves processed data to a parquet file."""

    apps_meta_data.to_parquet(apps_meta_path,index=False)

    '''Saves the raw text file for later processing in JSON format'''
    with open(app_information_dict_path, 'w', encoding='utf-8') as f:
        json.dump(app_information_dict, f, indent=4)