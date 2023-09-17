from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
import requests , uuid
from decouple import config
import json

def extract_layout_and_translate(input_file_path: str, endpoint: str, form_recognizer_key: str, translate_api_key: str):
    try:
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(
                form_recognizer_key)
        )
        with open(input_file_path, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                model_id="prebuilt-document", document=f, locale="en-US"
            )
        extracted_data = poller.result()

        if extracted_data:
            content = extracted_data.to_dict()['content']
            print("Extracted content:", content)
            print("-----------------------------------")\
            # Translation API call
            translate_url = "https://api.cognitive.microsofttranslator.com/translate"
           

            headers = {
                'Ocp-Apim-Subscription-Key': translate_api_key,
                'Ocp-Apim-Subscription-Region': 'West US',
                'Content-Type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
            }

            data = [{
                'text':content,
            }]

            params = {
                'api-version': '3.0',
                'from': 'en',
                'textType': 'plain',
                'to': ['bn']
            }

            response = requests.post(
                translate_url, headers=headers, params=params, json=data)

            if response.status_code == 200:
                try:
                    translated_data = response.json()
                    return translated_data
                except json.JSONDecodeError:
                    return response.text # Return the response content as is
            else:
                return f"Translation failed with status code {response.status_code}: {response.text}"

        return extracted_data.to_dict()

    except Exception as e:
        return str(e)

# Your Azure Form Recognizer credentials
endpoint = "https://rohi-123.cognitiveservices.azure.com/"
form_recognizer_key = config('FORM_RECOGNIZER_KEY')

# Your translation API key and target language
translate_api_key = config('AZURE_TRANSLATE_API_KEY')

# Path to the input PDF file
input_file_path = "./Sih Solution.pdf"

# Call the function and print the translated content
translated_content = extract_layout_and_translate(
    input_file_path, endpoint, form_recognizer_key, translate_api_key)
print("Translated content:", translated_content)
