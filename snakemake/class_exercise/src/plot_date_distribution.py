import argparse
import pandas as pd
import matplotlib.pyplot as plt


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', type=str, required=True, help='Path to input TSV file (ICD or ATC)')
parser.add_argument('--output_plot', type=str, required=True, help='Path to save the output plot')
args = parser.parse_args()

# Read the dataset
df = pd.read_csv(args.input_file, sep='\t')

# Ensure datetime dtypes
df['episode_start'] = pd.to_datetime(df['episode_start'])
df['episode_end'] = pd.to_datetime(df['episode_end'])

# Create figure with two subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Plot episode start date distribution
axes[0].hist(df['episode_start'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Number of Episodes')
axes[0].set_title('Distribution of Episode Start Dates')
axes[0].grid(axis='y', alpha=0.3)

# Plot episode end date distribution
axes[1].hist(df['episode_end'], bins=50, color='coral', edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Number of Episodes')
axes[1].set_title('Distribution of Episode End Dates')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(args.output_plot, dpi=300, bbox_inches='tight')
print(f"Plot saved to {args.output_plot}")

# Print summary statistics
print(f"\nSummary Statistics:")
print(f"Total episodes: {len(df)}")
print(f"Start date range: {df['episode_start'].min()} to {df['episode_start'].max()}")
print(f"End date range: {df['episode_end'].min()} to {df['episode_end'].max()}")
