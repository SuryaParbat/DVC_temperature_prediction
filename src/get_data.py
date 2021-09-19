# read params
# process
# return dataframe

import yaml
import pandas as pd
import argparse
import logging
from src.logger import moniter, create_log_file

create_log_file('air_temp.log')

@moniter
def read_params(config_path):
    try:
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
        logging.debug(f"""read_params is Successfully executed""")
        return config

    except Exception as e:
        logging.error(f""" ERROR IN : read_params : {str(e)}\n""")
        return f"""ERROR IN : read_params : {str(e)}\n"""

@moniter
def get_data(config_path):
    try:
        config = read_params(config_path)
        # print(config)
        data_path = config["data_source"]["s3_source"]
        # print(data_path)
        df = pd.read_csv(data_path, encoding='utf-8')
        # print(df.head(5))
        logging.debug(f"""get_data is Successfully executed""")
        return df

    except Exception as e:
        logging.error(f""" ERROR IN : get_data : {str(e)}\n""")
        return f"""ERROR IN : get_data : {str(e)}\n"""


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="../params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
