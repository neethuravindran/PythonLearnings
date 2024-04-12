import pandas as pd
import matplotlib.pyplot as plt

df_temp = pd.read_csv("Temp.csv")

x_moscow = df_temp["Moscow"]
x_san_Francisco = df_temp["San Francisco"]

plt.hist(x_moscow, len(x_moscow), facecolor='green', alpha=0.5)
plt.hist(x_san_Francisco, len(x_san_Francisco), facecolor='yellow', alpha=0.5)

plt.xlabel("Temp")
plt.ylabel("Freq")
plt.title("Temperature of Moscow vs San Francisco")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right')

plt.show()