# Take generated mutant trimers and select only 331-531 region in one of the trimers.
import os 
from biopandas.pdb import PandasPdb

directory = '/mnt/ncshare/ozkilim/charge_pca_deepmut/Mutant_Structures_classical'
for file in os.listdir(directory):
    folder = directory + '/' + file
    ppdb = PandasPdb()
    ppdb.read_pdb(folder)
    start_res=331
    end_res=531
    chain_id = 'A'

    data = ppdb.df['ATOM']

    # select parts and re-save..
    ppdb.df['ATOM'] = ppdb.df['ATOM'][(ppdb.df['ATOM']['residue_number'].values >= start_res) & (ppdb.df['ATOM']['residue_number'].values <= end_res) & (ppdb.df['ATOM']['chain_id'].values == 'A')] 
    
    ppdb.to_pdb(path='/mnt/ncshare/ozkilim/charge_pca_deepmut/stripped_RBD_classical' + '/' + file, 
            records=None, 
            gz=False, 
            append_newline=True)

