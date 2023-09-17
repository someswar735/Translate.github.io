from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from decouple import config
def extract_text_from_document(input_file_path:str):
    key=config('FORM_RECOGNIZER_KEY')
    endpoint=config('FORM_RECOGNIZER_ENDPOINT')
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
            return extracted_data.to_dict()['content']
        else:
            return "No content extracted from the document."

    except Exception as e:
        return str(e)