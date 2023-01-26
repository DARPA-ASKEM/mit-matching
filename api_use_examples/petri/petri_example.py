import requests
import sys
sys.path.append("../..")
from api_ip_addr import API_IP_ADDR
from gpt_key import GPT_KEY

def main():
    base_path=f"http://{API_IP_ADDR}/petri/"
    with open("seird.py", "r") as f:
        code = f.read()
    
    dict= {"code": code, "gpt_key": GPT_KEY}

    r = requests.post(base_path + "get_places", params=dict)
    print("Places: " + r.text)

    r = requests.post(base_path + "get_parameters", params=dict)
    print("Parameters: " + r.text)

    r = requests.post(base_path + "get_transitions", params=dict)
    print("Transitions: " + r.text)

if __name__ == "__main__":
    main()

