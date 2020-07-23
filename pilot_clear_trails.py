import pandas as pd


def ambiguous_trails(file_name_input, file_name_output):
    ambiguous_trails_df = pd.read_csv(file_name_input)  # file of all tempt
    ambiguous_trails_df = ambiguous_trails_df[ambiguous_trails_df.trial_type != 'Clear_profit_side']  # not tempt
    # ambiguous_trails_df = ambiguous_trails_df[ambiguous_trails_df.trial_type != 'Clear_not_profit_side']  # tempt
    ambiguous_trails_df.to_csv(file_name_output, index=False)


# ambiguous_trails('study1_tempt.csv', "study1_tempt_amb.csv")
ambiguous_trails('study1_not_tempt.csv', "study1_not_tempt_amb.csv")


def clear_trails(file_name_input, file_name_output):
    clear_df = pd.read_csv(file_name_input)
    clear_df = clear_df[clear_df.trial_type == 'Clear_profit_side']  # not tempt
    # clear_df = clear_df[clear_df.trial_type == 'Clear_not_profit_side']  # tempt
    clear_df.to_csv(file_name_output, index=False)


# clear_trails('study1_tempt.csv', "study1_tempt_clear.csv")
clear_trails('study1_not_tempt.csv', "study1_not_tempt_clear.csv")
