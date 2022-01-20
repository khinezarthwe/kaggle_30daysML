import os

import pandas as pd


train_data = pd.read_csv(os.path.dirname(__file__) + '/data/train.csv', index_col='id')
test_data = pd.read_csv(os.path.dirname(__file__) + '/data/test.csv', index_col='id')

print(train_data.head())
print(test_data.head())


