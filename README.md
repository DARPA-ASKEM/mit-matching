# mit-matching
This repository contains examples of how to use the REST API developed by the MIT team to match related data in different formats. 

This API was first made available during the January Hackathon and it is still preliminary. Our goal is to gather feedback on how to improve it. 

## Requirements

Please reach out to one of us to obtain the IP address with which to poulate `api_ip_addr.py`. 

You will also need a valid key for GPT-3, with which to populate `gpt_key.py`. You can sign up for such a key [here](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBxcUY4QTBQSVlNSjdRVDRjTGRhZ2lQdUpDeEZUMEhMOKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHh2VzlwQjFWMnItb05pVjJiNERqUWtFMzZ1VnhpOEJao2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q).

## API documentation

Concrete examples are available under the `api_use_example` directory, but here are some details on each call.

---

### `/avail_check/run` 

This is just a sanity check call to ensure that you can communicate with our server. 

- Request type: `POST`
- Inputs:
    - `input`, string: an arbitrary string
- Output: A longer string containing `input`.
---

### `/code_dataset/run` (WIP)


---

### `/code_formula/run` 

This call matches each line in a file that contains one LaTeX formula per line, with the most salient line of code from a python script.

- Request type: `POST`
- Inputs:
    - `input_code`, string: A python script repersented as a string.
    - `input_formulas`, string: A string containing LaTeX formulas separated by `\n` characters.
    - `gpt_key`, string: A key to the GPT-3 API.
- Output: A list (nesting level 0) of lists (nesting level 1). For each list in nesting level 1:
    - element 0, a string, is one of the input formulas in `input_formulas`
    - element 1 is a lnie of code from `input_code`.

---

### `/code_text/run`

This call matches each function name in a python script with the most relevant lines of text from a text description.

- Request type: `POST`
- Inputs:
    - `input_code`, string: A python script repersented as a string.
    - `input_text`, string: A multi-line text description, represented as a string using `\n` to denote line breaks.
    - `gpt_key`, string: A key to the GPT-3 API.
- Output: A list (nesting level 0) of lists (nesting level 1). For each list in nesting level 1:
    - element 0, a string, is a function name parsed from `input_code`
    - element 1, an integer, is the starting line number of the block of matching lines
    - element 2, an integer, is the ending line number(inclusive) of the block of matching lines
    - element 3, a string, is the block of matching lines, with successive lines separated by `\n`
