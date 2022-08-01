#1
import pandas as pd
#pd.set_option('display.max_columns', None)

#2
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
titanic = pd.read_csv(path)

#3
print(titanic.head(10))
print()

#4
print(titanic.shape)

#5
print()

#6
print(titanic.info())

#7
print(titanic.describe())

#8
print(titanic.value_counts('Embarked'))
print(titanic.value_counts('Pclass'))

#9
print(titanic[['Age', 'Fare']].max())

#10
print(titanic.sort_values('Fare', ascending=False).head(10))