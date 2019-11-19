import pandas as pd
from entity_extractor import EntityExtractor

def main():
    #all_data = pd.read_csv('/Users/nmokhber/Documents/ISI/Alfred/developement/Kaggle/data/kaggle.csv')
    # all_data = pd.read_csv('/home/negar/alfred/developement/Kaggle/data/kaggle.csv')
    # data_left = all_data[all_data['political_side'] == 'l']
    # print(data_left.shape)
    # data_right = all_data[all_data['political_side'] == 'r']
    # print(data_right.shape)
    # ee = EntityExtractor()
    # left_tuples = ee.extract_all_entities_spacy(data_left['text'].tolist())
    # df_l = pd.DataFrame.from_records(left_tuples, columns=['entity', 'count'])
    # print('left calculated...')
    # right_tuples = ee.extract_all_entities_spacy(data_right['text'].tolist())
    # df_r = pd.DataFrame.from_records(right_tuples, columns=['entity', 'count'])
    # print('right calculated...')
    # df_l.to_csv('/home/negar/alfred/developement/Kaggle/data/entities_left.csv', index=None, header=True)
    # df_r.to_csv('/home/negar/alfred/developement/Kaggle/data/entities_right.csv', index=None, header=True)
    # print('df left and df right have been saved :)')
    df_l = pd.read_csv('/Users/nmokhber/Documents/ISI/Alfred/developement/Kaggle/data/entities_left.csv')
    df_r = pd.read_csv('/Users/nmokhber/Documents/ISI/Alfred/developement/Kaggle/data/entities_right.csv')
    common = pd.merge(df_l, df_r, on=['entity'])
    common['count'] = common['Count_x']+common['Count_y']
    common = common[['entity', 'count']]
    common.columns = ['entity', 'count']
    common = common.sort_values(by=['count'],  ascending=False)
    #common.to_csv('/Users/nmokhber/Documents/ISI/Alfred/developement/Kaggle/data/common.csv', index=None, header=True)
    common.to_csv('/home/negar/alfred/developement/Kaggle/data/entities_left.csv', index=None, header=True)
    print('finish')


if __name__ == '__main__':
    main()