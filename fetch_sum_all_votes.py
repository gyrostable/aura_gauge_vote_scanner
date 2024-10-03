from data_fetcher import fetch_votes, fetch_proposal
import argparse


def main():
    parser = argparse.ArgumentParser(description="Compute total votes for proposal")
    parser.add_argument(
        "proposal_id",
        help="Proposal ID to analyze",
    )
    args = parser.parse_args()

    votes: list = fetch_votes(args.proposal_id)  # type: ignore

    total_power = 0.0

    # Copied & adjusted from processor.py
    for vote in votes:
        choice_weights = vote["choice"]
        total_votes = sum(choice_weights.values())
        total_vp = float(vote["vp"])
        total_power += total_vp

    print(f"Total power:     {total_power:,.0f}")
    print(f"Threshold power: {total_power * 0.1e-2:,.0f}")
    print()
    print(f"Total power:     {total_power}")
    print(f"Threshold power: {total_power * 0.1e-2}")


if __name__ == "__main__":
    main()
