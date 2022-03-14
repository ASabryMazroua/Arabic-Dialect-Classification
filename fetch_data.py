import json
import math
import requests
import pandas as pd

def fetch_data(ids):
    '''
    A function to fetch data from the API.
    
        Parameters:
                ids (list): A list of ids (integrs) to fetch

        Returns:
                text (dict): A dictionary where keys are the ids and values are the text
        
    '''
    results = {}  
    # We'll loop over the ids to fetch the text data
    # We'll split ids into 1000 because of the limit of the API
    # Futrue work: 
    #    we can handle if the connection timed out or any other problem that would happen
    #    we can add some assertion to make sure that ids are valid
    for i in range(math.ceil(len(ids)/1000)):
        sub_ids = json.dumps(ids[i*1000:1000*(i+1)])
        while True:
            r = requests.post("https://recruitment.aimtechnologies.co/ai-tasks", sub_ids)
            # print(r.status_code)
            if r.status_code == 200:
                results.update(json.loads(r.text))
                break;
        print(f"We managed to fetch {len(results)} samples of text.")
    return results

if __name__ == '__main__':
    #Read the ids' file, then fetch data, and write the file to a csv
    source_data = pd.read_csv("files/dialect_dataset.csv")
    text_dict = fetch_data(list(source_data.loc[:,"id"].astype(str)))
    #We'll make sure that we managed to fetch all the ids
    if len(source_data) == len(text_dict):
        source_data.loc[:,"text"] = text_dict.values()
        source_data.to_csv("data/full_dialect_dataset.csv",encoding='utf-8-sig')        