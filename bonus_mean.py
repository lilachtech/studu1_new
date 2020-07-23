import pandas as pd

df = pd.read_csv('study1_data.csv')  # need to change file number

user_data = df.groupby(['user_id', 'conditions', 'bonus', 'final_payment']).sum()

print(user_data)  # need to change
user_data.reset_index().to_csv(r'study1_bonus1.csv', header=True, index=False)  # need to change val and file name