import pandas as pd
import os
import json

# diffs = pd.read_pickle("./models/diffs.pkl")

path = '/Users/nmokhber/Documents/ISI/Alfred/filter_v1/data'
data = pd.DataFrame(columns=['source', 'political_side', 'title', 'language', 'event_date', 'text'])

for root, subdirs, files in os.walk(path):
    for file in files:
        if not file.startswith('filter'):
            continue
        file_path = os.path.join(root, file)
        print('^^^^^^^^^^^')
        print('root = ' + root)
        print('file = ' + file)
        with open(file_path, 'r') as json_file:
            for line in json_file:
                obj = json.loads(line)
                try:
                    text = obj['knowledge_graph']['description'][0]['value']
                except:
                    text = None  # TODO np.nan ?
                try:
                    title = obj['knowledge_graph']['title'][0]['value']
                except:
                    title = None
                try:
                    date = obj['knowledge_graph']['event_date'][0]['key']
                except:
                    date = None
                try:
                    political_side = obj['knowledge_graph']['political_side']
                except:
                    political_side = None
                try:
                    language = obj['knowledge_graph']['language'][0]['key']
                except:
                    language = None
                try:
                    source = obj['knowledge_graph']['source'][0]['key']
                except:
                    source = None
                if 'espanol' in source:
                    continue
                new_row = pd.DataFrame(
                    {'source': [source], 'political_side': [political_side], 'title': [title], 'language': [language],
                     'event_date': [date], 'text': [text]})
                data = data.append(new_row, ignore_index=True)
                #print('one row')

data.to_csv(r'data/dataframe3.csv', index=None, header=True)