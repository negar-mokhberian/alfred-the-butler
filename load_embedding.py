from gensim.models import KeyedVectors
import os

models_path = '/Users/nmokhber/Documents/ISI/Alfred/codes/filter_v1/models'
model_file = 'word2vec_entity_unified.txt'
wv_model = KeyedVectors.load_word2vec_format(os.path.join(models_path, model_file), binary=False)
print(wv_model.most_similar(positive=['l_barack_obama'], topn = 10))
print(wv_model.most_similar(positive=['r_barack_obama'], topn = 10))
print(wv_model.most_similar(positive=['l_donald_trump'], topn = 10))
print(wv_model.most_similar(positive=['r_donald_trump'], topn = 10))
while True:
    w = input("\nEnter a word : ")
    print(wv_model.most_similar(positive=[w], topn=10))
#print(wv_model.similarity('l_barack_obama', 'r_barack_obama'))
#print(wv_model.similarity('l_donald_trump', 'r_donald_trump'))
#print(wv_model.similarity('l_messina', 'r_messina'))
#print('tamaam')