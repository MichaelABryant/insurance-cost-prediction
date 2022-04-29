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

