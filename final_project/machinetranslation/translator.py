"""
Translator for English to French or French to English using IBM Watson
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2021-08-13'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Takes English text and returns a French translation
    """
    translation_response = language_translator.translate(\
                           text=english_text, model_id='en-fr')
    translation = dict(translation_response.get_result())
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Takes French text and returns an English translation
    """
    translation_response = language_translator.translate(\
    text=french_text, model_id='fr-en')
    translation = dict(translation_response.get_result())
    english_text = translation['translations'][0]['translation']

    return english_text
    