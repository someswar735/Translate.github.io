from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
import requests
from decouple import config


def extract_layout_and_translate(input_file_path: str, endpoint: str, key: str, translate_api_key: str):
    try:
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )
        with open(input_file_path, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                model_id="prebuilt-document", document=f, locale="en-US"
            )
        extracted_data = poller.result()

        if extracted_data:
            content = extracted_data.to_dict()['content']
            print("Extracted content:", content)
            print("-----------------------------------")
            # Translate the content using a translation API
            translation_url = "https://text-translator2.p.rapidapi.com/translate"
            translation_payload = {
                "text": content,
                "source_language": "en",
                "target_language": "bn",  # Replace with your desired target language code
            }
            translation_headers = {
                "content-type": 'application/x-www-form-urlencoded',
                "Accept-Encoding": 'application/gzip',
                "X-RapidAPI-Key": translate_api_key,
                "X-RapidAPI-Host": 'text-translator2.p.rapidapi.com'
            }

            translation_response = requests.post(
                translation_url, data=translation_payload, headers=translation_headers)

            if translation_response.status_code == 200:
                translated_content = translation_response.json()[
                    'data']['translatedText']
                return translated_content
            else:
                return "Translation failed"

        return extracted_data.to_dict()

    except Exception as e:
        return str(e)


# Your Azure Form Recognizer credentials
endpoint = "https://rohi-123.cognitiveservices.azure.com/"
form_recognizer_key = config('FORM_RECOGNIZER_KEY')

# Your translation API key and target language
translate_api_key = config('TRANSLATE_API_KEY')
target_language = "fr"  # Replace with your desired target language code

# Path to the input PDF file
input_file_path = "./Sih Solution.pdf"

# Call the function and print the translated content
translated_content = extract_layout_and_translate(
    input_file_path, endpoint, form_recognizer_key, translate_api_key)
print("Translated content:", translated_content)
