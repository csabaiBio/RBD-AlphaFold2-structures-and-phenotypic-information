# RBD-AlphaFold2-structures-and-phenotypic-information

## This repository is provded alongside AlphaFold2 data found at: 
### https://figshare.com/projects/SARS-CoV-2_RBD_single_mutant_AlphaFold2_structures/150089 

#### The scripts are presented to reproduce all reasults in the paper titled: "SARS-CoV-2 RBD deep mutational AlphaFold2 structures carry phenotypic information"

# Getting started. 
## Download and unzip the data running (for linux/mac).
### This data can also be downloaded manually.

`./data_prepare.sh`

# Data structure created:

## FASTA
- wuahn
- alpha 
- beta
- delta
- eta
- omicron_ba1
- omicron_ba2

## Structures
- wuahn
- alpha 
- beta
- delta
- eta
- omicron_ba1
- omicron_ba2

# Simple statistics and antibody escape plots notebook.
`../antibody_escape/antibody_escape_vs_structuraldistortion.ipynb`

# Wuhan generalization experemnt:
`cd wuhan_generalization_experements`
### then to create all embeddings and run random forrest classifier experement.
`./wuhan_generalization.sh`
### Then to visualise reasults:
`../wuhan_generalization_experements/RF_generalisation_plot.ipynb`

# Umap reasults figure:
`./projections/UMAP_all_vars_structs.ipynb`

# Scripts to create PQR files
`./data_usage_scripts/PQR-APBS.ipynb`


## FoldX RBD protein expression prediction experement.
### Run experement with foldX software installed.
`./foldX_stability/foldx_expression_prediction.py`
