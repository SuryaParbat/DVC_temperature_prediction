# read the data from data source
# save it in the ../data/raw for further process

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)

    df = df.drop(columns=["UDI", "Product ID", "Type"])
    # replacing all " " with "_" in columns name
    new_col = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, index=False, header=new_col)
    # print(new_col)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="../params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)