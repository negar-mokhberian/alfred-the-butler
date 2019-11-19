import pandas as pd
import os
from word_embedding import WordEmbedding


def main():
    path = '/home/negar/alfred/developement/Kaggle'
    #path = '/Users/nmokhber/Documents/ISI/Alfred/developement/Kaggle'
    all_data = pd.read_csv(os.path.join(path, 'data/kaggle.csv'))
    list_terms = pd.read_csv(os.path.join(path, 'data/common.csv'))
    WE = WordEmbedding(list_terms=list_terms.entity.loc[0:199]) # TODO more than 200
    print('starting processing texts...')
    processed_texts = all_data.apply(WE.unify_terms, axis=1)
    #all_data['processed_text'].tolist()
    all_data = None
    print('starting the embedding...')
    model = WE.calc_word2vec(processed_texts, size=100, window=7, min_count=15, workers=5)
    print('words embedded for articles...')

    WE.save_word2vec(model, os.path.join(path, 'models/word2vec_total.txt'))
    print('embeddings saved')


if __name__ == '__main__':
    main()
