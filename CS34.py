import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Cars.csv')

df = df.drop(['Model', 'Type', 'LowPrice', 'HighPrice', 'Drive', 'CityMPG', 'HwyMPG', 'FuelCap', 'Length'], axis=1)
df = df.drop(['Width', 'Wheelbase', 'Height', 'UTurn', 'Weight', 'Acc030', 'Acc060'], axis=1)
df = df.drop(['QtrMile', 'PageNum', 'Size'], axis=1)

df['count'] = df.groupby('Make')['Make'].transform('count')
df.drop_duplicates('Make', inplace=True)
df.sort_values(by='count', ascending=False, inplace=True)

plt.figure(figsize=(400,100))
ax1 = plt.subplot(121, aspect='equal')
plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right')
df.plot(kind='pie', y='count', ax=ax1, autopct='%1.1f%%', startangle=90, shadow=False, labels=df['Make'], legend=False,
        fontsize=8)
plt.tight_layout()
plt.show()
