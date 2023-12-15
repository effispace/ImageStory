import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv('API_URL')
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(api_key, headers=headers, data=data)

    if response.status_code != 200:
        return f"Request failed with status code: {response.status_code}, message: {response.text}"

    return response.text
def returnTextImg():
    output = query("cuddles.png")
    parsed_output = json.loads(output)
    extracted_text = parsed_output[0]['generated_text']
    return extracted_text

returnTextImg()