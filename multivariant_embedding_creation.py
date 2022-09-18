## This is a generic script to create sets that can be used as train and test for all vairntes weith PDB files. 

# Input: Dirs of PDB's and FASTA files.
from prody import *
from biopandas.pdb import PandasPdb
import numpy as np
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
import os
import pandas as pd
from fasta_one_hot_encoder import FastaOneHotEncoder
  
variant_scores_path = "/mnt/ncshare/ozkilim/charge_pca_deepmut/SARS-CoV-2-RBD_DMS_Omicron/results/final_variant_scores/final_variant_scores.csv"

variants_names = {
    "Wuhan-Hu-1_v2": "Wuhan-Hu-1_v2",
    "N501Y": "Alpha", 
    "Beta": "Beta",
    "Delta": "Delta",
    "E484K": "Eta",
    "Omicron_BA1":"Omicron_BA1"
}
# Expression and Binding scores per variant background -- for the heatmap plots
scores_df = (
    pd.read_csv(variant_scores_path)
        .rename(columns = {"position":"site",
                           "delta_expr":"RBD expression", # rename for the selection menus 
                           "delta_bind":"ACE2 binding"    # rename for the selection menus 
                          })
        .replace({"target":variants_names})
)
wuhan = scores_df.loc[scores_df["target"] == "Wuhan-Hu-1_v2"]    
alpha = scores_df.loc[scores_df["target"] == "Alpha"]    
beta = scores_df.loc[scores_df["target"] == "Beta"]    
delta = scores_df.loc[scores_df["target"] == "Delta"]    
eta = scores_df.loc[scores_df["target"] == "Eta"]    
omicron = scores_df.loc[scores_df["target"] == "Omicron_BA1"]    

# Output: Embedding for Adj matric and One-hot fasta files for each varient seperately so further experements with combinations can be done down the line.


encoder = FastaOneHotEncoder(
    nucleotides = "galmfwkqespvicyhrndt",
    lower = True,
    sparse = False,
    handle_unknown="ignore"
)


def distance_matrix_creator(PDB_filename):
    """"This function takes in a PDB and ... it returns a symetrix MxM matrix that is rotation and shift independant"""""
    ppdb = PandasPdb()
    data = ppdb.read_pdb(PDB_filename)
    atom_data = ppdb.df['ATOM']    
    mut_removed = atom_data
    # print(len(mut_removed["residue_number"])-len(atom_data["residue_number"])) #different for alpha...? much smaller number of atoms?...
    # print(mut_removed["x_coord",])
    position_matrix = mut_removed[["residue_number","x_coord" , "y_coord" , "z_coord"]]
    # aggresgate and take mean of xyz values for each residue as an approximation.
    aggregation_functions = {'x_coord': 'mean', 'y_coord': 'mean', 'z_coord': 'mean'}
    position_matrix = position_matrix.groupby(position_matrix['residue_number']).aggregate(aggregation_functions)  
    # cartersian productcartersian product of distance. 
    dist_mat = distance_matrix(position_matrix,position_matrix,p=2) #p=2 for euclidian disntace

    return dist_mat 


def one_hot_encode(directory,varient_measurements,varient_name):
    """Save one hot encoding embedding of each mutants of a varient of interest."""
    encoder = FastaOneHotEncoder(
        nucleotides = "galmfwkqespvicyhrndt",
        lower = True,
        sparse = False,
        handle_unknown="ignore"
    )
    out_data = []
    for file in os.listdir(directory):
        path  = directory + "/" + file
        try:
            mut_name = file[-11:-6]
            # loop over all and keep the end string as a label for each vector for puting no theplot.. keep  the  main mutantname  for clustering..
            encoding = encoder.transform_to_df(path, verbose=True)
            encoding = np.array(encoding).flatten() #flattened for PCA.        
            # get phenotype expresion value. 
            expression = varient_measurements.loc[varient_measurements["mutation"]== mut_name]["RBD expression"].values
            binding = varient_measurements.loc[varient_measurements["mutation"]== mut_name]["ACE2 binding"].values  
            encoding = np.append(encoding,expression[0])
            encoding = np.append(encoding,binding[0])
            out_data.append(encoding)
        except:
            pass
        
    out_data = np.array(out_data)
    output_file = "./embeddings/" + varient_name+"_one_hot_encoding.npy" 
    np.save(output_file,out_data)



def adj_encoding(directory,varient_measurements,varient_name):
    """Save adjacency encodings for each mutant of a varient"""
    out_data = []
    # that directory
    for idx, filename in enumerate(os.listdir(directory)):
        try:
            file_path = os.path.join(directory, filename)
            mut_name = file_path[-9:-4]
            # create distance matrix.
            d = distance_matrix_creator(file_path)
            feature_vec = d.flatten()
            # get phenotype expresion value. 
            expression = varient_measurements.loc[varient_measurements["mutation"]== mut_name]["RBD expression"].values
            binding = varient_measurements.loc[varient_measurements["mutation"]== mut_name]["ACE2 binding"].values  
            
            feature_vec = np.append(feature_vec,expression[0])
            feature_vec = np.append(feature_vec,binding[0])

            out_data.append(feature_vec)
        except:
            pass

    out_data = np.array(out_data)
    output_file = "./embeddings/" + varient_name+"_adj_mat_encoding.npy" 

    np.save(output_file,out_data)
    
# Build in antibody escape data for further downstream experements...
    
# TODO:    
    # Extend this with Both omicron varients.when BA2 data is out.

experemental_list = [wuhan,alpha,beta,delta,eta,omicron]
pdb_list = ["/mnt/ncshare/ozkilim/charge_pca_deepmut/Wuhan_RBDs/structures/Wuhan_RBDs","/mnt/ncshare/ozkilim/charge_pca_deepmut/Wuhan_RBDs/structures/Alpha_aligned","/mnt/ncshare/ozkilim/charge_pca_deepmut/Wuhan_RBDs/structures/Beta_aligned","/mnt/ncshare/ozkilim/charge_pca_deepmut/Wuhan_RBDs/structures/Delta_aligned","/mnt/ncshare/ozkilim/charge_pca_deepmut/Wuhan_RBDs/structures/Eta_Wuhan_RBD_DMS_PDB","/mnt/ncshare/ozkilim/charge_pca_deepmut/Wuhan_RBDs/structures/Omicron_Wuhan_RBD_DMS_PDB"]
FASTA_list = ["/mnt/ncshare/ozkilim/charge_pca_deepmut/Fasta_files_RBD/Wuhan_RBD","/mnt/ncshare/ozkilim/charge_pca_deepmut/Fasta_files_RBD/Alpha_RBD","/mnt/ncshare/ozkilim/charge_pca_deepmut/Fasta_files_RBD/Beta_RBD","/mnt/ncshare/ozkilim/charge_pca_deepmut/Fasta_files_RBD/Delta_RBD","/mnt/ncshare/ozkilim/charge_pca_deepmut/Fasta_files_RBD/Eta_RBD","/mnt/ncshare/ozkilim/charge_pca_deepmut/Fasta_files_RBD/Omicron_RBD"]
varient_names = ["wuhan","alpha","beta","delta","eta",'OmicronBA1']

for varient_measurements,PDB_files,FASTA_files,varient_name in zip(experemental_list,pdb_list,FASTA_list,varient_names):
    print(varient_name)
    print("One hot encoding")
    one_hot_encode(FASTA_files,varient_measurements,varient_name)
    print("Adj encoding")
    adj_encoding(PDB_files,varient_measurements,varient_name)