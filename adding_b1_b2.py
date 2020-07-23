import pandas as pd


def b1_b2(input_name, output_name):
    df = pd.read_csv(input_name)

    df['b1_cheating'] = df.apply(lambda row: 1 if (row['block_number'] == 1 and row['error'] == 1) else 0, axis=1)
    df['b2_cheating'] = df.apply(lambda row: 1 if (row['block_number'] == 2 and row['error'] == 1) else 0, axis=1)

    df['b1_sum'] = df.groupby(['user_id', 'block_number'])['b1_cheating'].transform('sum')
    df['b2_sum'] = df.groupby(['user_id', 'block_number'])['b2_cheating'].transform('sum')

    df.to_csv(output_name, index=False)


# tempt
# b1_b2('study1_tempt.csv', 'study1_tempt_b1_b2.csv')
# b1_b2('study1_tempt_amb.csv', 'study1_tempt_amb_b1_b2.csv')  # for ambiguous tempt
# b1_b2('study1_tempt_clear.csv', 'study1_tempt_clear_b1_b2.csv')  # for clear tempt

# not tempt
b1_b2('study1_not_tempt_clear.csv', 'study1_not_tempt_clear_b1_b2.csv')  # for clear not tempt
b1_b2('study1_not_tempt_amb.csv', 'study1_not_tempt_amb_b1_b2.csv')  # for ambiguous not tempt
b1_b2('study1_not_tempt.csv', 'study1_not_tempt_b1_b2.csv')  # b1 b2 for all not tempt
