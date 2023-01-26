import requests
import sys
sys.path.append("../..")
from api_ip_addr import API_IP_ADDR
from gpt_key import GPT_KEY
import ast

def main():
    base_path=f"http://{API_IP_ADDR}/petri/"
    with open("seird.py", "r") as f:
        code = f.read()
    
    dict= {"code": code, "gpt_key": GPT_KEY}

    places = requests.post(base_path + "get_places", params=dict).text
    print("Places: " + places)

    params = requests.post(base_path + "get_parameters", params=dict).text
    print("Parameters: " + params)

    tran = requests.post(base_path + "get_transitions", params=dict).text
    print("Transitions: " + tran)

    with open("section2.txt", "r") as f:
        text = f.read()

    dict2= {"text": text, "gpt_key": GPT_KEY}

    places = ast.literal_eval(places)

    for place in places:
        dict2["place"] = place
        desc = requests.post(base_path + "match_place_to_text", params=dict2).text
        print(f"Description for {place}: {desc}")
        

if __name__ == "__main__":
    main()

