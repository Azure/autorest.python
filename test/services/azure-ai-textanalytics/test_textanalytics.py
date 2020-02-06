import logging

from azure.identity import DefaultAzureCredential
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient

def main():
    client = TextAnalyticsClient(
        endpoint="https://krpratic-textanalytics.cognitiveservices.azure.com/",
        credential=DefaultAzureCredential()
    )

    response = client.languages(
        documents=[{
            'id': 1,
            'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'
        }]
    )

    assert response.documents[0].detected_languages[0].name == "English"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()