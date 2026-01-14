# Managing pipelines with Snakemake

## Snakemake pages
* [Homepage](https://snakemake.readthedocs.io/en/stable/)
* [Snakemake set-up](https://snakemake.readthedocs.io/en/stable/tutorial/setup.html#setup-on-windows)
* [Snakemake basics](https://snakemake.readthedocs.io/en/stable/tutorial/basics.html)

## Snakemake command line arguments
* Run from Snakefile's directory:

    ```snakemake --cores <number_of_threads>```

* Run Snakefile from different directory:

    ```snakemake --cores <number_of_threads> -s <snakefile_path>```

* Run Snakemake with configuration file:

    ```snakemake --cores <number_of_threads> --configfile <configfile_path>```

* Use environment modules:

    ```snakemake --cores <number_of_threads> --use-envmodules```

* Combine them into:

    ```snakemake --cores <number_of_threads> -s <snakefile_path> --configfile <configfile_path> --use-envmodules```

* Extra 1: Dry run (make sure that the connections work without actually running anything)

    ```snakemake --cores <number_of_threads> -n```

* Extra 2: Directed Acyclic Graph (DAG)

    ```snakemake --cores <number_of_threads> --dag```

## Exercises
1. Simple snakemake rule
    * [example_a](scripts/example_a/Snakefile)

2. Rule with variables
    * [example_b](scripts/example_b/Snakefile)

3. Rule with script
    * [example_c](scripts/example_c/Snakefile)

3. Multiple rules \[linear\]
    * [example_d](scripts/example_d/Snakefile)

4. Parameters for rules
    * [example_e](scripts/example_e/Snakefile)

5. Configuration file
    * [example_f](scripts/example_f/Snakefile)

6. Threading and Parallel computing \[parallel\]
    * Do not forget to ask for more processors to run in parallel.
    * [example_g](scripts/example_g/Snakefile)

7. Adding shell
    * Download plink for this exercise.
    * [example_h](scripts/example_h/Snakefile)

8. Biology example \[putting it all together\]
    * [example_i](scripts/example_i/)

9. Wildcards \[bonus example\]
    * [example_j](scripts/example_j/Snakefile)