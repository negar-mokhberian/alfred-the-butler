import pandas as pd
import os
from word_embedding import WordEmbedding


def main():
    path = '/home/negar/alfred/developement/Kaggle'
    all_data = pd.read_csv(os.path.join(path, '/data/kaggle_processed.csv'))
    data_left = all_data[all_data['political_side'] == 'l']
    print(data_left.shape)
    data_right = all_data[all_data['political_side'] == 'r']
    print(data_right.shape)

    WE = WordEmbedding()
    l_model = WE.calc_word2vec(data_left['text'], size=100, window=7, min_count=15, workers=5)
    print('words embedded for left articles...')
    r_model = WE.calc_word2vec(data_right['text'], size=100, window=7, min_count=15, workers=5)
    print('words embedded for right articles...')
    WE.save_word2vec(l_model, os.path.join(path, '/models/word2vec_left.txt'))
    WE.save_word2vec(r_model, os.path.join(path, '/models/word2vec_right.txt'))
    print('embeddings saved')

    # TODO lemmatizing and stemming?


if __name__ == '__main__':
    main()
