import numpy as np
import pandas as pd

# CS1
data = pd.read_csv('SalaryGender.csv')
print(data.head())

sal = np.array(data['Salary'].values)
print(sal)

gen = np.array(data['Gender'].values)
print(gen)

age = np.array(data['Age'].values)
print(age)

deg = np.array(data['Degree'].values)
print(deg)

# CS2

men = np.where(gen == 'male')
wmen = np.where(gen == 'female')
phd = np.where(deg == 'phd')
mphd = np.isin(men, phd)
wmphd = np.isin(wmen, phd)
print("The number of men with a PhD : " + str(np.count_nonzero(mphd)))
print("The number of women with a PhD : " + str(np.count_nonzero(wmphd)))

# CS3
age = pd.DataFrame(age)
deg = pd.DataFrame(deg)
data = data[data['Degree'] != 'phd']
print(data.head(100))

#CS4
print("The number of people having PhD is:", len(data.index))
