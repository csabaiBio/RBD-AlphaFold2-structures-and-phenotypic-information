# From the created embeddings run experements to see how each varient cluster performs as a test set after training on wuhan.

from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler
# load data
# split data into X and y
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from matplotlib import cm
import pandas as pd
import os
from Bio import SeqIO


"""This file runs 4 experements to use some representations of Wuhan single varients to make predictions about other varients ACE2 binding.
We use Random forrest to classify a varient as a strong or weak binder. 
    
1. Summation model baseline: Sum together the single point mutants ACE2 magnitude for a new multiple varient. 
2. FASTA train and test: Fasta one hot encoded representation. 
3. AF2 adjacecny matrix train and test: AF2 strucutral data.
4. ESM embedding train and test: ESM2 structural contact map representations used.
 
"""

def train(dataset_wuhan):
    """train on all of wuhan for a given embedding"""
    dataset = dataset_wuhan[~np.isnan(dataset_wuhan).any(axis=1)]
    X = dataset[:,:-2]
    Y = dataset[:,-1].reshape(-1, 1)

    est = KBinsDiscretizer(n_bins=2, encode='ordinal', strategy='quantile')
    est.fit(Y) # return est so that we split other distributions the same as wuhan is split.
    Y = est.transform(Y)

    model = RandomForestClassifier().fit(X,Y) # fit model to training data
    
    return model, est


def test(test_set,model,est):
    """Test on 1000 samples of each phenotype class for a given varient"""
    test_dataset = np.load(test_set,allow_pickle=True)
    dataset= test_dataset[~np.isnan(test_dataset).any(axis=1)]
    X_test = dataset[:,:-2]
    Y = dataset[:,-1].reshape(-1, 1)
    y_test = est.transform(Y) # use the same transform for the train data.
        
    dataframe = np.hstack((X_test,y_test)) # recombine here before splitting again.
    df = pd.DataFrame(dataframe)
    table_ones = df.loc[df.iloc[:,-1] == 1]
    table_zeros = df.loc[df.iloc[:,-1] == 0]

    ones = table_ones.sample(n=1000) # split into two frames and sample# split into two frames and sample
    zeros = table_zeros.sample(n=1000)
    
    sampled = ones.append(zeros)
    sampled = sampled.to_numpy()

    X_test = sampled[:,:-1]
    y_test = sampled[:,-1].reshape(-1, 1)

    y_pred = model.predict(X_test) # make predictions for test data
    predictions = [round(value) for value in y_pred]
    
    accuracy = accuracy_score(y_test, predictions) # evaluate predictions
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    return accuracy


def get_muts_list(wuhan_baseline,variant):
    """Get the differences between two sequaneces in the form needed to retireve files"""
    mut_list = []
    start = 331
    for i in range(len(wuhan_baseline)):
        if wuhan_baseline[i] != variant[i]:
            mut_name = str(wuhan_baseline[i]) + str(i+start) + str(variant[i])
            mut_list.append(mut_name)
    return mut_list    


def model(wuhan,mut_list):
    """Intakes the list of point mutations from wuhan to a target variant.
    Outputs the sum of single binding affinity contributions."""
    kd_list = []
    for mut in mut_list:
        single_kd = wuhan.loc[wuhan["mutation"]== mut]["ACE2 binding"].values
        kd_list.append(single_kd)
    
    model_output = np.sum(np.array(kd_list))
    
    return model_output


def addition_model(var_scores,fasta_folder,est,wuhan):
    """Calc bin classification for linear model to compare against others."""
    wuhan_baseline =  "NITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKST"
    targets = []
    predictions = []
    for filename in os.listdir(fasta_folder):
        try:
            input_file = os.path.join(fasta_folder, filename)
            target_mut = input_file[-11:-6] # get mut from fasta file name.

            with open(input_file) as handle:
                for record in SeqIO.parse(handle, "fasta"):
                    variant = record.seq

            target_kd = var_scores.loc[var_scores["mutation"]==target_mut]["ACE2 binding"].values[0]
            mut_list = get_muts_list(wuhan_baseline,variant)
            prediction = model(wuhan,mut_list)
            if not np.isnan(prediction) and not np.isnan(target_kd):
                targets.append(target_kd)
                predictions.append(prediction)
        except:
            pass

    pred = np.array(predictions) # curently no list.. 
    true = np.array(targets)

    # print(true)
    # print(pred)
    # Threshold to make binary classifier from this baseline model.
    true = est.transform(true.reshape(-1,1))
    pred = est.transform(pred.reshape(-1,1))
    accuracy = accuracy_score(true, pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    return accuracy


def main():
    """Main function to run each experement"""
    # ------ Experemenal ACE2 values for baseline model ---------:
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

    lab_scores_list = [alpha,beta,delta,eta,omicron_ba1,omicron_ba2]
    base_var_list = ["alpha","beta","delta","eta","omicron_ba1","omicron_ba2"] #match to how data is downloaded.


    for i in range(5): # Repete each experement 5 times.

        # ---------- 1. FASTA train and test ------------
        dataset_wuhan = np.load("./embeddings/wuhan_one_hot_encoding.npy",allow_pickle=True)
        model,est = train(dataset_wuhan)
        FASTA = []
        print("Fasta")
        for var in base_var_list:
            print(var)
            test_set = "./embeddings/"+ var +"_one_hot_encoding.npy"
            acc = test(test_set,model,est)
            FASTA.append(acc)

        # --------- 2. AF2 adjacecny matrix train and test ---------
        dataset_wuhan = np.load("./embeddings/wuhan_adj_mat_encoding.npy",allow_pickle=True)
        model,est = train(dataset_wuhan)
        print("Adj")
        ADJ = []
        for var in base_var_list:
            test_set = "./embeddings/"+ var +"_adj_mat_encoding.npy"
            acc = test(test_set,model,est)
            ADJ.append(acc)

        # --------- 3. Summation model baseline ------------
        BASELINE = []
        print("Baseline")
        for var,lab_scores in zip(base_var_list,lab_scores_list):
            folder = "../Fasta_files_RBD/"+ var +"_RBD"
            acc = addition_model(lab_scores,folder,est,wuhan)
            BASELINE.append(acc) 

        # --------- 4. ESM embedding train and test ------------
        # dataset_wuhan = np.load("./embeddings/wuhan_ESM2_one_hot_encoding.npy",allow_pickle=True)
        # model,est = train(dataset_wuhan)
        # ESM = []
        # for var in base_var_list:
        #     test_set = "./ESM_embeddings/"+ var +"_one_hot_encoding.npy"
        #     acc = test(test_set,model,est)
        #     ESM.append(acc)

        # Save reasults to be plotted in RF_generalisation_plot

        np.save("./reasults/RF_experiment_reasults_"+str(i)+".npy",np.array([FASTA,ADJ,BASELINE]))
    
if __name__ == "__main__":
    main()