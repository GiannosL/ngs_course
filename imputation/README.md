# Applied Bioinformatics / Next-Generation Sequencing / Genotype Imputation
Teaching material for Genotype Imputation lecture in NGS course.

## Basic **BASH** commands
1. `ls <path>` 
    * list the directory contents.
2. `less -S <file>` 
    * show the contents of the file, chop long lines.
3. `head -n <int> <file>` 
    * show the top *int* lines of a file.
4. `grep "pattern" <file>` 
    * show the lines in file that contain pattern.
5. `grep -v "pattern" <file>`
    * show lines in file that do NOT contain pattern.
6. `wc -l <file>` 
    * count lines in file.

## File formats
* **Variant Call Format (VCF)**
    * [Manual](https://samtools.github.io/hts-specs/VCFv4.2.pdf)

* **BED/BIM/FAM files (plink format)**
    * [Plink file formats](https://www.cog-genomics.org/plink/1.9/formats)

## Tools
1. Plink2
    * [Plink homepage](https://www.cog-genomics.org/plink/)
2. Impute5
    * [J. Marchini software](https://jmarchini.org/software/)
    * [Paper](SupplementaryMaterial/Impute5_paper.pdf)
    * [Manual](SupplementaryMaterial/Impute5_manual.pdf)

## Human genome references
1. **HapMap3**
    * [Welcome Sanger Institute](https://www.sanger.ac.uk/resources/downloads/human/hapmap3.html)
2. **1000 Genomes project**
    * [Paper](https://www.nature.com/articles/nmeth.1974)

## In-class exercises
1. [Data exploration](Exercises/exercise_1.md)
2. [Data preparation](Exercises/exercise_2.md)
3. [Imputation](Exercises/exercise_3.md)

### Post-class update
The tools used during class as well as the input can be found [here](Exercises/Tools-Data/).
