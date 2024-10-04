# analyzer.py

import os
import pandas as pd
from data_fetcher import fetch_votes, fetch_proposal
from processor import process_votes
from config import CAMPAIGNS
import argparse


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

    choices = proposal["choices"]

    # Safety net
    for c in target_choices:
        if c not in choices:
            raise ValueError(f"Config error: choice {c} not found.")

    print("Processing votes...")
    df = process_votes(votes, choices, target_choices)
    return df


if __name__ == "__main__":
    # Create the results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)

    parser = argparse.ArgumentParser(description="Pull proposal data")
    parser.add_argument(
        "proposal_id",
        nargs="?",
        help="Proposal ID to analyze; default = most recent one.",
    )
    args = parser.parse_args()

    if args.proposal_id:
        (campaign,) = [c for c in CAMPAIGNS if c["proposal_id"] == args.proposal_id]
    else:
        campaign = CAMPAIGNS[0]

    PROPOSAL_ID = campaign["proposal_id"]
    TARGET_CHOICES = list(campaign["target_choices"].keys())

    df = analyze_proposal(PROPOSAL_ID, TARGET_CHOICES)
    if not df.empty:
        output_file = f"results/votes_analysis_{PROPOSAL_ID}.csv"
        df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    else:
        print("No matching votes found.")
