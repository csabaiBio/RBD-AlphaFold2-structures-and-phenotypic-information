# SARS-CoV-2 RBD deep mutational AlphaFold2 structures carry phenotypic information.
## Scientific data.

## This repository is provided alongside AlphaFold2 data found at: 
### https://figshare.com/projects/SARS-CoV-2_RBD_single_mutant_AlphaFold2_structures/150089 

#### The scripts are presented to reproduce all results in the paper titled: "SARS-CoV-2 RBD deep mutational AlphaFold2 structures carry phenotypic information"

![Superposition of single mutants](./reasults_figs/fig2b_ribbons.png)

# Getting started. 
## Download and unzip the data running (for linux/mac).
`./data_prepare.sh`
### This data can also be downloaded manually.

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

# Generated WT main varinats:
### These are used for local distortion and alignment analysis.
[`../wt_pdbs`](https://github.com/csabaiBio/RBD-AlphaFold2-structures-and-phenotypic-information/tree/main/wt_pdbs)

# Reproducing our data-set validation and useful notebooks:

## Visualizing structural distortion on mutation (mutation-distortion maps).
### We investigate the mean distortion in distance each amino acid has for each each structure created. We observe that every mutation at a given position corresponds to a structural distortion at that position as well as some others in the structure.
`../data_usage_scripts/mutation_distortion_maps.ipynb`

### To create all of the maps for all of the mutant clusters:
`../data_usage_scripts/mutation_distortion.py`
### To view all of these maps.
`../data_usage_scripts/all_mut_dist_maps.ipynb`

## Simple statistics notebook.
### Exploring simple amino acid variation statistics.
`../data_usage_scripts/aa_changes_vs_RMSD.ipynb`
### Exploring the importance of the interface with respect to ACE2 binding values.
`../interface_exploration/interface_importance.ipynb`

## Protein Disorder analysis notebook.
### Here we investigate how pLDDT (b-factor) output of the AF2 files correlate with state-of-the-art disorder estimations.
`../disorder_analysis/iupred_notebook-Analyses_mod.ipynb`

## Wuhan generalization experiment:
`cd wuhan_generalization_experiments`
### To create all embeddings and run random forest classifier experiment.
`./wuhan_generalization.sh`
### Then to visualize results with the notebook:
`./RF_generalization_plot.ipynb`

## Umap results figure:
### Visualize embeddings (representations) of the generated dataset.
`./projections/UMAP_all_vars_structs.ipynb`

## Scripts to create PQR files
### Create PQR files for further downstream tasks.
`./APBS_and_PQR/PQR-APBS.ipynb`

## FoldX RBD protein expression prediction experiment.
### Run FoldX stability function for all structures with foldX software installed.
`./foldX_stability/foldx_expression_prediction.py`

## Validation that structures are correctly aligned.
### We see a direct correlation between RMSD values in the 3D space and rotation invariant adjacency matrix space.
`../rotation_analysis/MSE_vs_adjacency_dist.ipynb`

## Antibody escape plots notebook.
### Using the Bloom et al antibody escape calculator, we observe structural distortion correlates with antibody escape.
`../antibody_escape/antibody_escape_vs_structuraldistortion.ipynb`