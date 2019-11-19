# TODO compare with the counts from dig gui
# TODO empty ones: bloomberg/ wall street journal/ boston globe/money
# TODO reuters/ economist/ forbes/ ap (associate press) ye chert o pertayi daare
# TODO it seems that since 2019 the data has gotten better
# TODO check for language field (knowledge graph) to be English
# TODO add patricks data

import os
import json
import pandas as pd


class Filter:
    """
        TODO
    """

    def __init__(self, liberal_path, conservative_path):
        self.df = pd.DataFrame(columns=['source', 'political_side', 'title', 'event_date', 'text'])
        with open(liberal_path, 'r') as f:
            self.liberal_sources = f.read().splitlines()
        with open(conservative_path, 'r') as f:
            self.conservative_sources = f.read().splitlines()
        print('init done')

    def filter_aws(self, aws_path='/home/rcf-proj3/kl4/nmokhber/alfred/aws',
                   filtered_path='/home/rcf-proj3/kl4/nmokhber/alfred/codes/filter_v1/data'):
        cnt_duplicate = 0
        for root, subdirs, files in os.walk(aws_path):
            for file in files:
                if '.jl.v2' in file:
                    lines_cnt = 0
                    file_path = os.path.join(root, file)
                    print('^^^^^^^^^^^')
                    print('root = ' + root)
                    print('file = ' + file)
                    with open(file_path, 'r') as json_file:
                        for line in json_file:
                            lines_cnt += 1
                            obj = json.loads(line)
                            try:
                                source = obj['knowledge_graph']['source'][0]['key']
                                title = obj['knowledge_graph']['title'][0]['key']
                                date = obj['knowledge_graph']['event_date'][0]['key']
                                text = obj['knowledge_graph']['description'][0]['value'].strip()
                                # language = obj['knowledge_graph']['language'][0]['key'] TODO check konam bebinam aya hame english ha label daran ya na
                            except:
                                continue
                            if any(substring in source for substring in self.liberal_sources):
                                political_side = 'l'
                            elif any(substring in source for substring in self.conservative_sources):
                                political_side = 'r'
                            else:
                                continue
                            # TODO Language Filtering
                            if 'espanol' in source or 'spanish' in source:
                                continue
                            # TODO Duplicate removing
                            # mini_text = text[0:int(len(text)/2)]
                            # if not self.df.empty:
                            #     if self.df['text'].str.contains(mini_text).any():
                            #         tmp = self.df['text'].str.contains(mini_text)
                            #         cnt_duplicate = cnt_duplicate + 1
                            #         continue
                            new_row = pd.DataFrame(
                                {'source': [source], 'political_side': [political_side], 'title': [title],
                                 'event_date': [date], 'text': [text]})
                            self.df = self.df.append(new_row, ignore_index=True)
                        print('lines count:  {}'.format(lines_cnt))
                        print('duplicate count: {}'.format(cnt_duplicate))
        self.df.to_csv(filtered_path, index=None, header=True)


# liberal_source = ['new york times', 'newyorktimes', 'washington post', 'washingtonpost', 'new yorker', 'newyorker',
#                   'politico', 'atlantic', 'cnn']
# center_source = ['foreign affairs', 'foreignaffairs']
# conservative_source = ['new york post', 'newyorkpost', 'spectator', 'washington times', 'washingtontimes']

# TODO balance the count randomly
filter = Filter('/home/rcf-proj3/kl4/nmokhber/alfred/v1/source_filters/liberal.txt',
                '/home/rcf-proj3/kl4/nmokhber/alfred/v1/source_filters/conservative.txt')
filter.filter_aws(aws_path='/home/rcf-proj3/kl4/nmokhber/alfred/v1/aws_v1',
                  filtered_path='/home/rcf-proj3/kl4/nmokhber/alfred/v1/data_v1/filtered_v1.csv')
