import requests
from decouple import config


def summarize_text(input_text:str):
    try:
        url = config('OPENAI_SUMMARIZE_ENDPOINT')
        payload = {"text": input_text}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": config('OPENAI_SUMMARIZE_API_KEY'),
            "X-RapidAPI-Host": "open-ai21.p.rapidapi.com",
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()['result']
        else:
            return "Summarization failed."

    except Exception as e:
        return str(e)