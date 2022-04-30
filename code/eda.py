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
    if val < 2500:
        charges_binned.append('charges < \$2,500')
    elif (val >=2500) and (val < 7500):
        charges_binned.append('\$2,500 <= charges < \$7,500')
    elif (val >=7500) and (val < 10000):
        charges_binned.append('\$7,500 <= charges < \$10,000')
    elif (val >=10000) and (val < 20000):
        charges_binned.append('\$10,000 <= charges < \$20,000')
    else:
        charges_binned.append('charges > \$20,000')

df['charges_binned'] = charges_binned       
g = sns.pairplot(df.loc[:,df.columns != 'charges'],
                  hue='charges_binned',
                  hue_order = ['charges < \$2,500',
                               '\$2,500 <= charges < \$7,500',
                               '\$7,500 <= charges < \$10,000',
                               '\$10,000 <= charges < \$20,000',
                               'charges > \$20,000'
                               ])
for ax in g.axes.flatten():
    ax.grid(False)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
g.legend.set_title(None)
plt.savefig('../output/eda/pairplot.jpg', bbox_inches='tight')
plt.show()