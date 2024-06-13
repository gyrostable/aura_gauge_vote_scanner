# processor.py

import pandas as pd


def process_votes(votes, choices, target_choices):
    choice_indices = {choice: index + 1 for index, choice in enumerate(choices)}
    target_indices = [choice_indices[choice] for choice in target_choices if choice in choice_indices]

    filtered_votes = []
    for vote in votes:
        matching_choices = [choice for choice in vote['choice'].keys() if int(choice) in target_indices]
        if matching_choices:
            num_choices = len(vote['choice'])
            vp_per_choice = vote['vp'] / num_choices
            filtered_votes.append({
                'address': vote['voter'],
                'choices': [choices[int(choice) - 1] for choice in matching_choices],
                'voting_power': vp_per_choice * len(matching_choices)
            })

    return pd.DataFrame(filtered_votes)
