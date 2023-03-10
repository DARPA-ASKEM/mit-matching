import requests
import os
import sys
sys.path.append("../..")
from api_ip_addr import API_IP_ADDR
from gpt_key import GPT_KEY

def generate_headers(dir):
    fw = open(os.path.join(dir, 'headers.txt'), "w+")
    for filename in os.listdir(dir):
        data_path = os.path.join(dir, filename)
        # checking if it is a csv file
        if os.path.isfile(data_path) and data_path.endswith(".csv"):
            with open(data_path, "r") as fr:
                fw.write("{}:\t{}\n".format(filename, fr.read().split('\n')[0]))
    fw.close()

def main():
    path=f"http://{API_IP_ADDR}/code_dataset/run"
    with open("bucky_sample.py", "r") as f:
        code = f.read()

    generate_headers("./data_sample")
    headers = "./data_sample/headers.txt"

    dict= {"input_code": code, "input_dataset": headers, "gpt_key": GPT_KEY}

    r = requests.post(path, params=dict)
    print(r.text)

if __name__ == "__main__":
    main()