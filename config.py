# config.py

# Define the proposal ID and target choices here

# Must be sorted descending (newest first)
CAMPAIGNS = [
    {
        "proposal_id": "0x7f604b07b26848a99f07c9a4ddfd1c0599176cb31615542ce87800010195b7fc",
        "date_announced": "2024-09-27",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x143d297ea7b43ee93fb157dfffad5a7af9d100cf68cbf7cd70569ee3e4ca5aac",
        "date_announced": "2024-09-13",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x5c9b2b52b7e866e42c8b1ab166e6af34feef697c4ab5f35f5c468b379024187e",
        "date_announced": "2024-08-31",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x4e5be40be9a9a66fd89751189183091299e55af7e849257cc59aca5d683c4dff",
        "date_announced": "2024-08-16",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe sDAI/GYD": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0xee768fb42cd5a0c47072adfc8b0245b3360578e2fce1b2b88d1e7c6765f8e869",
        "date_announced": "2024-01-08",
        "max_spin_per_vote": 8,
        "target_choices": {
            "Gyroe sDAI/GYD": {"max_spin": 800e3},
        },
    },
    {
        "proposal_id": "0x78aaf514dd57a595fffea9c4b42b3db87b6dc112027bf4447c196d4bbe72a2d0",
        "date_announced": "2024-07-19",
        "max_spin_per_vote": 8,
        "target_choices": {
            "z-Gyroe USDT/GYD": {"max_spin": 400e3},
            "Gyroe USDC/GYD": {"max_spin": 400e3},
            "Gyroe USDT/GYD": {"max_spin": 600e3},
            "Gyroe sDAI/GYD": {"max_spin": 600e3},
        },
    },
    {
        "proposal_id": "0xb2185096fc70b23df3253e46993c07e7e7ed1a7fb617ad574a15a0e6d5ded1ab",
        "date_announced": "2024-07-06",
        "max_spin_per_vote": 6,
        "target_choices": {
            "z-Gyroe USDC.e/GYD": {"max_spin": 840e3},
            "z-Gyroe USDT/GYD": {"max_spin": 840e3},
            "Gyroe USDC/GYD": {"max_spin": 840e3},
            "Gyroe USDT/GYD": {"max_spin": 840e3},
            "Gyroe sDAI/GYD": {"max_spin": 840e3},
        },
    },
    {
        "proposal_id": "0x917f4e9d801a047c8f63b9ff60bf68141acd7865b4ef62b4d0fa58ab7738d7dd",
        "date_announced": "2024-06-20",
        "max_spin_per_vote": 8,
        "target_choices": {
            "z-Gyroe USDC.e/GYD": {"max_spin": 1.2e6},
            "z-Gyroe USDT/GYD": {"max_spin": 1.2e6},
            "Gyroe USDC/GYD": {"max_spin": 600e3},
        },
    },
    {
        "proposal_id": "0xf5f08d407b3643c6bdd0155d70729be7be8128153d74f3941872874564d3c056",
        "date_announced": "2024-06-07",
        "max_spin_per_vote": 8,
        "target_choices": {
            "z-Gyroe USDC.e/GYD": {},
            "z-Gyroe USDT/GYD": {},
        },
    },
]

# Previous campaigns
# Campaign 5: 8 SPIN per vote capped
# PROPOSAL_ID = "0xee768fb42cd5a0c47072adfc8b0245b3360578e2fce1b2b88d1e7c6765f8e869"
# TARGET_CHOICES = ["Gyroe sDAI/GYD"]
# Campaign 4: 8 SPIN per vote capped
# PROPOSAL_ID = "0x78aaf514dd57a595fffea9c4b42b3db87b6dc112027bf4447c196d4bbe72a2d0"
# TARGET_CHOICES = ["z-Gyroe USDT/GYD", "Gyroe USDC/GYD", "Gyroe USDT/GYD", "Gyroe sDAI/GYD"]
# Campaign 1: 8 SPIN per vote capped
# PROPOSAL_ID = "0xf5f08d407b3643c6bdd0155d70729be7be8128153d74f3941872874564d3c056"
# TARGET_CHOICES = ["z-Gyroe USDC.e/GYD", "z-Gyroe USDT/GYD"]
# Campaign 2: 6 SPIN per vote capped
# PROPOSAL_ID = "0x917f4e9d801a047c8f63b9ff60bf68141acd7865b4ef62b4d0fa58ab7738d7dd"
# TARGET_CHOICES = ["z-Gyroe USDC.e/GYD", "z-Gyroe USDT/GYD", "Gyroe USDC/GYD"]
# Campaign 3: 6 SPIN per vote capped
# PROPOSAL_ID = "0xb2185096fc70b23df3253e46993c07e7e7ed1a7fb617ad574a15a0e6d5ded1ab"
# TARGET_CHOICES = ["z-Gyroe USDC.e/GYD", "z-Gyroe USDT/GYD", "Gyroe USDC/GYD", "Gyroe USDT/GYD", "Gyroe sDAI/USDC"]
