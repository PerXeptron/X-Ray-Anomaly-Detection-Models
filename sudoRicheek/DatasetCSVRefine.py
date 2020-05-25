"""
How to use ?
* python DatasetCSVRefine.py [path-to-input-csv] [path-to-output-csv] [policy(optional)]
"""

import pandas as pd
import sys, os

csv_file_path = sys.argv[1]
output_file_path = sys.argv[2]
user_policy = None
if len(sys.argv) > 3 :
    user_policy = sys.argv[3]

def get_new_csv(pre_csv_path, policy="ones"):
    inp_csv = pd.read_csv(pre_csv_path, dtype=str)
    ### Make NaNs to zeroes
    ### Make -1s to something depending on policy

    out_csv = inp_csv.replace(to_replace="1.0", value="1")
    out_csv = out_csv.replace(to_replace="0.0", value="0")
    out_csv = out_csv.fillna('0')

    out_csv["Path"] = "/" + out_csv["Path"].astype(str)
    if policy == "ones" :
        out_csv = out_csv.replace(to_replace="-1.0", value="1")
        out_csv = out_csv.replace(to_replace="-1", value="1")
    elif policy == "zeroes" :
        out_csv = out_csv.replace(to_replace="-1.0", value="0")
        out_csv = out_csv.replace(to_replace="-1", value="1")
    else :
        out_csv = out_csv.replace(to_replace="-1.0", value="1")
        out_csv = out_csv.replace(to_replace="-1", value="1")

    return out_csv

def main():
    if user_policy is not None :
        new_csv = get_new_csv(csv_file_path, user_policy)
    else :
        new_csv = get_new_csv(csv_file_path)

    new_csv.to_csv(output_file_path)

if __name__ == "__main__" :
    main()