import pandas as pd
from prompts import PromptsDataCollection
from data_saver import save_data
from dotenv import load_dotenv
import google.generativeai as genai
import os
import time

def geminiResponse(model,prompt):
    response =  model.generate_content(
                prompt,
                generation_config = genai.types.GenerationConfig(
                        candidate_count = 1,
                        top_p=0.5,
                        top_k=1,
                        temperature=0
                    )    
                )
    return(response.text)

def extractInformation(text):
    fields = [""]*4  # four fields -- summary,features,adjectives,search_term
 
    # finding all the text between summary and features, doing the same for others as well
    start_marker = ["summary: ","features: ","adjectives: ","search_term: "]
    end_marker   = ["features:","adjectives","search_term"]
    len_prefix   = [9,10,12,13]        #  size of the start markers to ensure to add to the text starting point

    for f in range(3):
        start_ind = text.index(start_marker[f])
        end_ind   = text.index(end_marker[f])
        fields[f] = text[start_ind+len_prefix[f]:end_ind]
    
    start_ind = text.index(start_marker[3])
    fields[3] = text[start_ind+len_prefix[-1]:]

    return(fields)

def process_data(apps_meta_data,apps_meta_path,app_information_dict,app_information_dict_path):

    # Load environment variables from .env file
    load_dotenv()
    # setting up the gemini model
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    geminiModel = genai.GenerativeModel('gemini-1.5-pro')
    prompt      = PromptsDataCollection()

    count       = 0     # do only 1000 per day
    count_fail  = 0     # to check if we exceed the gemini RPM

    for r in range(len(apps_meta_data)):
        if count > 1000 or count_fail > 5:
            break

        app_package = apps_meta_data['app_package'].iloc[r]

        if app_package not in app_information_dict.keys():
            prompt.name     = apps_meta_data['app_name'].iloc[r]
            prompt.descript = apps_meta_data['description'].iloc[r]

            try:
                response = geminiModel.geminiResponse(prompt,None)
                app_information_dict[app_package] = response
                time.sleep(3)    # waiting for 3 seconds to avoid crossing the RPM threshold
                count += 1
                save_data(apps_meta_data,apps_meta_path,app_information_dict,app_information_dict_path)
            except:
                count_fail += 1  # counting the time of failure
                r -= 1           # going to this loop again
            
