from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    '''End-point /englishToFrench to translate e2f'''
    textToTranslate = request.args.get('textToTranslate')
    
    french_text = translator.english_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    '''End-point /frenchToEnglish to translate f2e'''
    textToTranslate = request.args.get('textToTranslate')

    english_text = translator.french_to_english(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    '''End-point / to render index page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
