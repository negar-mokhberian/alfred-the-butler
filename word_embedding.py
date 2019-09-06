import json
import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import gensim.models as gm
import entity_extractor

ee = entity_extractor.EntityExtractor()
STOP_WORDS = set(stopwords.words('english'))
pattern = re.compile('^[a-zA-Z_]*$')

def get_words(txt):
    return list(filter(
        lambda x: x.lower() not in STOP_WORDS and re.match(pattern, x) is not None, word_tokenize(txt.lower())
    ))

def unify_entities_poitical(text, list, political):
    for entity in list:
        entity = entity.strip()
        new = re.sub(r'\s+', '_', entity)
        new = political + '_' + new
        text = text.replace(entity, new)
    return text

sentence_words = []
#path = '/Users/nmokhber/Documents/ISI/Alfred/aws'
path = '/auto/rcf-proj3/kl4/nmokhber/alfred/aws'

for root, subdirs, files in os.walk(path):
    for file in files:
        if 'filter' in file and 'filtered_v1' in root:
            file_path = os.path.join(root, file)
            print('^^^^^^^^^^^')
            print('root = ' + root)
            print('file = ' + file)
            with open(file_path, 'r') as json_file:
                for line in json_file:
                        obj = json.loads(line)
                        text = obj['knowledge_graph']['description'][0]['value']
                        list_ent = []
                        # TODO get spacy event entities and look how they are in embedding ('war'?)
                        if 'dbpedia_entities' not in obj:
                            try:
                                list_ent = ee.extract_entities_dbpedia(text=text, confidence=0.3)
                            except:
                                pass
                        else:
                            for entity in obj['dbpedia_entities']:
                                list_ent.append(entity['surface_form'][0])
                        if len(list_ent) == 0:
                                    continue
                        political = obj['knowledge_graph']['political_side']
                        text = unify_entities_poitical(text, list_ent, political).lower() # TODO is lower() making any problem?
                        sent_words = list(map(get_words, sent_tokenize(text)))
                        sent_words = list(filter(lambda sw: len(sw) > 1, sent_words))
                        if len(sent_words) > 1:
                            sentence_words += sent_words

print('~~~~starting embedding')
model = gm.Word2Vec(sentence_words, size=128, window=3, min_count=10, workers=2) #TODO window size
model.wv.save_word2vec_format('word2vec_entity_unified.txt', binary=False)
model.wv.save_word2vec_format('word2vec_entity_unified_binary.txt')
model.save('word2vec2.model')
model.wv.save('w2v.txt')
print('tamaam')
