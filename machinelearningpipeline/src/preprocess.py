import pandas as pd
import sys
import yaml
import os

## Load parameters from param.yaml

params=yaml.safe_load(open("params.yaml"))['preprocess']

# preprocess input file from input path and store preprocessed output in output path 
# read input -> store it in data -> preprocess it
# make a dir name output path -> if exist dont make
# then store data into output_path in csv file without header and index -> means there is only csv data
# print that preprocessed pathe
def preprocess(input_path,output_path):
    data=pd.read_csv(input_path)
    
    os.makedirs(os.path.dirname(output_path),exist_ok=True)
    data.to_csv(output_path,header=None,index=False)
    print(f"Preprocesses data saved to {output_path}")

if __name__=="__main__":
    preprocess(params["input"],params["output"])
