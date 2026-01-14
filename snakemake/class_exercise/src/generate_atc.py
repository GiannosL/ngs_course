import random
import argparse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--out_file', type=str)
args = parser.parse_args()

# -----------------------------
# Configuration
# -----------------------------
num_patients = 1_000
max_episodes_per_patient = 20

# Sample ATC medication codes
atc_code_pool = [
    "C09AA",    # ACE inhibitors (Hypertension)
    "A10BA",    # Metformin (Type 2 diabetes)
    "J01FA",    # Macrolide antibiotics (Pneumonia)
    "L01DC",    # Targeted cancer therapy (Neoplasm)
    "A02BA",    # H2-receptor antagonists (GERD)
    "M01AB",    # Ibuprofen (Back pain)
    "N06AA",    # Tricyclic antidepressants (Depression)
    "J01CA",    # Beta-lactam antibiotics (UTI)
    "S01HA",    # Antiinfective agents (Sepsis)
    "N02BA"     # Salicylates (Chest pain)
]

random.seed(71)
np.random.seed(71)

# -----------------------------
# Generate synthetic data
# -----------------------------
records = []

for patient_id in range(1, num_patients + 1):
    num_episodes = random.randint(1, max_episodes_per_patient)

    for _ in range(num_episodes):
        start_date = datetime(2023, 1, 1) + timedelta(
            days=random.randint(0, 365)
        )
        length_of_stay = random.randint(1, 14)
        end_date = start_date + timedelta(days=length_of_stay)

        # Randomly assign 1–3 ATC codes per episode
        medication_codes = random.sample(
            atc_code_pool,
            random.randint(1, 3)
        )

        records.append({
            "patient_id": f"P{patient_id:04d}",
            "episode_start": start_date,
            "episode_end": end_date,
            "atc_codes": ','.join(medication_codes)
        })

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(records)

# Ensure datetime dtype
df["episode_start"] = pd.to_datetime(df["episode_start"])
df["episode_end"] = pd.to_datetime(df["episode_end"])

df.to_csv(args.out_file, sep='\t', index=False)
