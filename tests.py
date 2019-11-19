#
# import re
# import os
# import gensim.models as gm
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize, word_tokenize
# from gensim.models import KeyedVectors
#
#
#
# file_path='/Users/nmokhber/Documents/ISI/Alfred/filter_v1/models/word2vec_entity_unified.txt'
# model = KeyedVectors.load_word2vec_format(file_path, binary=False)
# print(model.most_similar(positive='l_guatemala', topn=10))
# print(model.most_similar(positive='r_guatemala', topn=10))
#
# # TODO limit it to the entities
# # TODO also look at it after projection

import sys
lines = []
i = 0
for line in sys.stdin:
    #print(line, end="")
    lines.append(line)
    i  = i +1
    if i > 1:
        break

k = int(lines[0])
array = lines[1].split(' ')
print(array)
array = [int(x.strip()) for x in array]
print(array)
print(type(array))


#!/bin/bash
#SBATCH --nodes=1
#SBATCH --mem=32gb
#SBATCH -t 3:59:59

source /home/rcf-proj3/kl4/nmokhber/alfred/alfred_venv/bin/activate
cd /home/rcf-proj3/kl4/nmokhber/alfred/codes/
