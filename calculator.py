from config import CAMPAIGNS

import argparse
import pandas as pd
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Analyze pulled results")
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

    pid = campaign["proposal_id"]
    filename = f"results/votes_analysis_{pid}.csv"
    df = pd.read_csv(filename)

    per_pool = pd.DataFrame(
        {"total_votes_pool": df.groupby("choice").total_votes.sum()}
    )
    per_pool["max_spin_pool"] = [
        campaign["target_choices"][c].get("max_spin", np.inf) for c in per_pool.index
    ]
    per_pool["max_spin_per_vote_pool"] = [
        campaign["target_choices"][c].get(
            "max_spin_per_vote", campaign["max_spin_per_vote"]
        )
        for c in per_pool.index
    ]
    per_pool["spin_per_vote_if_threshold_pool"] = np.minimum(
        per_pool["max_spin_per_vote_pool"],
        per_pool["max_spin_pool"] / per_pool["total_votes_pool"],
    )

    threshold = campaign.get("threshold_power")
    if threshold is None:
        # We use reasonable defaults so you don't *have* to define the threshold power when it's obvious.
        if any(per_pool.total_votes_pool.between(30e3, 40e3)):
            raise ValueError(
                "Pool with intermediate number of votes. Explicitly set `threshold_power` in config for this campaign. Use `fetch_sum_all_pools.py` to compute."
            )
        threshold = 40e3

    per_pool["is_above_threshold_pool"] = per_pool["total_votes_pool"] >= threshold
    per_pool["spin_per_vote_pool"] = np.where(
        per_pool["is_above_threshold_pool"],
        per_pool["spin_per_vote_if_threshold_pool"],
        0.0,
    )

    # Info:
    missed_threshold_pools = per_pool[~per_pool["is_above_threshold_pool"]]
    if not missed_threshold_pools.empty:
        print("NB: The following pools did not reach the threshold:")
        print(missed_threshold_pools[["total_votes_pool"]])

    # print(per_pool)

    df = df.merge(per_pool, on="choice")

    df["spin"] = df["total_votes"] * df["spin_per_vote_pool"]
    # print(df)

    per_voter = df.groupby("address").spin.sum()

    print("SPIN per voter:")
    per_voter_fmt = per_voter.apply(lambda x: f"{x:.2f}")
    print(per_voter_fmt)

    print()
    print("Python format:")
    for addr, spin in per_voter.items():
        spin_str = f"{spin:,.2f}".replace(",", "_")
        print(f'("{addr}", {spin_str}),')

    output_filename = f"results/emissions_{pid}.csv"
    pd.DataFrame({"address": per_voter.index, "spin": per_voter.values}).to_csv(
        output_filename, index=False
    )


if __name__ == "__main__":
    main()
