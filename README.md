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
##### Args:
- text (str): text input to be annotated
- confidence (float): the confidence of the annotation, ranging from 0 to 1. Setting a high confidence threshold instructs DBpedia Spotlight to avoid incorrect annotations as much as possible at the risk of losing some correct ones.
- filter (List[str]): The types of entities to be extracted.
##### Returns:
- entities (List[str])
### Spacy
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

```
A total 330,000 compressors were imported to China in July 2005, down almost 50 pct year-on-year, it was reported on September 12, 2005. 

 The reason for the decrease is the large inventories of compressors accumulated at Chinese air-conditioner manufacturers. 

 The biggest sources of China's compressor imports were Japan, Malaysia and Taiwan during the month. Malaysia alone imported 60,000 compressors to China in July 2005, up 175 pct year-on-year. The other two major sources of compressors saw a decrease of over 30 pct in their imports to China. 

 The biggest importer in July was air-conditioner manufacturer Shanghai Sharp, with some 53,000 imported compressors, followed by Fujitsu General, Haier and Gree. 
^^^^dbpedia^^^^
['China', 'Chinese', 'China', 'Japan', 'Malaysia', 'Taiwan', 'Malaysia', 'China', 'China', 'Shanghai', 'Sharp', 'Fujitsu General', 'Haier']
^^^^spacy^^^^
['China', 'Chinese', 'China', 'Japan', 'Malaysia', 'Taiwan', 'Malaysia', 'China', 'China', 'Shanghai Sharp', 'Fujitsu General', 'Haier', 'Gree']
```
