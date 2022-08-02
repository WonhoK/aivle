#1
import pandas as pd
import numpy as np
#pd.set_option('display.max_columns', None)

#2
path = 'https://bit.ly/TitanicFile'
data = pd.read_csv(path)

#3
print(data.head())

#4
#4-1
data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

#4-2
data.rename(columns={'Sex' : 'Male'}, inplace=True)

#4-3
data['Male'] = data['Male'].map({'male' : 1, 'female' : 0})

#4-4
data['Family'] = data['SibSp'] + data['Parch']

#4-5
data.drop(['SibSp', 'Parch'], axis = 1, inplace=True)

#4-6
print(data.head())

#5
bin = range(0, 100, 10)
data['Age_Group'] = pd.cut(data['Age'], bins=bin, right=False,
                           labels=['유아', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대'])
print(data.head())
print(data.groupby('Age_Group', as_index=False)['Age'].agg(['min', 'max']))