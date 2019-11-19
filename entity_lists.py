import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
import entity_extractor



ee = entity_extractor.EntityExtractor()
STOP_WORDS = set(stopwords.words('english'))
pattern = re.compile('^[a-zA-Z_]*$')

def write_list(list, filename):
    with open(filename, 'w') as filehandle:
        for listitem in list:
            filehandle.write('%s\n' % listitem)


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_words(txt):
    return list(filter(
        lambda x: x.lower() not in STOP_WORDS and re.match(pattern, x) is not None, word_tokenize(txt.lower())
    ))

def unify_entities(text, list):
    for entity in list:
        entity = entity.strip()
        new = re.sub(r'\s+', '_', entity)
        text = text.replace(entity, new)
    return text

all_entities = []
person_entities = []
place_entities = []
organisation_entities = []
sentence_words = []
file_path = '/home/rcf-proj3/kl4/nmokhber/alfred/aws/processed/2019-02-08/2019-02-07.jl.v2'
lines_cnt = 1323348 #file_len(file_path)
articles=[]
with open (file_path, 'r') as json_file:
    for i in range(lines_cnt):
        obj = json.loads(json_file.readline())
        text = obj['knowledge_graph']['description'][0]['value']
        #text = text
        #list_ent = ee.extract_entities_dbpedia(text=text, confidence=0.2)
        list_ent = []
        if 'dbpedia_entities' not in obj:
            try:
                list_ent = ee.extract_entities_dbpedia(text=text, confidence=0.3)
            except:
                pass
        else:
            for entity in obj['dbpedia_entities']:
                list_ent.append(entity['surface_form'][0])
                type_list = entity['types']
                new = re.sub(r'\s+', '_', entity['surface_form'][0].strip().lower())
                if any('Person' in s for s in type_list):
                    person_entities.append(new)
                elif any('Place' in s for s in type_list):
                    place_entities.append(new)
                elif any('Organization' or 'Organisation' in s for s in type_list):
                    organisation_entities.append(new)

write_list(person_entities, 'person_entities.txt')
write_list(place_entities, 'place_entities.txt')
write_list(organisation_entities, 'organisation_entities.txt')

#model = Word2Vec(sentence_words, size=128, window=3, min_count=40, workers=2)
#model.wv.save_word2vec_format('word2vec_entity_unified.txt', binary=False)
#model.save('word2vec2.model')
#print(model.wv.vectors.shape)
#word = 'china'
#print(model.most_similar(word, topn=10))

