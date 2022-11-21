# Script to reproduce entire experemental pipeline. Runtime= 
# 1. Create all embeddings from data downloaded.
python3 embeddings_creation.py 
# 2. Run all experements on the embeddings and lab data from bloom lab.
python3 RF_generalization_experiments.py 
# 3. Present data as figure
