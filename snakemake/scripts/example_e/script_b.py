import pandas as pd

multiplier_value = snakemake.params.multiplier

df = pd.read_csv(snakemake.input.n, sep="\t")
df["column-A"] = df["column-A"]*multiplier_value
df["column-B"] = df["column-B"]*multiplier_value
df["column-C"] = df["column-C"]*multiplier_value

df.to_csv(snakemake.output.s, index=False, sep="\t")
