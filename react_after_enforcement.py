import pandas as pd

# df = pd.read_csv('study1_tempt.csv')
#
# low_df = df[df.conditions == 'low_enforcement']
#
# low_df.to_csv("low_only.csv", index=False)
low_df = pd.read_csv('low_only.csv')


before_list = []
first_list = []
second_list = []
third_list = []
trails_number_list = []
user_id_list = []
block_number_list = []

for index, row in low_df.iterrows():
    if row['inspection'] == 1:
        before = row['choice_correct']
        trail_number = row['trial_number']
        user_id = row['user_id']
        block_number = row['block_number']

        if block_number == 2 and trail_number >= 97:
            first = 'nan'
            second = 'nan'
            third = 'nan'
        else:
            first = low_df.iloc[index + 1]['choice_correct']
            second = low_df.iloc[index + 2]['choice_correct']
            third = low_df.iloc[index + 3]['choice_correct']

        before_list.append(before)
        first_list.append(first)
        second_list.append(second)
        third_list.append(third)
        block_number_list.append(block_number)
        trails_number_list.append(trail_number)
        user_id_list.append(user_id)

        print(trail_number, before, first, second, third)

    else:
        print('none')

print(trails_number_list)
print(before_list)
print(first_list)
print(second_list)
print(third_list)


low_df = pd.DataFrame(list(zip(user_id_list, block_number_list, trails_number_list, before_list, first_list, second_list, third_list)),
                      columns=['User ID', 'Block Num', 'Trail Number', 'Before', 'First', 'Second', 'Third'])

print(low_df)
low_df.to_csv("low_df_react_id_nan_7dropped.csv", index=False)
print('hello')
