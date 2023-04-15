"""
The Script uses Watson Language Translator service to do following operations:
- Translate English text to French
    - Accepts English text parameter and returns French value
- Translate French text to English
    - Accepts French text parameter and returns English value
"""
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

# Instance code starts here
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

# English to French Function
def english_to_french(englishText):
    ''' Translate English to French '''
    translation = language_translator.translate(englishText,model_id='en-fr').get_result()
    frenchText = translation["translations"][0]["translation"]
    return frenchText

# French to English Function
def french_to_english(frenchText):
    ''' Translate French to English '''
    translation = language_translator.translate(frenchText,model_id='fr-en').get_result()
    englishText = translation["translations"][0]["translation"]
    return englishText
