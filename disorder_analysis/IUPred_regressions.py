import os, glob
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns
from Bio import SeqIO


var_list = ["Alpha","Beta","Delta","Eta","Omicron","OmicronBA2"]
r2_scores_short = []
r2_scores_long = []
for var in var_list: 
    # Short
    df_bfactor = pd.read_csv('./iupred_plddt/'+ var +'_bfactor.csv')
    df_all = pd.read_csv('./iupred_plddt/'+ var +'_iupred2a_short.csv')

    if var == "OmicronBA2":
        df_bfactor['pos'] = df_bfactor['pos'] - 330
        # df_all['pos']= df_all['pos'] + 19

    df_bfactor['pos'] = df_bfactor['pos'].astype(int)
    df_all['pos'] = df_all['pos'].astype(int)
    df_all['Iupred2'] = df_all['Iupred2'].astype(float)
    df_merge = pd.merge(df_all, df_bfactor)
    # Chop off ends before analysis.
    df_merge = df_merge[(df_merge['pos'] < 181) & (df_merge['pos'] > 19)]
    # linear regression. Bug for omicronba2?
    X = df_merge.iloc[:, 2].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = df_merge.iloc[:, 4].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(1/X, 100-Y)  # perform linear regression
    r2 = linear_regressor.score(1/X, 100-Y)
    r2_scores_short.append(round(r2,2))

    # Long
    df_bfactor = pd.read_csv('./iupred_plddt/'+ var +'_bfactor.csv')
    df_all = pd.read_csv('./iupred_plddt/'+ var +'_iupred2a_long.csv')

    if var == "OmicronBA2":
        df_bfactor['pos'] = df_bfactor['pos'] - 330
        # df_all['pos'] = df_all['pos'] + 19

    df_bfactor['pos'] = df_bfactor['pos'].astype(int)
    df_all['pos'] = df_all['pos'].astype(int)
    df_all['Iupred2'] = df_all['Iupred2'].astype(float)
    df_merge = pd.merge(df_all, df_bfactor)
    # Chop off ends before analysis.
    df_merge = df_merge[(df_merge['pos'] < 181) & (df_merge['pos'] > 19)]
    # linear regression. Bug for omicronba2?
    X = df_merge.iloc[:, 2].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = df_merge.iloc[:, 4].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(1/X, 100-Y)  # perform linear regression
    r2 = linear_regressor.score(1/X, 100-Y)

    r2_scores_long.append(round(r2,2))

table_out = pd.DataFrame([np.array(r2_scores_short),np.array(r2_scores_long)])

table_out.to_csv("disorder_regression_reasults.csv")

# Repete for long and short... 