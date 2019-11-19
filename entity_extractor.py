import spacy
import requests
import logging
import re
import collections
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class EntityExtractor:
    """
    **Description**
        This extractor takes a string of text as input, uses either DBPedia API or Spacy to annotate words and phrases in the text input.
    Examples:
            entity_extractor = EntityExtractor()
            entity_extractor.extract_entities_dbpedia(text=input_doc, confidence = 0.6)
            entity_extractor.extract_entities_spacy(text=input_doc)
    """

    def __init__(self):
        self.pattern = re.compile('^[a-zA-Z_]*$')  # TODO add dot? add it to entity extraction
        # dbpedia spotlight
        self._spotlight_search_url = 'http://model.dbpedia-spotlight.org/en/annotate'

        # spacy
        self._nlp = spacy.load('en_core_web_md')  # TODO not the small one?

    def retry_extract_entities_dbpedia(self, text: str, confidence=0.5, filter=['Person', 'Place', 'Organisation']):
        """
           Extract entities using DBpedia Spotlight API with the input text, confidence and fields filter to be used.
           Args:
               text (str): text input to be annotated
               confidence (float): the confidence of the annotation
               filter (List[str]): the types of entities to be extracted
           Returns:
               entities (List[str])
        """
        entities = []
        filter = ','.join(filter)
        search_data = [('confidence', confidence),
                       ('text', text),
                       ('types', filter)]
        search_headers = {'Accept': 'application/json'}
        logging.basicConfig(level=logging.DEBUG)
        s = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        s.mount('http://', HTTPAdapter(max_retries=retries))
        r = s.post(self._spotlight_search_url,
                   data=search_data,
                   headers=search_headers)
        results = r.json()
        for resource in results['Resources']:
            entities.append(resource['@surfaceForm'])
        # s.get("http://httpstat.us/503")
        return entities

    def extract_entities_dbpedia(self, text: str, confidence=0.5, filter=['Person', 'Place', 'Organisation']):
        entities = []
        filter = ','.join(filter)
        search_data = [('confidence', confidence),
                       ('text', text),
                       ('types', filter)]
        search_headers = {'Accept': 'application/json'}
        r = requests.post(self._spotlight_search_url,
                          data=search_data,
                          headers=search_headers)
        results = r.json()
        for resource in results['Resources']:
            entities.append(resource['@surfaceForm'])
        return entities

    def is_entity(self, word):
        doc = self._nlp(word)
        for entity in doc.ents:
            if entity.text == word:
                return True
        return False

    def extract_entities_spacy(self, text: str, filter=['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC']):
        """
            Extract entities using Spacy with the input text to be used.
            Args:
                text (str): text input to be annotated
                filter (List[str]): the types of entities to be extracted
            Returns:
                entities (List[str])
        """
        entities = []
        doc = self._nlp(text)
        for entity in doc.ents:
            entity_text = entity.text.replace('.', '')
            entity_text = entity.text.replace('\'s', '')
            if entity_text.endswith('s') and self.is_entity(entity_text[:-1]):
                entity_text = entity_text[:-1]
            if entity.label_ in filter and re.match(self.pattern, entity_text) is not None:
                entities.append(entity_text)
        return entities

    def unify_entities_spacy(self, row):
        text = row['text']
        ent_set = set(self.extract_entities_spacy(text))
        for entity in ent_set:
            new_ent = row['political_side'] + '_' + re.sub(r'\s+', '_', entity.strip())
            try:
                text = re.sub(r'\b%s\b' % entity, ' ' + new_ent + ' ', text)
            except:
                continue
        return re.sub(r'\s+', ' ', text)

    def extract_all_entities_spacy(self, articles):
        ent_list = list(map(self.extract_entities_spacy, articles))
        # for text in articles:
        flat_list = [item for sublist in ent_list for item in sublist]
        counter = collections.Counter(flat_list)
        return counter.most_common()
