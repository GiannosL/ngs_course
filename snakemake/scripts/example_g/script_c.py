from time import sleep

with open(snakemake.output.f, "w+") as f:
    for i in range(10):
        f.write(f"{i}\n")
        sleep(3)
