import os
import pandas as pd
from sklearn.model_selection import train_test_split

class AEData():
    def __init__(self, path, train_file_name, train_labels_file_name, test_data_file_name):
        self.path = path
        print(f"path: {path}")
        self.train_file_name = train_file_name
        self.train_labels_file_name = train_labels_file_name
        self.test_data_file_name =test_data_file_name

        print(f"Setting training data...")
        self.set_training_data(path, train_file_name)
        
        print(f"Setting training labels...")
        self.set_training_labels(path, train_labels_file_name)

        print(f"Setting test data...")
        self.set_test_data(path, test_data_file_name)

    def __getitem__(self, index):
        return self.data[index], self.labels[index]

    def __len__(self):
        return len(self.data)

    def get_data_helper(self, path, filename):
        #Create file path
        file_path = os.path.join(path, filename)

        #read data
        data = pd.read_csv(file_path)

        return data, file_path

    def set_training_data(self, path, filename):
        self.train_data, _ = self.get_data_helper(path, filename)

    def set_training_labels(self, path, filename):
        self.train_labels, _ = self.get_data_helper(path, filename)

    def set_test_data(self, path, filename):
        self.test_data, _ = self.get_data_helper(path, filename)
