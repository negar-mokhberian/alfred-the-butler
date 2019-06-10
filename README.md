# alfred-the-butler
## class: EntityExtractor
This class gives tools to annotate words and phrases in a text input. These tools are DBPedia Spotlight API and Spacy package. There are no inputs needed for making an instance of this class. An example of making an instance of this class is as follow:
```
entity_extractor = EntityExtractor()
```
### DBPedia
Extract list of entities using DBpedia Spotlight API to annotate the input text. 
##### Example: 


        ```
        entity_extractor.extract_entities_dbpedia(text=input_doc, confidence = 0.6)
        ```
#####Args:
- text (str): text input to be annotated
- confidence (float): the confidence of the annotation, ranging from 0 to 1. Setting a high confidence threshold instructs DBpedia Spotlight to avoid incorrect annotations as much as possible at the risk of losing some correct ones.
- filter (List[str]): The types of entities to be extracted.
##### Returns:
- entities (List[str])
####Spacy
Extract entities using Spacy package from the input text.
##### Example:
```
        entity_extractor.extract_entities_spacy(text=input_doc)
```
##### Args:
- text (str): text input to be annotated
- filter (List[str]): the types of entities to be extracted
##### Returns:
- entities (List[str])
