import pandas as pd

df = pd.read_csv(snakemake.input.n, sep="\t")
df["column-A"] = df["column-A"]**2
df["column-B"] = df["column-B"]**2
df["column-C"] = df["column-C"]**2

df.to_csv(snakemake.output.s, index=False, sep="\t")
