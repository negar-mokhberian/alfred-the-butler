import pandas as pd
import pickle

from jedi.evaluate.syntax_tree import eval_subscript_list


def main():
    all_data = pd.read_csv('./data/kaggle_processed.csv')
    # split data
    sub_data = all_data[['text', 'political_side']]
    print(sub_data.shape[0])
    length = int(sub_data.shape[0]/20)
    i = 0
    j = 0
    tot = 0
    while i < sub_data.shape[0]:
        j += 1
        if i + length < sub_data.shape[0]:
            sub_sub = sub_data.iloc[i:(i + length)]
        else:
            sub_sub = sub_data.iloc[i:]
        tot += sub_sub.shape[0]
        sub_sub.to_csv('./data/chunks/chunk{}.txt'.format(j), index=None, header=True)
        i += length
    print(tot)

if __name__ == '__main__':
    main()
