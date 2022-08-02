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
print(titanic.loc[:,['Name', 'Age', 'Sex']])

#5
print(titanic[['Name', 'Age', 'Sex']].head(10))
print(titanic.loc[0:9, ['Name', 'Age', 'Sex']]) # 0:9 일때 8이 아니라 9로 나옴(범위 말고 행 이름으로 생각)

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
print(titanic.loc[titanic['Age'].between(10, 20, inclusive='left')]['Fare'].mean())
print(titanic.loc[titanic['Age'].between(10, 20, inclusive='left'), ['Fare']].mean())