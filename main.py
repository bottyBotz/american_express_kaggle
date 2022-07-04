#import numpy as np
import sys
import os
import time 

sys.path.append("")
import pandas as pd
from sklearn.model_selection import train_test_split
from dataloaders.dataloader import AEData





def main():
    #REFERENCE: https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
    #DATA_DIR = '/mnt/f/MLData/ae' 
    #sys.path.append(os.path.dirname(DATA_DIR))
    path = '/mnt/f/MLData/ae' 
    train_file_name = 'train_data.csv' 
    train_labels_file_name = 'train_labels.csv'
    test_data_file_name = 'test_data.csv'
    print(path)
    startTime = time.time()
    data = AEData(path, train_file_name, train_labels_file_name, test_data_file_name) #path, train_file_name, train_labels_file_name, test_data_file_name
    print(f"Time to load data: {time.time() - startTime}")

    print("Hello World!")


if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()