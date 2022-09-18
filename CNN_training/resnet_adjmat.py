import pandas as pd 
import numpy as np
from cv2 import cv2
from sklearn.model_selection import train_test_split
import torch
from torch import nn
from torch.autograd import Variable
from torch.nn import Linear, ReLU, MSELoss, Sequential, Conv2d, MaxPool2d, Module, Softmax, BatchNorm2d, Dropout, CrossEntropyLoss
from torch.optim import Adam, SGD
import torch.optim as optim
import torchvision
from torchvision import datasets, models, transforms
import copy
import math
import os
import pandas as pd
from torchvision.io import read_image
import pickle
import os
import pandas as pd
from torchvision.io import read_image
from torch.utils.data import Dataset, DataLoader
import argparse
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter
import csv 


def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False   
            
            
class Baseline_model():
    def __init__(self):
        """Resnet models"""
        
    def resnet50_model():
        model_ft = models.resnet50(pretrained=True) 
        model_ft.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

        set_parameter_requires_grad(model_ft, False)
        num_ftrs = model_ft.fc.in_features
        model_ft.fc = nn.Linear(num_ftrs, 2) 
        return model_ft
    
    def resnet18_model():
        model_ft = models.resnet18(pretrained=True) 
        model_ft.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

        set_parameter_requires_grad(model_ft, False)
        num_ftrs = model_ft.fc.in_features
        model_ft.fc = nn.Linear(num_ftrs, 2) 
        return model_ft

    def resnet101_model():
        model_ft = models.resnet101(pretrained=True) 
        model_ft.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

        set_parameter_requires_grad(model_ft, False)
        num_ftrs = model_ft.fc.in_features
        model_ft.fc = nn.Linear(num_ftrs, 2) 
        return model_ft


# split and normalise to 2 files for training and testing...

class ADJDataset(Dataset):
    def __init__(self, annotations_file, transform=None, target_transform=None):

        self.adj_labels = pd.read_csv(annotations_file)
 
    def __len__(self):
        return len(self.adj_labels)

    def __getitem__(self, idx):
        # Need to call get item unill we have correct number ofsamples and ignore failure no find cases..
        try:
            adj_path = str(self.adj_labels.iloc[idx, 1])
            image = np.load(adj_path) #load adj image # failing here to load image?....
            image = np.expand_dims(image, 0)   
            # Add extra dimentions to image with reshaping.
            ACE2 = self.adj_labels.iloc[idx, 2]  
            expr = self.adj_labels.iloc[idx, 3]  
        except Exception as e:
            return None
        return image, ACE2,expr


# Create a string to save the model and reasults that describes the experemental conditions. 

def collate_fn(batch):
    batch = list(filter(lambda x: x is not None, batch))
    return torch.utils.data.dataloader.default_collate(batch)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #device config
# run on two GPU's'

def trainLoop(train_path,test_path):
    num_epocs = 50
    ''' trainLoop is the function that can be iuteratively run. 
    It instantiates and trains a new model each time it is called. 
    Outputs : train and validation accruacy as well as the trained model'''
    # Load data..
    # Train dataloader
    training_data = ADJDataset(train_path)
    train_dataloader = DataLoader(training_data, collate_fn=collate_fn,batch_size=32, shuffle=True) 
    # Test dataloader
    testing_data = ADJDataset(test_path)
    test_dataloader = DataLoader(testing_data, collate_fn=collate_fn,batch_size=32, shuffle=True) 

    train_accuracy = []
    test_accuracy = []
    
    # Baseline experement
    model_ft = Baseline_model.resnet50_model()
    model_ft = nn.DataParallel(model_ft,device_ids=[0, 1])
    model_ft = model_ft.to(device)
    # defining the optimizer
    optimizer = optim.SGD(model_ft.parameters(), lr=0.0003) #with regulerization. 
    
    writer = SummaryWriter()

    criterion = CrossEntropyLoss()
    for epoch in tqdm(range(num_epocs)):
        for step, (x, y, _) in enumerate(train_dataloader):   # gives batch data
            # ------- Training --------
            # Mount tensors on the GPU
            x = x.float().to(device)
            y = y.float().to(device)
            # zero grad
            optimizer.zero_grad()
            # forward pass
            outputs = model_ft(x) # Expected 4-dimensional input for 4-dimensional weight [64, 3, 7, 7], but got 3-dimensional input of size [16, 201, 201] instead
            # Calculate loss           
            loss = criterion(outputs,y.long()) # cross entropy for a binary classification task
            # Backward pass
            loss.backward()
            # update weights
            optimizer.step()
            # evaluate performance
        
        # ------- Evaluations --------
        with torch.no_grad():
            # Training accuracy JANOS----------
            out_data = model_ft(x.float().to(device))
            
            loss_train = criterion(out_data,y.long())
            
            _, preds = torch.max(out_data, 1)
            running_corrects = torch.sum(preds == y.float().to(device))
            cls_train = running_corrects.double() / len(out_data)
            train_accuracy.append(cls_train.item())
        
            # Testing accuracy JANOS----------
            x_test, y_test ,_ = next(iter(test_dataloader))
            out_data = model_ft(x_test.float().to(device))
            
            loss_test = criterion(out_data,y_test.long().to(device))

            _, preds = torch.max(out_data, 1)
            running_corrects = torch.sum(preds == y_test.float().to(device))
            cls_val = running_corrects.double() / len(out_data)
            test_accuracy.append(cls_val.item())

        writer.add_scalar('Accuracy/train', cls_train.item(), epoch)
        writer.add_scalar('Accuracy/test', cls_val.item(), epoch)
        
        writer.add_scalar('loss/train', loss_train, epoch)
        writer.add_scalar('loss/test', loss_test, epoch)
                
    return model_ft

# save trained model and test on the entire test set for the accuracy of a given fold. Over each fold get the STD and mean for plotting downstream.

def test(model_ft,test_path):
    '''Test newly trained model on the entire held out test set for that fold and return reasults'''
    testing_data = ADJDataset(test_path)
    test_dataloader = DataLoader(testing_data, collate_fn=collate_fn,batch_size=32, shuffle=True) 
    test_accuracy = []
    with torch.no_grad():
        for step, (x, y, _) in enumerate(test_dataloader):   # gives batch data
            # ------- Training --------
            # Mount tensors on the GPU
            x = x.float().to(device)
            y = y.float().to(device)
            # zero grad
            # forward pass
            out_data = model_ft(x) # Expected 4-dimensional input for 4-dimensional weight [64, 3, 7, 7], but got 3-dimensional input of size [16, 201, 201] instead
            _, preds = torch.max(out_data, 1)
            running_corrects = torch.sum(preds == y)
            cls_val = running_corrects.double() / len(out_data)
            test_accuracy.append(cls_val.item())
        
    # take the mean of the test accruacy
    print(test_accuracy)
        
    return np.mean(test_accuracy)
        

def train_test_and_save(vairent_name):
    for i in range(5):
        train_path = "/mnt/ncshare/ozkilim/charge_pca_deepmut/CNN_training/cross_val_splits/" + vairent_name + "_train_" + str(i) +".csv"
        test_path = "/mnt/ncshare/ozkilim/charge_pca_deepmut/CNN_training/cross_val_splits/" + vairent_name + "_test_" + str(i) +".csv"        
        # Training
        model_ft = trainLoop(train_path,test_path)
        # Testing
        print("testing")
        fold_acc = test(model_ft,test_path)
        # save to csv reasults file
        row = [i, fold_acc]
        with open("/mnt/ncshare/ozkilim/charge_pca_deepmut/CNN_training/accs_50/" + vairent_name + ".csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)


def main():
    """For each varient train and test CNN of one of 5 foleds already generated. Save all reasults in seperate files to be collated and displayed as reasults. Currently this is to predict ACE2 binding affinity"""
    varients = ["wuhan","alpha","beta","delta","eta","omicronBA1"]
    for vairent_name in varients:
        train_test_and_save(vairent_name)
        
if __name__ == "__main__":
    main()