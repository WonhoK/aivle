#1
import pandas as pd
#pd.set_option('display.max_columns', None)

#2
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
titanic = pd.read_csv(path)

#3
print(titanic['Name'])

#4
print(titanic[['Name', 'Age', 'Sex']])

#5
print(titanic[['Name', 'Age', 'Sex']].head(10))

#6
print(titanic.loc[titanic['Age'] >= 70])

#7
Fare_mean = titanic['Fare'].mean()
print(Fare_mean)

#8
print(titanic.loc[titanic['Fare'] < Fare_mean])

#9
print(titanic.loc[titanic['Embarked'].isin(['Southhampton', 'Queenstown'])])

#10
print(titanic['Fare'].loc[titanic['Age'].between(10, 20, inclusive='left')].mean())