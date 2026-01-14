import argparse
import pandas as pd
import numpy as np


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', type=str, required=True, help='Path to combined dataset TSV file')
parser.add_argument('--num_batches', type=int, required=True, help='Number of batches to create')
parser.add_argument('--output_dir', type=str, required=True, help='Directory to save output batch files')
args = parser.parse_args()

import os
os.makedirs(args.output_dir, exist_ok=True)

# Read the combined dataset
df = pd.read_csv(args.input_file, sep='\t')

# Ensure datetime dtypes
df['episode_start'] = pd.to_datetime(df['episode_start'])
df['episode_end'] = pd.to_datetime(df['episode_end'])

# Get unique patients
unique_patients = df['patient_id'].unique()

# Split patients into batches using numpy's array_split
patient_batches = np.array_split(unique_patients, args.num_batches)

# Create a batch file for each group of patients
for batch_idx, patient_batch in enumerate(patient_batches, start=1):
    # Filter dataframe to include only patients in this batch
    df_batch = df[df['patient_id'].isin(patient_batch)].copy()
    
    # Sort by patient_id and episode_start for consistency
    df_batch = df_batch.sort_values(by=['patient_id', 'episode_start']).reset_index(drop=True)
    
    # Save to file
    output_file = os.path.join(args.output_dir, f'batch_{batch_idx:03d}.tsv')
    df_batch.to_csv(output_file, sep='\t', index=False)
