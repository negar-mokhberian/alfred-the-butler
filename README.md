# alfred-the-butler
### class: EntityExtractor
There are no inputs needed for making an instance of this class. An example of making an instance of this class is as follow:
__entity_extractor = EntityExtractor()__
This extractor uses either DBPedia Spotlight API or Spacy package to annotate words and phrases in a text input.
####DBPedia
        extract_entities_dbpedia(self, text: str, confidence=0.5, filter=['Person', 'Place', 'Organisation'])
Extract entities using DBpedia Spotlight API to annotate the input text. Confidence specifies the and fields filter to be used.
__Example:__ 
        entity_extractor.extract_entities_dbpedia(text=input_doc, confidence = 0.6)
__Args:__
- text (str): text input to be annotated
- confidence (float): the confidence of the annotation, ranging from 0 to 1. Setting a high confidence threshold instructs DBpedia Spotlight to avoid incorrect annotations as much as possible at the risk of losing some correct ones.
- filter (List[str]): The types of entities to be extracted.
__Returns:__
    entities (List[str])
####Spacy
        extract_entities_spacy(self, text: str, filter = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC'])
 Extract entities using Spacy package from the input text.
__Example:__ 
        entity_extractor.extract_entities_spacy(text=input_doc)
__Args:__
                -text (str): text input to be annotated
                -filter (List[str]): the types of entities to be extracted
__Returns:__
                entities (List[str])
