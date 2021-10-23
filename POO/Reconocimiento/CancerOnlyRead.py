import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('POO\Reconocimiento\data.csv')

x = df.diagnosis.value_counts()

labels = [ "Benign","Malignant"]

plt.pie(x, labels =labels, autopct = '%.0f%%')
plt.show()

print(df.corr())

df_mean = df.loc[: , 'radius_mean' : "fractal_dimension_mean" ] 

print(df_mean)

print(df_mean.corr())

corr = df_mean.corr()

plt.figure(figsize=(10,8))

sns.heatmap(corr,  cmap= "Greens", linewidths=1.25 )

plt.show()

se_df = df.loc[:, "radius_se" : "fractal_dimension_se"]

print(se_df.corr())

plt.figure(figsize=(10,8))

sns.heatmap(se_df.corr(),  cmap= "Blues", linewidths=1.25, linecolor= "black" )

plt.show()