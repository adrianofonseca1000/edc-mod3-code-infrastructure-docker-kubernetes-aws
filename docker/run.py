import pandas as pd

#url = 'https://raw.githubusercontent.com/jbronlee/Datasets/master/pima-indians-diabetes.data.csv'

url = 'https://raw.githubusercontent.com/adrianofonseca1000/random-forest-classifier-dataset-titanic/master/data/titanic_data.csv'

df = pd.read_csv(url)

print(df.columns)

print(df.head())

print(df.shape)
