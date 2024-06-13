# analyzer.py

import os
import pandas as pd
from data_fetcher import fetch_votes, fetch_proposal
from processor import process_votes
from config import PROPOSAL_ID, TARGET_CHOICES


def analyze_proposal(proposal_id, target_choices):
    print("Fetching votes...")
    votes = fetch_votes(proposal_id)
    if not votes:
        print("Failed to fetch votes.")
        return pd.DataFrame()

    print("Fetching proposal details...")
    proposal = fetch_proposal(proposal_id)
    if not proposal:
        print("Failed to fetch proposal details.")
        return pd.DataFrame()

    choices = proposal['choices']
    print("Processing votes...")
    df = process_votes(votes, choices, target_choices)
    return df


if __name__ == "__main__":
    # Create the results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)

    df = analyze_proposal(PROPOSAL_ID, TARGET_CHOICES)
    if not df.empty:
        output_file = f"results/votes_analysis_{PROPOSAL_ID}.csv"
        df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    else:
        print("No matching votes found.")
