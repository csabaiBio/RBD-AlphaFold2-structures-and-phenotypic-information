from prody import *
from biopandas.pdb import PandasPdb
import numpy as np
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
import os
import pandas as pd
from fasta_one_hot_encoder import FastaOneHotEncoder
from prody import *
from biopandas.pdb import PandasPdb
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
import torch
import esm
from Bio import SeqIO

""" This is a generic script to create sets that can be used as train and test for all vairntes weith PDB files. 
# Output: Embedding for Adj matric and One-hot fasta files for each varient seperately so further experements with combinations can be done down the line. """

# Both ACE2 and RBD expression are saved into the matrix for use downstream. (repete full script for RBD prediction.)

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


def ESM_generate(model,batch_converter,directory,varient_measurements,varient_name):
    """Save one hot encoding embedding of each mutants of a varient of interest."""
    
    out_data = []
    i=0

    for file in os.listdir(directory):
        path  = directory + "/" + file
        try:
            
            mut_name = file[-11:-6]
            # loop over all and keep the end string as a label for each vector for puting no theplot.. keep  the  main mutantname  for clustering..
            fasta_sequences = SeqIO.parse(open(path),'fasta')
            for fasta in fasta_sequences:
                name, sequence = fasta.id, fasta.seq
                    
            data = [
                ("protein1", str(fasta.seq)),
            ]

            batch_labels, batch_strs, batch_tokens = batch_converter(data) # can do in batches but here just do by one... 

            with torch.no_grad():
                results = model(batch_tokens, repr_layers=[33], return_contacts=True)

            encoding = np.array(results["contacts"]).flatten() #flattened for PCA. 
            # get phenotype expresion value. 
            expression = varient_measurements.loc[varient_measurements["mutation"]== mut_name]["RBD expression"].values
            binding = varient_measurements.loc[varient_measurements["mutation"]== mut_name]["ACE2 binding"].values  
            encoding = np.append(encoding,expression[0])
            encoding = np.append(encoding,binding[0])
            out_data.append(encoding)
            i  = i+1
            print(i)
        except:
            pass
        
    out_data = np.array(out_data)
    output_file = "./embeddings/" + varient_name+"_ESM2_adj_mat.npy" 
    np.save(output_file,out_data)


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



def encode_onehot_padded(aa_seqs):
        '''
        one-hot encoding of a list of amino acid sequences with padding
        parameters:
            - aa_seqs : list with CDR3 sequences
        returns:
            - enc_aa_seq : list of np.ndarrays containing padded, encoded amino acid sequences
        '''
        ### Create an Amino Acid Dictionary
        aa_list = sorted(['A', 'C', 'D', 'E','F','G', 'H','I', 'K', 'L','M','N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])
        
        aa_dict = {char : l for char, l in zip(aa_list, np.eye(len(aa_list), k=0))}
        
        #####pad the longer sequences with '-' sign
        #1) identify the max length
        max_seq_len = max([len(x) for x in aa_seqs])
        #2) pad the shorter sequences with '-'
        aa_seqs = [seq + (max_seq_len - len(seq))*'-'
                        for i, seq in enumerate(aa_seqs)]
        # encode sequences:
        sequences=[]
        for seq in aa_seqs:
            e_seq=np.zeros((len(seq),len(aa_list)))
            count=0
            for aa in seq:
                if aa in aa_list:
                    e_seq[count]=aa_dict[aa]
                    count+=1
                else:
                    print ("Unknown amino acid in peptides: "+ aa +", encoding aborted!\n")
            sequences.append(e_seq)
        enc_aa_seq = np.asarray(sequences)
        
        return np.squeeze(enc_aa_seq)


def one_hot_encode(directory,varient_measurements,varient_name):
    """Save one hot encoding embedding of each mutants of a varient of interest."""
    out_data = []
    for file in os.listdir(directory):
        path  = directory + "/" + file
        try:
            mut_name = file[-11:-6]
            # loop over all and keep the end string as a label for each vector for puting no theplot.. keep  the  main mutantname  for clustering..            
            fasta_sequences = SeqIO.read(path,'fasta')
            aa_seq = str(fasta_sequences.seq)
            encoding = encode_onehot_padded(aa_seq)
            encoding = np.array(encoding).flatten()        
            # get phenotype ACE2 and expresion value. 
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
    

def main():

    model, alphabet = esm.pretrained.esm2_t33_650M_UR50D() # Load ESM-2 model
    batch_converter = alphabet.get_batch_converter()
    model.eval()  # disables dropout for deterministic results

    variant_scores_path = "../SARS-CoV-2-RBD_DMS_Omicron/results/final_variant_scores/final_variant_scores.csv"

    variants_names = {
        "Wuhan-Hu-1_v2": "Wuhan-Hu-1_v2",
        "N501Y": "Alpha", 
        "Beta": "Beta",
        "Delta": "Delta",
        "E484K": "Eta",
        "Omicron_BA1":"Omicron_BA1",
        "Omicron_BA2":"Omicron_BA2"
    }

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
    omicron_ba1 = scores_df.loc[scores_df["target"] == "Omicron_BA1"]    
    omicron_ba2 = scores_df.loc[scores_df["target"] == "Omicron_BA2"]    

    experemental_list = [wuhan,alpha,beta,delta,eta,omicron_ba1,omicron_ba2]
    
    # Make these relative and matching then way we unzip from the data prep script.
    
    wuhan_pdb_path = "../Wuhan_RBDs/structures/Wuhan-Hu-1_v2"
    alpha_pdb_path = "../Wuhan_RBDs/structures/Alpha"
    beta_pdb_path = "../Wuhan_RBDs/structures/Beta"
    delta_pdb_path = "../Wuhan_RBDs/structures/Delta"
    eta_pdb_path = "../Wuhan_RBDs/structures/Eta"
    omicron_ba1_pdb_path = "../Wuhan_RBDs/structures/Omicron_BA1"   
    omicron_ba2_pdb_path = "../Wuhan_RBDs/structures/OmicronBA2_RBD_DMS_PDB/OmicronBA2_aligned"
   

    wuhan_FASTA_path = "../Fasta_files_RBD/wuhan_RBD"
    alpha_FASTA_path = "../Fasta_files_RBD/alpha_RBD"
    beta_FASTA_path = "../Fasta_files_RBD/beta_RBD"
    delta_FASTA_path = "../Fasta_files_RBD/delta_RBD"
    eta_FASTA_path = "../Fasta_files_RBD/eta_RBD"
    omicron_ba1_FASTA_path = "../Fasta_files_RBD/omicron_ba2_RBD"
    omicron_ba2_FASTA_path = "../Fasta_files_RBD/omicron_ba2_RBD" 

    
    pdb_list = [wuhan_pdb_path,alpha_pdb_path,beta_pdb_path,delta_pdb_path,eta_pdb_path,omicron_ba1_pdb_path,omicron_ba2_pdb_path]
    FASTA_list = [wuhan_FASTA_path,alpha_FASTA_path,beta_FASTA_path,delta_FASTA_path,eta_FASTA_path,omicron_ba1_FASTA_path,omicron_ba2_FASTA_path]
    
    varient_names = ["wuhan","alpha","beta","delta","eta",'omicron_ba1','omicron_ba2']

    for varient_measurements,PDB_files,FASTA_files,varient_name in zip(experemental_list,pdb_list,FASTA_list,varient_names):
        
        if varient_name == 'omicron_ba2':
            print(varient_name)
            print("One hot encoding")
            one_hot_encode(FASTA_files,varient_measurements,varient_name)
            print("Adj encoding")
            adj_encoding(PDB_files,varient_measurements,varient_name)
            # print("ESM encoding")
            # ESM_generate(model,batch_converter,FASTA_files,varient_measurements,varient_name) #only run this later if required.
            
        
if __name__ == "__main__":
    main()