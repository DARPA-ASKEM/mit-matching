import requests
import os
import sys
sys.path.append("../..")
from api_ip_addr import API_IP_ADDR
from gpt_key import GPT_KEY

def main():
    path=f"http://{API_IP_ADDR}/annotation/link_dataset_col_to_dkg"
    with open("./data_sample/covid_deaths_usafacts.csv", "r") as f:
        csv = f.read()

    print(csv)
    dict= {"csv_str": csv, "gpt_key": GPT_KEY}

    r = requests.post(path, params=dict)
    print(r.text)

if __name__ == "__main__":
    main()