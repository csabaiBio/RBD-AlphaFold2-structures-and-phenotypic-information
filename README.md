# RBD-AlphaFold2-structures-and-phenotypic-information

### This repository is provded alongside AlphaFold2 data found at: href{https://figshare.com/projects/SARS-CoV-2_RBD_single_mutant_AlphaFold2_structures/150089} The scripts are presented to reproduce all reasults in the paper titled: "SARS-CoV-2 RBD deep mutational AlphaFold2 structures carry phenotypic information"

# Data structure:

FASTA

- wuahn
- alpha 
- beta
- delta
- eta
- omicronBA1
- omicronBA2

structures

- wuahn
- alpha 
- beta
- delta
- eta
- omicronBA1
- omicronBA2



# Download and unzip the data running:
`./data_prepare.sh`

# To run CNN experements: 
### 1. Prepare data:
`CNN_training/generate_adj_files.ipynb`
### 2. Create 5 fold splits:
`CNN_training/5_fold_split.ipynb`
### 3. Train and test Resnet50 on created splits for each variant:
`python3 CNN_training/resnet_adjmat.py`

## To Clean the spike protein data from: 
`python3 trimer_to_RBD.py`

# To create figures for the paper:

# Scripts to create "Pseudo-complex"

# Scripts to create PQR files

## FoldX RBD protein expression prediction experement.
### Run experement with foldX software installed.
`data_release_paper/foldX_stability/foldx_expression_prediction.py`
### Create figure
`expression_foldx_analysis.ipynb`