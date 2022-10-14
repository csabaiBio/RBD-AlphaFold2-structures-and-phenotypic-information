# # This script will download all figshare data for this project. 
# # It will dump the data in the correct format for validating all 
# # of our analyses as well as a convinient format for further use.

# # 1. Download provided data from the paper
# # wget all data.
# # wuhan.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304680/versions/1 -P ./structures/wuhan
unzip structures/wuhan/1 -d structures/wuhan 
rm structures/wuhan/1
rm structures/wuhan/*.pdb
unzip structures/wuhan/Wuhan.zip -d ./structures/wuhan 
rm structures/wuhan/Wuhan.zip

# alpha.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304554/versions/1 -P ./structures/alpha
unzip structures/alpha/1 -d structures/alpha 
rm structures/alpha/1
rm structures/alpha/*.pdb
unzip structures/alpha/Alpha.zip -d ./structures/alpha 
rm structures/alpha/Alpha.zip

# beta.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304620/versions/1 -P ./structures/beta
unzip structures/beta/1 -d structures/beta 
rm structures/beta/1
rm structures/beta/*.pdb
unzip structures/beta/Beta.zip -d ./structures/beta 
rm structures/beta/Beta.zip

# # delta.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304665/versions/1 -P ./structures/delta
unzip structures/delta/1 -d structures/delta 
rm structures/delta/1
rm structures/delta/*.pdb
unzip structures/delta/Delta.zip -d ./structures/delta 
rm structures/delta/Delta.zip

# # eta.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304641/versions/1 -P ./structures/eta
unzip structures/eta/1 -d structures/eta 
rm structures/eta/1
rm structures/eta/*.pdb
unzip structures/eta/Eta.zip -d ./structures/eta 
rm structures/eta/Eta.zip

# # omicronba1.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304671/versions/1 -P ./structures/omicron_ba1
unzip structures/omicron_ba1/1 -d structures/omicron_ba1 
rm structures/omicron_ba1/1
rm structures/omicron_ba1/*.pdb
unzip structures/omicron_ba1/OmicronBA1.zip -d ./structures/omicron_ba1 
rm structures/omicron_ba1/OmicronBA1.zip

# # omicronba2.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21304674/versions/1 -P ./structures/omicron_ba2
unzip structures/omicron_ba2/1 -d structures/omicron_ba2
rm structures/omicron_ba2/1
rm structures/omicron_ba2/*.pdb
unzip structures/omicron_ba2/OmicronBA2.zip -d ./structures/omicron_ba2
rm structures/omicron_ba2/OmicronBA2.zip

# # FASTA sequences.
wget --no-check-certificate https://figshare.com/ndownloader/articles/21311130/versions/1 -P ./FASTA
unzip FASTA/1 -d FASTA
# unzip each subfolder...to iots own subfolder...
unzip FASTA/original.zip -d FASTA/wuhan
rm FASTA/original_seq.zip
unzip FASTA/Alpha_seq.zip -d FASTA/alpha
rm FASTA/Alpha_seq.zip
unzip FASTA/Beta_seq.zip -d FASTA/beta
rm FASTA/Beta_seq.zip
unzip FASTA/Delta_seq.zip -d FASTA/delta
rm FASTA/Delta_seq.zip
unzip FASTA/Eta_seq.zip -d FASTA/eta
rm FASTA/Eta_seq.zip
unzip FASTA/Omicron_seq.zip -d FASTA/omicron_ba1
rm FASTA/Omicron_seq.zip
unzip FASTA/OmicronBA2_seq.zip -d FASTA/omicron_ba2
rm FASTA/OmicronBA2_seq.zip
rm FASTA/1
