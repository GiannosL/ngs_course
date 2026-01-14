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

# Sample ICD-10 diagnosis codes
icd10_code_pool = [
    "I10",        # Essential (primary) hypertension
    "E11",      # Type 2 diabetes mellitus without complications
    "J18",      # Pneumonia, unspecified organism
    "C34",     # Malignant neoplasm of unspecified part of lung
    "K21",      # Gastro-esophageal reflux disease without esophagitis
    "M54",      # Low back pain
    "F32",      # Major depressive disorder, single episode, unspecified
    "N39",      # Urinary tract infection, site not specified
    "A41",      # Sepsis, unspecified organism
    "R07"       # Chest pain, unspecified
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

        # Randomly assign 1–3 ICD-10 codes per episode
        diagnosis_codes = random.sample(
            icd10_code_pool,
            random.randint(1, 3)
        )

        records.append({
            "patient_id": f"P{patient_id:04d}",
            "episode_start": start_date,
            "episode_end": end_date,
            "icd10_codes": ','.join(diagnosis_codes)
        })

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(records)

# Ensure datetime dtype
df["episode_start"] = pd.to_datetime(df["episode_start"])
df["episode_end"] = pd.to_datetime(df["episode_end"])

df.to_csv(args.out_file, sep='\t', index=False)
