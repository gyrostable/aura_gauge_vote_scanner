# config.py

# Define the proposal ID and target choices here

# Must be sorted descending (newest first)
CAMPAIGNS = [
    {
        "proposal_id": "0x967cf0759a25bd15f4033b2d9e35fc70412190d2f83f8b6f7e40ac08de76be19",
        "date_announced": "2025-02-17",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
        # Disable threshold power b/c it was announced late.
        "threshold_power": 0,
    },
    {
        "proposal_id": "0xe70964d063328607938e80017578513b0d0b38b23c938a02f4e5c07d0f0edb1a",
        "date_announced": "2025-02-02",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
        # Disable threshold power b/c it was announced late.
        "threshold_power": 0,
    },
    {
        "proposal_id": "0xd3eb06d107554f4feb7fb8f7730c3a50c49fbca160454b8964a98164edfda038",
        "date_announced": "2025-01-17",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0xb71b94ed1a2482360378ebfa795d66c9a70a2e31498088551ce5710716e41f5f",
        "date_announced": "2025-01-05",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x2e7f83ca9125fbde09b4d9d3aee2309a6e1facaac65be224e3ff48dce01b5486",
        "date_announced": "2024-12-20",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0xca2db946abe18169bd4fd1d296721f16df66a4052e9ebee434d7085bc9968c4e",
        "date_announced": "2024-12-06",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x2cc46de8f63d957646a1e3132a95056e9274f9277f016b02eb588888bc942a9a",
        "date_announced": "2024-11-23",
        "max_spin_per_vote": 6,
        "target_choices": {
            # For some reason the label for this option has changed to include the gauge address.
            "Gyroe USDT/GYD (0xfc)": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x9dcb635e6a6f9469ea739b9c10008cfcfc60b39c04c0640c4bba223c7000d3fc",
        "date_announced": "2024-11-08",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe sDAI/GYD": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x92210213b7685eca71b046724cfee9afd0375b938412ad30e479610caa0a2d4c",
        "date_announced": "2024-10-25",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe sDAI/GYD": {"max_spin": 360e3},
        },
    },
    {
        "proposal_id": "0x3220c1c5c2a02676e9df058cdd576a474ace75f183616d53bd0f5106aeb20cd5",
        "date_announced": "2024-10-11",
        "max_spin_per_vote": 6,
        "target_choices": {
            "Gyroe USDT/GYD": {"max_spin": 360e3},
        },
        # HACK: Intentionally ignoring the threshold here. The vote didn't make the threshold but we
        # decided to emit 50% of the SPIN because it was very close. (ticket-0739 with farmerfroom)
        # "threshold_power": 36493.12096334147,
        "threshold_power": 0.0,
    },
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
        "date_announced": "2024-08-01",
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
