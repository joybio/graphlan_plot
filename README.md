[TOC]

# GraPhlAn plot script

## Birefing introduction

GraPhlAn is a software tool for producing high-quality circular representations of taxonomic and phylogenetic trees. This script is designed to automate the process of generating circular phylogenetic tree visualizations using Graphlan. With this script, you can easily create high-quality graphical representations of phylogenetic trees without the need for manual intervention.


##  Installation

#Prerequisites
Before using this script, ensure that you have the following dependencies installed:

R (version 4.3.1 or higher)
Graphlan
  ```bash
  conda create -n graphlan -c bioconda graphlan r-base r-optparse
  ```

Activate the environment
  ```bash
  conda activate graphlan
  ```

## Quick start

Here are two examples of how to use the script:

Example 1: Cloadgram+Heatmap

Basic usage:
  ```bash
  Rscript graphlan_plot.r --input demo1/taxonomy2.spf --design demo1/metadata.txt --type heatmap --output demo1/Heat_results
  ```
Advanced usage with additional options:
   ```bash
  Rscript graphlan_plot.r --input demo2/taxonomy2.spf --design demo2/metadata.txt --number 150 --colname Group --group all --type heatmap --output demo2/Heat_results
  ```
  or specify the desired group
  ```bash
  Rscript graphlan_plot.r --input demo1/taxonomy2.spf --design demo1/metadata.txt --number 150 --colname Group --group N,D,SHL,SHH --type heatmap --output demo1/Heat_results
  ```
  
 
Example 2: Cloadgram+barplot

Basic usage:
  ```bash
  Rscript graphlan_plot.r --input demo1/taxonomy2.spf --design demo1/metadata.txt --type bar --output demo1/Bar_results
  ```
Advanced usage with additional options:
  ```bash
  Rscript graphlan_plot.r --input demo1/taxonomy2.spf --design demo1/metadata.txt --number 150 --group all --type heatmap --output demo1/Bar_results
  ```
  or specify the desired group

  ```bash
  Rscript graphlan_plot.r --input demo2/taxonomy2.spf --design demo2/metadata.txt --number 150 --colname Group --group Z,DSS,SHJ --type bar --output demo2/Bar_results
  ```
  

#Output
The script will generate a circular phylogenetic tree visualization and save it to the specified output file.
# Options
  ```bash
  Rscript graphlan_plot.r -h
  ```
  ```bash
  Usage: graphlan_plot.r [options]
  Options:
        -i INPUT, --input=INPUT
                Metadata of metaphlan4 [default taxonom2.spf]
        -n NUMBER, --number=NUMBER
                Top number threshold [default 150]
        -d DESIGN, --design=DESIGN
                Design file or metadata [default metadata.tsv]
        -c COLNAME, --colname=COLNAME
		        Select column name to use, e.g. Group [default Group]
        -g GROUP, --group=GROUP
                Specify the desired group, comma seperate. e.g. A,B,C,D [default all]
        -t TYPE, --type=TYPE
		        specify plot type, e.g. heatmap, bar, [default heatmap]
        -o OUTPUT, --output=OUTPUT
                Output pdf directory. [default ./]
        -h, --help
                Show this help message and exit
  ```

#Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. We welcome any improvements or bug fixes.

#License
This project is licensed under the MIT License - see the LICENSE file for details.

#Contact
If you have any questions or encounter issues with the script, please contact joybio at [1806389316@pku.edu.cn].
