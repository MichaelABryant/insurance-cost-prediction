import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

df = pd.read_csv('../insurance.csv')

df.info()

for i in df.columns:
    if df[i].dtype == 'float64' or i == 'age':
        ax = sns.histplot(data = df, x=i)
        ax.grid(False)
        plt.ylabel('Count')
        plt.savefig('../output/eda/histplot_{}.jpg'.format(i), bbox_inches='tight')
        plt.show()
    else:
        ax = sns.barplot(x=df[i].value_counts().index, y=df[i].value_counts().values)
        ax.grid(False)
        plt.xlabel(i)
        plt.ylabel('Count')
        plt.savefig('../output/eda/barplot_{}.jpg'.format(i), bbox_inches='tight')
        plt.show()
        
categorical = ['sex', 'children', 'smoker', 'region']
numerical = ['age', 'bmi', 'charges']

corr = df[numerical].corr()
f, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corr, annot=True)
plt.savefig('../output/eda/correlation_heatmap.jpg', bbox_inches='tight')
plt.show()

charges_binned = []
for idx, val in enumerate(df['charges']):
    if val < 10000:
        charges_binned.append('1000 > charge')
    elif (val >=10000) and (val < 20000):
        charges_binned.append('10000 <= charge < 20000')
    elif (val >=20000) and (val < 30000):
        charges_binned.append('20000 <= charge < 30000')
    elif (val >=30000) and (val < 40000):
        charges_binned.append('30000 <= charge < 40000')
    else:
        charges_binned.append('charge > 40000')

df['charges_binned'] = charges_binned       
g = sns.pairplot(df.loc[:,df.columns != 'charges'].sort_values(['charges_binned']),
                  hue='charges_binned')
for ax in g.axes.flatten():
    ax.grid(False)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
g.legend.set_title(None)
plt.savefig('../output/eda/pairplot.jpg', bbox_inches='tight')
plt.show()