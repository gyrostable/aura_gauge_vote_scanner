# processor.py

import pandas as pd
from decimal import Decimal, getcontext

# Set precision high enough to avoid rounding issues
getcontext().prec = 28


def process_votes(votes, choices, target_choices):
    choice_indices = {choice: index + 1 for index, choice in enumerate(choices)}
    target_indices = [choice_indices[choice] for choice in target_choices if choice in choice_indices]

    filtered_votes = []
    for vote in votes:
        choice_weights = vote['choice']
        total_votes = sum(choice_weights.values())
        matching_choices = [choice for choice in choice_weights.keys() if int(choice) in target_indices]
        if matching_choices:
            total_vp = Decimal(vote['vp'])
            total_vp_for_matching_choices = sum(
                (Decimal(choice_weights[choice]) / Decimal(total_votes)) * total_vp
                for choice in matching_choices
            )
            filtered_votes.append({
                'address': vote['voter'],
                'choices': [choices[int(choice) - 1] for choice in matching_choices],
                'total_voting_power': float(total_vp),
                'vote_weight': float(sum(choice_weights[choice] for choice in matching_choices) / total_votes),
                'voting_power': float(total_vp_for_matching_choices)
            })

    return pd.DataFrame(filtered_votes)
