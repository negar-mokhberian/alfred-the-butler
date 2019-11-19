import pandas as pd
import pickle
from entity_extractor import EntityExtractor

def main():
    col = []
    ee = EntityExtractor()
    i = 1
    while i < 22:
        print('started the process {}'.format(i))
        sub = pd.read_csv('./data/chunks/chunk{}.txt'.format(i))
        print(sub.shape[0])
        processed = sub.apply(ee.unify_entities_spacy, 1)
        #col.extend(processed)
        with open('./data/column_parts/column{}.txt'.format(i), 'wb') as fp:
            pickle.dump(processed, fp)
        i += 1

if __name__ == '__main__':
    main()
