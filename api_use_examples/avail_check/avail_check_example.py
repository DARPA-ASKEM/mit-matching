import requests
import sys
sys.path.append("../..")
from api_ip_addr import API_IP_ADDR

def main():
    path=f"http://{API_IP_ADDR}/avail_check/run"
    word = "blahblah"
    dict= {"input": word}

    r = requests.post(path, params=dict)
    print(r.text)

if __name__ == "__main__":
    main()