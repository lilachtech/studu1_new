import pandas as pd

# tempt_df = tempt_df.drop('error', axis=1)
# tempt_df['condition'].replace(['high_enforcement', 'low_enforcement', 'no_enforcement2'], [1, 2, 3], inplace=True)
# cheating_rates = tempt_df.groupby('user_id')['error'].sum()
# cheating_rates = df.groupby(['user_id', 'block_number', 'error']).sum()
# cheating_rate = tempt_df.choice_correct.sum()


def clean(input, output):
    tempt_df = pd.read_csv(input)
    tempt_df['fine_size'].replace('-', 0, inplace=True)
    tempt_df.to_csv(output, index=False)


def tempt(input, output):
    tempt_df = pd.read_csv(input)
    tempt_df = tempt_df.query("profitable_side != true_side")
    tempt_df['error'] = tempt_df.apply(lambda row: 1 if (row['choice_correct'] == 0) else 0, axis=1)
    tempt_df.to_csv(output, index=False)


def not_tempt(input, output):
    tempt_df = pd.read_csv(input)
    tempt_df = tempt_df.query("profitable_side == true_side")
    tempt_df['error'] = tempt_df.apply(lambda row: 1 if (row['choice_correct'] == 0) else 0, axis=1)
    tempt_df.to_csv(output, index=False)


#clean('study1_data.csv', 'study1_clean.csv')
#tempt('study1_clean.csv', 'study1_tempt.csv')
#not_tempt('study1_clean.csv', 'study1_not_tempt.csv')