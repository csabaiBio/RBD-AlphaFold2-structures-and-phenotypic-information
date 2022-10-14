#here we loop over all single mutations of the Wuhan variant and use the pre-trained GeoPPI to get the predicted change in binding energy
import pandas as pd
import os
import subprocess
import time
from tqdm import tqdm
import csv 

def get_muts(variant):
    """This function returns the binding affiity of a given variant given its name"""
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
    # Expression and Binding scores per variant background -- for the heatmap plots
    scores_df = (
        pd.read_csv(variant_scores_path)
            .rename(columns = {"position":"site",
                            "delta_expr":"RBD expression", # rename for the selection menus 
                            "delta_bind":"ACE2 binding"    # rename for the selection menus 
                            })
            .replace({"target":variants_names})
    )
        # Expression and Binding scores per variant background -- for the heatmap plots
  
    muts = scores_df.loc[scores_df["target"] == variant]["mutation"]
    epression = scores_df.loc[scores_df["target"] == variant]["RBD expression"]

    return muts, epression


def foldX_one_var(variant,start):

    muts, epression = get_muts(variant) 

    row = ["mut_name", str(5), str(5)]
    with open('./stability_predictions_' + variant + '.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    for mut_name , value in tqdm(zip(muts,epression)):
        # some of these are not single sutants?... looks like tis a mutant of a mutant..
        # mutationinfo = mut_name[:1] + "E" + mut_name[1:] # add and E into the mutation name for GeoPPI to be compatable.
        try:
        # edited_mut_name = mut_name[1:-1] + '-' +mut_name[-1] #just for stipped part of the spike protein as the naming system is different. 
        # print(edited_mut_name)
        # ignore nanss and loop over both with zip..     
        # pdbfile = "spike_" + edited_mut_name + ".pdb"
        # pdb_dir = '/mnt/ncshare/ozkilim/charge_pca_deepmut/stripped_RBD_classical'
            
            pdb_dir = '../Wuhan_RBDs/structures/' + variant  #must be callable for all files... this is the sticking point.
            pdbfile = start + mut_name  +'.pdb' #uses start path infor as its different currently for each path.
            # save to some log file and then re-read it and delte it?
            comm = './foldx --command=Stability --pdb={} --pdb-dir={} --output-dir=./stability_output'.format(pdbfile,pdb_dir)
            os.system(comm) 
            output_file = "./stability_output/" + start + mut_name + "_0_ST.fxout"
            file = pd.read_csv(output_file,header=None,sep="\t") #upack saved reasults from the API and repack for our own data anlysis.
            output = file.values.tolist()[0][1] 

            row = [mut_name, str(value), str(output)]
            with open('./stability_predictions_' + variant + '.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)
            
        except:
            pass 
        
#  automate all reasults for all varients for figure production.   
def main():
    '''Repete FoldX predictionsof stability for each varient.'''
    varient_names = ["Wuhan-Hu-1_v2","Alpha","Beta","Delta","Eta",'Omicron_BA1',"Omicron_BA2"]
    start_path = ["RBD_331_531_","rot-Alpha_RBD_331_531_","rot-Beta_RBD_331_531_","rot-Delta_RBD_331_531_","Eta_RBD_331_531_","Omicron_RBD_331_531_","rot-OmicronBA2_RBD_331_531_"] 
    for variant,start in zip(varient_names,start_path):
        foldX_one_var(variant,start)   

if __name__ == "__main__":
    main()
    
