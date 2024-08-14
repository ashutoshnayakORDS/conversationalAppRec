from data_loader import load_data
from llm_processor import process_data

def main():
    apps_meta_path            = "../../data/review/app_meta.parquet"      
    app_information_dict_path = "../../data/review/app_information_dict.json"

    apps_meta_data,app_information_dict = load_data(apps_meta_path,app_information_dict_path)
    apps_meta_data['summary']     = ""       # initializing for updates
    apps_meta_data['features']    = ""
    apps_meta_data['adjectives']  = ""
    apps_meta_data['search_term'] = ""
    process_data(apps_meta_data,apps_meta_path,app_information_dict,app_information_dict_path)

if __name__ == "__main__":
    main()