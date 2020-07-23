import pandas as pd

df = pd.read_csv('study1_bonus11.csv')
df.to_csv(r'study1_bonus.txt', header=None, index=None, sep=',', mode='a')
