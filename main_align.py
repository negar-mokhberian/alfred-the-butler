import pandas as pd
from word_embedding import WordEmbedding
from gensim_word2vec_procrustes_align import smart_procrustes_align_gensim

def main():
    WE = WordEmbedding()
    model_l = WE.load_embedding('./models/word2vec_left.txt')
    model_r = WE.load_embedding('./models/word2vec_right.txt')
    model_r_aligned = smart_procrustes_align_gensim(model_l, model_r)

    WE.save_word2vec(model_r, './models/aligned_word2vec_right.txt')
    print('embeddings saved')

    # TODO lemmatizing and stemming?

if __name__ == '__main__':
    main()
