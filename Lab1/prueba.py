import pandas as pd


titanic = pd.read_csv("./titanic.csv", header=0, delimiter=',')
Q1 = titanic['fare'].quantile(0.25)
Q3 = titanic['fare'].quantile(0.75)
IQR = Q3 - Q1

small_outliers = titanic['fare'] < (Q1 - 1.5 * IQR)
big_outliers = titanic['fare'] > (Q3 + 1.5 * IQR)

cosa = titanic['fare'] [small_outliers | big_outliers]
#print (list(small_outliers))
print(type(titanic['fare']))
print(type(small_outliers))
#print(small_outliers)
#print(big_outliers)
#print(titanic['fare'])
#print(cosa)