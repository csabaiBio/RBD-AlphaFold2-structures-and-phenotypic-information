# RBD-AlphaFold2-structures-and-phenotypic-information

This repository is provded alongside AlfaFold2 data for 

The scripts to reproduce figure 1 from the paper:

## To train the Resnet50: 

Prepare data:
`CNN_training/generate_adj_files.ipynb`
Create 5 fold splits:
`CNN_training/5_fold_split.ipynb`
Train and test Resnet50 on created splits for each variant:
`python3 CNN_training/resnet_adjmat.py`

## To run the XGBoost experements:

Prepare FASTA and Adjacency matrix data:
`python3 multivariant_embedding_creation.py`
Train GXBoost classifier for FASTA and Adjacency matrix data 
`python3 XGBoost_methods_output.py`
To Clean the spike protein data from: 
`python3 trimer_to_RBD.py`

## To create figures for the paper:

### Classification figure:
`present_predictions.ipynb`

### PCA plot of the FASTA files:
`fasta_PCA/PCA_run.ipynb`

### Linear Model

#### ACE2 prediction
`dependance_of_muts_ACE2.ipynb`

#### RBD expressiobn prediction
`dependance_of_muts_Expression.ipynb`