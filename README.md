# AURA Snapshot Vote Analyzer

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

Define the `proposal_id` and `target_choices` in the `config.py` file.
* `proposal_id` is the unique ID of the proposal to analyze
* `target_choices` contains the list of choices to consider for analysis

## Usage

To analyze a specific proposal and filter out votes based on specific choices, run:
```sh
python analyzer.py
```

Results will then be stored in the `results` folder containing the `proposal_id` as the run identifier.