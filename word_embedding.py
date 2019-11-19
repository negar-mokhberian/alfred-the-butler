import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import KeyedVectors, Word2Vec


class WordEmbedding:

    def __init__(self, model=None, list_terms=None):
        self.list_terms = list_terms
        self.STOP_WORDS = set(stopwords.words('english'))
        self.pattern = re.compile('^[a-zA-Z_]*$')  # TODO add dot? add it to entity extraction
        if model is not None:
            self.model = model
        else:
            self.model = None
        if list_terms is not None:
            self.list_terms = list_terms
        else:
            self.list_terms = None
        # TODO self.labeled_terms = None  # TODO
        # TODO self.pairs = list(map(lambda x: ('l_' + x, 'r_' + x), self.labeled_terms))

    # TODO filter and list?
    def get_words(self, txt):
        return list(filter(
            lambda x: x not in self.STOP_WORDS and re.match(self.pattern, x) is not None, word_tokenize(txt)
        ))

    def text_to_sentence_words(self, text):
        sent_words = list(map(self.get_words, sent_tokenize(text.lower())))
        sent_words = list(filter(lambda sw: len(sw) > 1, sent_words))
        return sent_words

    # TODO what is workers?

    def save_word2vec(self, model, path='models/word2vec_entity_unified.txt'):
        model.wv.save_word2vec_format(path, binary=False)

    def calc_word2vec(self, list_articles, size=128, window=5, min_count=10, workers=4):
        sentence_words = []
        # TODO make it more compact and efficient?
        for text in list_articles:
            sent_words = self.text_to_sentence_words(text)
            if len(sent_words) > 1:
                sentence_words.extend(sent_words)
        print('sentence words lists are calculated')
        print(type(sentence_words))
        self.model = Word2Vec(sentence_words, size=size, window=window, min_count=min_count, workers=workers)
        return self.model

    def load_embedding(self,
                       file_path='/Users/nmokhber/Documents/ISI/Alfred/codes/filter_v1/models/word2vec_entity_unified.txt'):
        self.model = KeyedVectors.load_word2vec_format(file_path, binary=False)
        return self.model

    def most_similar_w2vec(self, word, cnt=10):
        print('hey')
        return self.model.most_similar(positive=[word], topn=cnt)
        # most_similar_to_given(entity1, entities_list) Get the entity from entities_list most similar to entity1.

    # TODO generalize and use other kind of embeddings
    # print(wv_model.most_similar(positive=['l_barack_obama'], topn = 10))
    # print(wv_model.most_similar(positive=['r_barack_obama'], topn = 10))
    # print(wv_model.most_similar(positive=['l_donald_trump'], topn = 10))
    # print(wv_model.most_similar(positive=['r_donald_trump'], topn = 10))
    # while True:
    #     w = input("\nEnter a word : ")
    #     print()

    # TODO new, should be tested check with both load and train
    def calc_cos_sim_labeled(self):
        return list(map(lambda x: self.model.similarity(x[0], x[1]), self.pairs))  # TODO should the wv be here?

    # TODO take care if term does not exist in one of them

    def calc_diffs_labeled(self, model1, model2, terms):  # TODO havaset bashe ke jahat mohemme
        # return list(map(lambda x: self.model.wv[x[0]] - self.model.wv[x[1]], self.pairs))
        return dict(map(lambda x: (x, model2.wv[x] - model1.wv[x]), terms))

    # TODO maybe I need to use wordvec for getting the vector?
    # TODO shape diffs ro check konam

    def unify_terms(self, row):
        text = row['text']
        political = row['political_side']
        common = set(word_tokenize(text)) & set(self.list_terms)
        for term in common:
            new_term = row['political_side'] + '_' + re.sub(r'\s+', '_', term.strip())
            try:
                text = re.sub(r'\b%s\b' % term, ' ' + new_term + ' ', text)
            except:
                continue
        return re.sub(r'\s+', ' ', text)


# TODO fekr konam yeki az diff ha joftesh ro peyda nemikone, barresi kon ke chera

# rank(entity1, entity2)
# Rank of the distance of entity2 from entity1, in relation to distances of all entities from entity1.

# word_vec(word, use_norm=False)
# Get word representations in vector space, as a 1D numpy array.
#
# Parameters:
# word (str) – Input word
# use_norm (bool, optional) – If True - resulting vector will be L2-normalized (unit euclidean length).
# Returns:
# Vector representation of word.
#
# Return type:
# numpy.ndarray
#
# Raises:
# KeyError – If word and all ngrams not in vocabulary.

# distance(w1, w2)
# #Compute cosine distance between twowords.Calculate 1 - similarity().
