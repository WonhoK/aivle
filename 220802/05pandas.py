#1
import pandas as pd
#pd.set_option('display.max_columns', None)

#2
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
titanic = pd.read_csv(path)

#3
print(titanic['Fare'].median())

#4
print(titanic.groupby('Embarked', as_index=False)['Fare'].mean())

#5
tmp = titanic.groupby(['Embarked', 'Sex'], as_index=False)[['Fare', 'Age']].mean()
print(tmp)

#7
print(titanic.groupby(['Embarked', 'Survived'], as_index=False)[['Fare', 'Age']].agg(['max', 'min', 'mean', 'std']))
