import requests
from decouple import config

def translate_text(input_text:str, target_language:str):
    try:
        translation_url = config('TRANSLATE_ENDPOINT')
        translation_payload = {
            "text": input_text,
            "source_language": "en",
            "target_language": target_language,
        }
        translation_headers = {
            "content-type": 'application/x-www-form-urlencoded',
            "Accept-Encoding": 'application/gzip',
            "X-RapidAPI-Key": config('TRANSLATE_API_KEY'),
            "X-RapidAPI-Host": 'text-translator2.p.rapidapi.com',
        }

        translation_response = requests.post(
            translation_url, data=translation_payload, headers=translation_headers)

        if translation_response.status_code == 200:
            return translation_response.json()['data']['translatedText']
        else:
            return "Translation failed."

    except Exception as e:
        return str(e)