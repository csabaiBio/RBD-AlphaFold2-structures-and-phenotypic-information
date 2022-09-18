# This master script perfroms all experements requred to show structures generated my alphafold contain phenotypic information. Output is compressed reasults materix ready to be plotted for paper figure.    

import numpy as np
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import csv

def XGBoost_cls(embedding_path):
    '''This function take sin a pre processed one hot encoded matrix representation '''
    dataset = np.load(embedding_path ,allow_pickle=True)
    dataset= dataset[~np.isnan(dataset).any(axis=1)]
    X = dataset[:,:-2]
    Y = dataset[:,-2:-1].reshape(-1, 1) # this predictcs ACE2?
    scaler = StandardScaler().fit(X)
    X = scaler.transform(X)
    est = KBinsDiscretizer(n_bins=2, encode='ordinal', strategy='quantile') # is it ok to split at this point evenly for bin cls?
    est.fit(Y)
    Y = est.transform(Y)
    model = XGBClassifier()
    kfold = KFold(n_splits=5, shuffle=True)
    results = cross_val_score(model, X, Y, cv=kfold)
    
    return results.mean()*100, results.std()*100


def XG_one_varient(varient_name):
    '''Run experements for each variant and save to csv files to be presented in figure'''
    # --- FASTA
    embedding_path = "/mnt/ncshare/ozkilim/charge_pca_deepmut/embeddings/" +  varient_name + "_one_hot_encoding.npy"   
    reasults, STD = XGBoost_cls(embedding_path)
    
    row = ["FASTA",reasults, STD]
    with open("/mnt/ncshare/ozkilim/charge_pca_deepmut/experement_reasults/" + varient_name + ".csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        
    # --- ADJ XGBoost
    embedding_path = "/mnt/ncshare/ozkilim/charge_pca_deepmut/embeddings/" +  varient_name + "_adj_mat_encoding.npy"   
    reasults, STD = XGBoost_cls(embedding_path)
    row = ["ADJ",reasults, STD]
    with open("/mnt/ncshare/ozkilim/charge_pca_deepmut/experement_reasults/" + varient_name + ".csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def main():
    """For each varient train and test CNN of one of 5 foleds already generated. Save all reasults in seperate files to be collated and displayed as reasults. Currently this is to predict ACE2 binding affinity"""
    varients = ["wuhan","alpha","beta","delta","eta","omicronBA1"]
    for vairent_name in varients:
        XG_one_varient(vairent_name)
        
if __name__ == "__main__":
    main()
