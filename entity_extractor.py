import spacy
import requests


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
        # dbpedia spotlight
        self._spotlight_search_url = 'http://model.dbpedia-spotlight.org/en/annotate'
        # spacy
        self._nlp = spacy.load('en_core_web_sm') 


    def extract_entities_dbpedia(self, text: str, confidence=0.5, filter=['Person', 'Place', 'Organisation']):
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
        r = requests.post(self._spotlight_search_url,
                          data=search_data,
                          headers=search_headers)
        results = r.json()
        for resource in results['Resources']:
            entities.append(resource['@surfaceForm'])
        return entities

    
    def extract_entities_spacy(self, text: str, filter = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC']):
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
            if entity.label_ in filter:
                entities.append(entity.text)
        return entities
