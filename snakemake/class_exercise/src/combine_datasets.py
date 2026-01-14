import argparse
import pandas as pd


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--icd_file', type=str, required=True, help='Path to ICD codes TSV file')
parser.add_argument('--atc_file', type=str, required=True, help='Path to ATC codes TSV file')
parser.add_argument('--out_file', type=str, required=True, help='Path to output combined TSV file')
args = parser.parse_args()

# Read both datasets
df_icd = pd.read_csv(args.icd_file, sep='\t')
df_atc = pd.read_csv(args.atc_file, sep='\t')

# Merge on patient_id, episode_start, and episode_end
df_combined = pd.merge(
    df_icd,
    df_atc,
    on=['patient_id', 'episode_start', 'episode_end'],
    how='outer'
)

# Ensure datetime dtypes
df_combined['episode_start'] = pd.to_datetime(df_combined['episode_start'])
df_combined['episode_end'] = pd.to_datetime(df_combined['episode_end'])

# Sort by patient_id and episode_start
df_combined = df_combined.sort_values(by=['patient_id', 'episode_start']).reset_index(drop=True)

# Write to output file
df_combined.to_csv(args.out_file, sep='\t', index=False)
