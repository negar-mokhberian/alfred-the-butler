import pickle
from os import listdir
from os.path import isfile, join
import pandas as pd


def main():
    mypath = '/Users/nmokhber/Documents/ISI/Alfred/filter_v1/data/column_parts'
    # col_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # col_files = sorted(col_files)
    col_files = []
    for i in range(1, 20):
        col_files.append('column{}.txt'.format(i))
    col = []
    for col_f in col_files:
        print(col_f)
        with open(join(mypath, col_f), 'rb') as f:
            tmp_col = pickle.load(f)
            print(len(tmp_col))
            col.extend(tmp_col)
    print(len(col))
    all_data = pd.read_csv('./data/kaggle_processed.csv')
    all_data = all_data.iloc[0:len(col)]
    all_data['processed_text'] = col

    all_data.to_csv('./data/kaggle_important.csv', index=None, header=True)
    print('done')


if __name__ == '__main__':
    main()
