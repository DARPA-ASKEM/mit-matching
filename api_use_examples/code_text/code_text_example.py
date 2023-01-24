import requests
import sys
sys.path.append("../..")
from api_ip_addr import API_IP_ADDR
from gpt_key import GPT_KEY

def main():
    path=f"http://{API_IP_ADDR}/code_text/run"
    with open("CHIME_SIR_while_loop.py", "r") as f:
        code = f.read()
    with open("description.txt", "r") as f:
        text = f.read()

    dict= {"input_code": code, "input_text": text, "gpt_key": GPT_KEY}

    r = requests.post(path, params=dict)
    print(r.text)

if __name__ == "__main__":
    main()