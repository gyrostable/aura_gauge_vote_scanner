# AURA Snapshot Vote Analyzer

Original version by defilytica, adjustments by sschuldenzucker.

This small helper tool allows you to fetch gauge votes from AURAs snapshot space and analyze which addresses voted for a subset of pre-defined choices.

A potential use-case is to find voters for a subset for gauges to airdrop rewards to (contratry to participating in voting incentive markets)
## Setup

1. Clone the repository.
2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Add campaigns to the `CAMPAIGNS` constant in `config.py`. See there for which options you can set. Campaigns should be in reverse chronological order.

* `proposal_id` is the unique ID of the proposal to analyze
* `max_spin_per_vote` = SPIN per vote unless the pool's `max_spin` is reached (see below).
* `target_choices` contains the list of choices to consider for analysis
* In `target_choices`, you *can* optionally define:
    * `max_spin` = total SPIN available for this pool.
    * `max_spin_per_vote` = override the `max_spin_per_vote` for the campaign.
* Optionally, you can set `threshold_power` = power for a pool to be considered. Normally not needed, we have a heuristic.

## Usage

To pull data for a specific proposal and filter out votes based on specific choices, run:
```sh
python analyzer.py [proposal_id]
```

Results will then be stored in the `results` folder containing the `proposal_id` as the run identifier. If no `proposal_id` is given, the most recent one is used.

To compute how much SPIN everyone should get, run:

```sh
python calculator.py [proposal_id]
```

This outputs the resulting SPIN on the terminal and also writes a CSV in `results/`.
