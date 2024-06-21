# processor.py

import pandas as pd
from decimal import Decimal, getcontext

# Set precision high enough to avoid rounding issues
getcontext().prec = 28


def process_votes(votes, choices, target_choices):
    choice_indices = {choice: index + 1 for index, choice in enumerate(choices)}
    target_indices = {index: choice for choice, index in choice_indices.items() if choice in target_choices}

    filtered_votes = []
    for vote in votes:
        choice_weights = vote['choice']
        total_votes = sum(choice_weights.values())
        total_vp = Decimal(vote['vp'])

        for choice_index, weight in choice_weights.items():
            if int(choice_index) in target_indices:
                relative_weight = Decimal(weight) / Decimal(total_votes)
                voting_power = relative_weight * total_vp
                filtered_votes.append({
                    'address': vote['voter'],
                    'choice': target_indices[int(choice_index)],
                    'total_voting_power': float(total_vp),
                    'vote_weight': float(relative_weight),
                    'total_votes': float(voting_power)
                })

    return pd.DataFrame(filtered_votes)
