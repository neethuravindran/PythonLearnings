import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

df_school_data = pd.read_csv("school.csv")
# print(df_school_data.head())
df_school_data.describe()

df_grouped_data = df_school_data.groupby("school_rating").describe()
print(df_grouped_data.head())

corrmat = df_grouped_data.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)

plt.scatter(df_school_data["school_rating"], df_school_data["reduced_lunch"])
plt.grid()
plt.xlabel("Rating")
plt.ylabel("Reduced lunch")
plt.title("School rating vs Reduced lunch")
plt.show()