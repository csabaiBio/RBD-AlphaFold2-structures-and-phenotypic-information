#See how changing between amino acids effects RMSD as an average over all positions
import os
from Bio import SeqIO
import sys
sys.path.append('/mnt/ncshare/ozkilim/covid/covid_landscape/SARS2_RBD_Ab_escape_maps')
from bindingcalculator import BindingCalculator
from biopandas.pdb import PandasPdb
from scipy.spatial import distance_matrix
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import matplotlib.patches as mpatches
from scipy.signal import find_peaks
from scipy.spatial import distance_matrix

# ---- This script created all mutation-dostortion maps for all variants ---- 

def pos_matrix_creator(PDB_filename):
    """"This function takes in a PDB and ... it returns a symetrix MxM matrix that is rotation and shift independant"""""
    ppdb = PandasPdb()
    data = ppdb.read_pdb(PDB_filename)
    atom_data = ppdb.df['ATOM']    
    mut_removed = atom_data
    position_matrix = mut_removed[["residue_number","x_coord" , "y_coord" , "z_coord"]]
    # aggresgate and take mean of xyz values for each residue as an approximation.
    aggregation_functions = {'x_coord': 'mean', 'y_coord': 'mean', 'z_coord': 'mean'}
    position_matrix = position_matrix.groupby(position_matrix['residue_number']).aggregate(aggregation_functions)  

    return position_matrix 

base_var_list = ["wuhan","alpha","beta","delta","eta",'omicron_ba1','omicron_ba2'] #match to how data is downloaded.
pdb_file_list = ["6M0J_E","Alpha_RBD","Beta_RBD","Delta_RBD","Eta_RBD","Omicron_RBD","OmicronBA2_RBD"]

for dir ,pdb_file in zip(base_var_list,pdb_file_list):
    interaction_mat = []
    directory = "../structures/" + dir
    print(dir)
    for idx, filename in enumerate(os.listdir(directory)):
        try:
            file_path = os.path.join(directory, filename)
            mut_name = file_path[-9:-4]
            start = mut_name[0]
            target = mut_name[-1]
            pos = int(mut_name[1:-1])
            # create distance matrix.
            d = pos_matrix_creator(file_path)
            pdb_file_WT = "../wt_pdbs/rot-" + pdb_file + ".pdb"
            wuhan_mat = pos_matrix_creator(pdb_file_WT)
            dist = (wuhan_mat.to_numpy()-d.to_numpy())
            dist = np.linalg.norm(dist,axis=1)
            interaction_mat.append([pos,dist])
        except:
            pass
        
    np.save("./mutation_distortion_maps/" + dir + ".npy",np.array(interaction_mat))