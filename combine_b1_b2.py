import pandas as pd

b1_df = pd.read_csv('study1_not_tempt_amb_b1.csv')
b2_df = pd.read_csv('study1_not_tempt_amb_b2.csv')

result = pd.concat([b1_df, b2_df], axis=1, sort=False)
result.columns = ['ID', 'block1', 'b1', 'ID2', 'block2', 'b2']
result = result.drop(['block1', 'ID2', 'block2'], axis=1)
# result = result.drop(result.columns[2], axis=1)

result.to_csv('study1_not_tempt_amb_b1_b2_sum.csv', index=False)
