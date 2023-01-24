import requests
import sys
sys.path.append("../..")
from api_ip_addr import GPT_KEY



def main():
    path=f"http://{API_IP_ADDR}/code_formula/run"
    with open("CHIME_SVIIvR.py", "r") as f:
        code = f.read()
    with open("formula.tex_idx", "r") as f:
        formula = f.read()

    dict= {"input_code": code, "input_formula": formula, "gpt_key": GPT_KEY}

    r = requests.post(path, params=dict)
    print(r.text)

if __name__ == "__main__":
    main()